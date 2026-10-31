import hashlib
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import Mock, patch

from src import daily_air_monitor as monitor
from src import scheduler


class DailyAirMonitorTests(unittest.TestCase):
    def test_collect_archives_each_public_annual_series_and_hash(self) -> None:
        body = b'{"values":[1,2,3]}'
        response = Mock()
        response.content = body
        response.url = "https://example.test/series"
        response.json.return_value = json.loads(body)
        response.raise_for_status.return_value = None
        run_date = date(2026, 10, 28)

        with tempfile.TemporaryDirectory() as temporary_directory:
            data_dir = Path(temporary_directory)
            with patch.object(monitor.requests, "get", return_value=response) as get:
                paths = monitor.collect_public_annual_data(data_dir, run_date)

            self.assertEqual(
                [path.name for path in paths],
                [
                    "nox_2026-10-28.json",
                    "so2_2026-10-28.json",
                    "pm10_2026-10-28.json",
                    "no2_2026-10-28.json",
                ],
            )
            self.assertTrue(all(path.read_bytes() == body for path in paths))
            log_lines = (data_dir / "hashes.txt").read_text(
                encoding="utf-8"
            ).splitlines()
            self.assertEqual(len(log_lines), 4)
            self.assertTrue(
                all(hashlib.sha256(body).hexdigest() in line for line in log_lines)
            )
            self.assertEqual(
                [item.kwargs["params"]["pollutant"] for item in get.call_args_list],
                ["nox", "so2", "pm10", "no2"],
            )
            self.assertTrue(
                all(
                    item.kwargs["params"]["range"] == "year"
                    for item in get.call_args_list
                )
            )

    def test_existing_daily_archive_is_never_overwritten(self) -> None:
        run_date = date(2026, 10, 28)
        with tempfile.TemporaryDirectory() as temporary_directory:
            data_dir = Path(temporary_directory)
            existing = data_dir / "nox_2026-10-28.json"
            existing.write_bytes(b"original")
            response = Mock()
            response.content = b'{"values":[]}'
            response.url = "https://example.test/series"
            response.json.return_value = {}
            response.raise_for_status.return_value = None

            with patch.object(monitor.requests, "get", return_value=response):
                with self.assertRaises(FileExistsError):
                    monitor.collect_public_annual_data(data_dir, run_date)

            self.assertEqual(existing.read_bytes(), b"original")

    def test_ui_snapshot_is_saved_on_first_run_and_hash_is_logged(self) -> None:
        body = b"<html><title>public page</title></html>"
        response = Mock()
        response.content = body
        response.encoding = "utf-8"
        response.raise_for_status.return_value = None

        with tempfile.TemporaryDirectory() as temporary_directory:
            data_dir = Path(temporary_directory)
            with patch.object(monitor.requests, "get", return_value=response) as get:
                snapshot = monitor.check_ui_changes(data_dir, date(2026, 10, 28))

            self.assertEqual(
                snapshot,
                data_dir / "ui_snapshots" / "ui_snapshot_2026-10-28.html",
            )
            self.assertEqual(snapshot.read_bytes(), body)
            log_line = (data_dir / "ui_hashes.txt").read_text(
                encoding="utf-8"
            ).splitlines()[0]
            self.assertIn(hashlib.sha256(body).hexdigest(), log_line)
            get.assert_called_once()

    def test_unchanged_ui_response_does_not_create_another_snapshot(self) -> None:
        body = b"<html>same page</html>"
        digest = hashlib.sha256(body).hexdigest()
        response = Mock()
        response.content = body
        response.encoding = "utf-8"
        response.raise_for_status.return_value = None

        with tempfile.TemporaryDirectory() as temporary_directory:
            data_dir = Path(temporary_directory)
            data_dir.mkdir(parents=True, exist_ok=True)
            (data_dir / "ui_hashes.txt").write_text(
                f"2026-10-27T02:00:00+00:00\t{digest}\tui_snapshots/old.html\n",
                encoding="utf-8",
            )
            with patch.object(monitor.requests, "get", return_value=response):
                snapshot = monitor.check_ui_changes(data_dir, date(2026, 10, 28))

            self.assertIsNone(snapshot)
            self.assertFalse((data_dir / "ui_snapshots").exists())

    def test_scheduler_job_runs_both_monitoring_steps(self) -> None:
        with (
            patch.object(scheduler, "collect_public_annual_data") as collect,
            patch.object(scheduler, "check_ui_changes") as check_ui,
        ):
            scheduler.run_daily_job()

        collect.assert_called_once_with()
        check_ui.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
