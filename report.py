import json


def save_report(host, results):
    filename= f"{host}_scan_report.json"

    with open (filename, "w") as f:
        json.dump(results, f, indent=4)

    print(f"\nReport saved to {filename}")