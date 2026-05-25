import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO[str] = open(sys.argv[1])
            text: str = f.read()
            print("---")
            print(f"\n{text}\n")
            print("---")
            f.close()
            print(f"File '{sys.argv[1]}' closed.")
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
