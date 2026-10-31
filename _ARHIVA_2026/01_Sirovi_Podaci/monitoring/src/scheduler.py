"""Run the public air-data and page monitors every day at 02:00."""

from __future__ import annotations

import time

import requests
import schedule

if __package__:
    from .daily_air_monitor import check_ui_changes, collect_public_annual_data
else:
    from daily_air_monitor import check_ui_changes, collect_public_annual_data


def run_daily_job() -> None:
    errors: list[str] = []

    try:
        collect_public_annual_data()
    except (OSError, ValueError, requests.RequestException) as error:
        errors.append(f"API: {error}")

    try:
        check_ui_changes()
    except (OSError, ValueError, requests.RequestException) as error:
        errors.append(f"UI: {error}")

    if errors:
        print("Dnevni monitoring nije u potpunosti obavljen: " + " | ".join(errors))
    else:
        print("Dnevni monitoring obavljen.")


def main() -> None:
    schedule.every().day.at("02:00").do(run_daily_job)
    print("Scheduler aktivan; dnevni zadatak pokrece se u 02:00.")
    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
