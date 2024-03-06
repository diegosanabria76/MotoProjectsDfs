import csv
import gzip
import re

def highlight_occurrences(text, search_terms):
    # Create a regex pattern that matches any of the search terms
    pattern = '|'.join(search_terms)
    # Use a substitution pattern to highlight the occurrences
    highlighted_text = re.sub(pattern, lambda match: f'\033[1;31m{match.group(0)}\033[m', text, flags=re.IGNORECASE)
    return highlighted_text

def process_gz(input_file, search_terms, output_file):
    with gzip.open(input_file, 'rt') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            highlighted_row = [highlight_occurrences(cell, search_terms) for cell in row]
            writer.writerow(highlighted_row)

# Example usage:
input_file = 'callsSample.txt.gz'
output_file = 'output.csv'
search_terms = input('Enter search terms separated by commas: ').split(',')

process_gz(input_file, search_terms, output_file)
