"""Monitor unique items scraping progress."""

import json
import time
from pathlib import Path


def monitor_progress(
    file_path: str = "data/uniques_scraped.json", interval: int = 30
) -> None:
    """Monitor scraping progress.

    :param file_path: Path to scraped data file.
    :param interval: Check interval in seconds.
    """
    print("Monitoring scraping progress...")
    print(f"File: {file_path}")
    print(f"Check interval: {interval} seconds")
    print("Press Ctrl+C to stop monitoring\n")

    last_count = 0

    try:
        while True:
            path = Path(file_path)

            if path.exists():
                try:
                    with open(path, encoding="utf-8") as f:
                        data = json.load(f)

                    if "uniques" in data:
                        count = len(data["uniques"])
                        file_size = path.stat().st_size / 1024

                        if count > last_count:
                            new_items = count - last_count
                            msg = (
                                f"[{time.strftime('%H:%M:%S')}] {count} items "
                                f"(+{new_items}) - {file_size:.2f} KB"
                            )
                            print(msg)
                            last_count = count
                        elif count == last_count and count > 0:
                            msg = (
                                f"[{time.strftime('%H:%M:%S')}] {count} items "
                                f"(no change) - {file_size:.2f} KB"
                            )
                            print(msg)
                    else:
                        msg = (
                            f"[{time.strftime('%H:%M:%S')}] File exists "
                            f"but no 'uniques' key yet"
                        )
                        print(msg)
                except json.JSONDecodeError:
                    msg = (
                        f"[{time.strftime('%H:%M:%S')}] File exists but is "
                        f"incomplete (JSON decode error)"
                    )
                    print(msg)
                except Exception as e:
                    print(f"[{time.strftime('%H:%M:%S')}] Error: {e}")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] File not created yet...")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")
        if path.exists():
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                if "uniques" in data:
                    print(f"Final count: {len(data['uniques'])} unique items")
            except Exception:
                pass


if __name__ == "__main__":
    import sys

    interval = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    monitor_progress(interval=interval)
