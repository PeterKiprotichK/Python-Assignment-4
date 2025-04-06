def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (example: convert text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to {output_filename}")
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print(f"Error: Could not read or write to the file.")
