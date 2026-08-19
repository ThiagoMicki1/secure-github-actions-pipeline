from __future__ import annotations

import json
import sys
import urllib.request


def fetch_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=5) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    base_url = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://127.0.0.1:8000"
    health = fetch_json(f"{base_url}/health")
    controls = fetch_json(f"{base_url}/security-controls")

    if health.get("status") != "healthy":
        print("[FAIL] /health did not return healthy")
        return 1

    if "container-scanning" not in controls.get("controls", []):
        print("[FAIL] /security-controls missing container-scanning")
        return 1

    print(f"[PASS] App validation succeeded for {base_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
