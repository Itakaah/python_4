def secure_archive(
    filename: str, mode: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(filename) as f:
                data = f.read()
            return (True, data)
        else:
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("ancient_fragment.txt", "write"))
