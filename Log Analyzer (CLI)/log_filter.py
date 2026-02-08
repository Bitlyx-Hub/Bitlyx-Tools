import sys
from pathlib import Path

file_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("server.log")

try:
    with open(file_path, 'r') as f:
        for line in f:
            if "ERROR" in line or "WARNING" in line:
                print(line.rstrip())
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found", file=sys.stderr)
    sys.exit(1)
