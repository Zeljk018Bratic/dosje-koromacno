"""Archive the publicly exposed annual air-quality series and page HTML."""

from __future__ import annotations

import hashlib
import os
from datetime import date, datetime, timezone
from pathlib import Path

import requests

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw_air_data"
API_URL = (
    "https://zrak.infomedica.hr/v1/public/locations/"
    "b54fb46b-32b6-4d66-af03-2612faae6deb/series"
)
UI_URL = "https://zrak.infomedica.hr/mobilna-stanica-koromacno"
POLLUTANTS = ("nox", "so2", "pm10", "no2")
REQUEST_TIMEOUT_SECONDS = 30
USER_AGENT = "Koromacno-public-data-monitor/1.0"


def _sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _write_new_file(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as destination:
        destination.write(content)
        destination.flush()
        os.fsync(destination.fileno())


def collect_public_annual_data(
    data_dir: Path | None = None,
    today: date | None = None,
) -> list[Path]:
    """Fetch and hash one annual JSON response per configured pollutant."""
    root = data_dir or RAW_DATA_DIR
    run_date = today or date.today()
    year = run_date.year
    retrieved_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    responses: list[tuple[str, str, bytes]] = []

    for pollutant in POLLUTANTS:
        response = requests.get(
            API_URL,
            params={"pollutant": pollutant, "range": "year", "year": year},
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
        content = response.content
        response.json()
        responses.append((pollutant, response.url, content))

    saved_paths: list[Path] = []
    hash_log = root / "hashes.txt"
    for pollutant, request_url, content in responses:
        filename = f"{pollutant}_{run_date.isoformat()}.json"
        destination = root / filename
        _write_new_file(destination, content)
        saved_paths.append(destination)
        record = (
            f"{filename}\t{_sha256(content)}\t{retrieved_at}\t{request_url}\n"
        )
        with hash_log.open("a", encoding="utf-8", newline="\n") as log:
            log.write(record)
            log.flush()
            os.fsync(log.fileno())
        print(f"Arhivirano: {destination} (SHA-256 {_sha256(content)})")

    return saved_paths


def _last_recorded_ui_hash(hash_log: Path) -> str | None:
    if not hash_log.exists():
        return None

    last_line = ""
    with hash_log.open("r", encoding="utf-8") as source:
        for line in source:
            if line.strip():
                last_line = line.rstrip("\r\n")
    if not last_line:
        return None

    fields = last_line.split("\t")
    if len(fields) != 3 or len(fields[1]) != 64:
        raise ValueError(f"Neispravan zapis u {hash_log}")
    return fields[1]


def check_ui_changes(
    data_dir: Path | None = None,
    today: date | None = None,
) -> Path | None:
    """Hash the page's raw HTML response and save it when it changes."""
    root = data_dir or DATA_DIR
    run_date = today or date.today()
    hash_log = root / "ui_hashes.txt"
    previous_hash = _last_recorded_ui_hash(hash_log)

    response = requests.get(
        UI_URL,
        headers={"User-Agent": USER_AGENT},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    content = response.content
    current_hash = _sha256(content)
    snapshot_path: Path | None = None

    if current_hash != previous_hash:
        stamp = datetime.now(timezone.utc).strftime("%H%M%S%f")
        filename = f"ui_snapshot_{run_date.isoformat()}.html"
        snapshot_path = root / "ui_snapshots" / filename
        if snapshot_path.exists():
            snapshot_path = snapshot_path.with_name(
                f"ui_snapshot_{run_date.isoformat()}_{stamp}.html"
            )
        _write_new_file(snapshot_path, content)
        print(f"HTML snapshot spremljen: {snapshot_path}")
    else:
        print("HTML odgovor nije promijenjen od zadnje provjere.")

    root.mkdir(parents=True, exist_ok=True)
    record_path = (
        snapshot_path.relative_to(root).as_posix() if snapshot_path else "-"
    )
    record = (
        f"{datetime.now(timezone.utc).isoformat(timespec='seconds')}"
        f"\t{current_hash}\t{record_path}\n"
    )
    with hash_log.open("a", encoding="utf-8", newline="\n") as log:
        log.write(record)
        log.flush()
        os.fsync(log.fileno())

    return snapshot_path


def main() -> None:
    collect_public_annual_data()
    check_ui_changes()


if __name__ == "__main__":
    main()
