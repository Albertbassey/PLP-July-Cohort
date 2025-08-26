def modify_content(line):
    # Example modification: convert to uppercase
    return line.upper()

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as infile:
            lines = infile.readlines()

        modified_lines = [modify_content(line) for line in lines]

        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Could not read the file. Check permissions or file integrity.")

if __name__ == "__main__":
    main()
