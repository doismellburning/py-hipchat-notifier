# Script just using the Python stdlib (and cURL) to send HipChat notifications (lack of dependencies => single file => easy to drop in to other scenarios)

import argparse
import subprocess
import sys
import urllib

parser = argparse.ArgumentParser(description="Send HipChat notifications")
parser.add_argument('--room-id', required=True, help="")
parser.add_argument('--from', required=True)
parser.add_argument('--message', required=True)
parser.add_argument('--auth-token', required=True)

args = parser.parse_args()

if args.message == "-":
    args.message = sys.stdin.read()

hipchat_data = urllib.urlencode(vars(args))

print subprocess.check_output(["curl", "--silent", "--data", hipchat_data, "https://api.hipchat.com/v1/rooms/message"])
