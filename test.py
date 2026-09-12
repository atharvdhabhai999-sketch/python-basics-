import subprocess
import re

def scan_wifi():
    result = subprocess.run(
        ["netsh", "wlan", "show", "networks", "mode=bssid"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    output = result.stdout

    ssid = None
    networks = []

    for line in output.splitlines():
        line = line.strip()

        # Wi-Fi name
        if line.startswith("SSID ") and ":" in line:
            ssid = line.split(":", 1)[1].strip()

        # Signal strength
        elif line.startswith("Signal") and ":" in line:
            signal = line.split(":", 1)[1].strip()

        # Security type
        elif line.startswith("Authentication") and ":" in line:
            security = line.split(":", 1)[1].strip()

            networks.append({
                "name": ssid,
                "signal": signal,
                "security": security
            })

    return networks


print("\nNearby Wi-Fi Networks\n")
print("-" * 60)

for wifi in scan_wifi():
    print(f"Name     : {wifi['name']}")
    print(f"Signal   : {wifi['signal']}")
    print(f"Security : {wifi['security']}")
    print("-" * 60)
