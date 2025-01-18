import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
print(f"Processing file: {filename}")