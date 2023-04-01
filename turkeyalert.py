#!/usr/bin/env python3

import asyncio
import os
import json
import subprocess
import sys

from rich import print

HAMALERT_SERVER = 'hamalert.org'
HAMALERT_PORT = 7300
HAMALERT_USERNAME = os.environ.get('HAMALERT_USERNAME')
HAMALERT_PASSWORD = os.environ.get('HAMALERT_PASSWORD')

def process_line(line):
    print(f"[cyan]\[hamalert][/cyan] {line}")

    # Each line after the initial login is a JSON object.
    if not line.startswith('{'):
        return

    alert = json.loads(line)

    # Call notify-send to display a desktop notification.
    subprocess.run(['notify-send', 'HamAlert Notification!', alert['title']])


async def main():
    reader, writer = await asyncio.open_connection(HAMALERT_SERVER, HAMALERT_PORT)

    writer.write(f'{HAMALERT_USERNAME}\r\n'.encode())
    writer.write(f'{HAMALERT_PASSWORD}\r\n'.encode())
    writer.write(f'set/json\r\n'.encode())

    await writer.drain()

    while True:
        data = await reader.readline()
        if not data:
            break
        process_line(data.decode().strip())
        sys.stdout.flush()

if __name__ == '__main__':
    asyncio.run(main())
