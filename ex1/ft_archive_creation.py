import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO[str] = open(sys.argv[1])
            text: str = f.read()
            print("---")
            print(f"\n{text}\n")
            print("---")
            f.close()
            print(f"File '{sys.argv[1]}' closed.")
            print("\nTransform data:")
            f = open(sys.argv[1])
            text = f.read()
            lines: list[str] = text.split("\n")
            new_lines: list[str] = []
            for line in lines:
                new_lines.append(line + "#")
            new_text: str = "\n".join(new_lines)
            print("---\n")
            print(f"{new_text}")
            print("\n---")
            f.close()
        except OSError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        file_name: str = input("Enter new file name (or empty): ")
        if file_name == "":
            print("No saving data.")
        else:
            print(f"Saving data to '{file_name}'")
            try:
                new_file: typing.IO[str] = open(file_name, "w")
                new_file.write(new_text)
                new_file.close()
                print(f"Data saved in file '{file_name}'.")
            except OSError as e:
                print(f"Error opening file '{file_name}': {e}")
