#!/usr/bin/env python3

import argparse
import subprocess
import json
import sys


def get_all_containers():
    result = subprocess.run(['docker', 'ps', '-aq'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Failed to list containers", file=sys.stderr)
        sys.exit(1)
    return result.stdout.strip().splitlines()


def inspect_container(container_id):
    result = subprocess.run(['docker', 'inspect', container_id], capture_output=True, text=True)
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)[0]


def find_volume_mounts(volume_names):
    containers = get_all_containers()

    matches = []

    for container_id in containers:
        container_data = inspect_container(container_id)
        if not container_data:
            continue

        container_name = container_data.get("Name", "").lstrip("/")
        mounts = container_data.get("Mounts", [])

        for mount in mounts:
            if mount.get("Type") == "volume" and mount.get("Name") in volume_names:
                matches.append({
                    "volume": mount["Name"],
                    "container_name": container_name,
                    "container_id": container_id,
                    "mountpoint": mount["Destination"]
                })

    return matches


def main():
    parser = argparse.ArgumentParser(description="Find where Docker volumes are mounted in containers.")
    parser.add_argument("volumes", nargs="+", help="One or more Docker volume names or IDs")
    args = parser.parse_args()

    mounts = find_volume_mounts(args.volumes)

    if not mounts:
        print("No containers found using the specified volume(s).")
    else:
        for match in mounts:
            print(f"📦 Volume: {match['volume']}")
            print(f"🔗 Container: {match['container_name']} ({match['container_id']})")
            print(f"📁 Mountpoint inside container: {match['mountpoint']}\n")


if __name__ == "__main__":
    main()
