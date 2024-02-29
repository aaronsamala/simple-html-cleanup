# This will ingest a file and remove all the HTML tags from it
# and save the result to a new text file.
# Usage: python simple-html-cleanup.py <input-file> <output-file>
# Example: python simple-html-cleanup.py input.html output.txt

import sys
import re

def main():
    if len(sys.argv) != 3:
        print('Usage: python simple-html-cleanup.py <input-file> <output-file>')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as file:
        data = file.read()
        data = re.sub(r'<[^>]*>', '', data)
        with open(output_file, 'w') as file:
            file.write(data)

if __name__ == '__main__':
    main()
