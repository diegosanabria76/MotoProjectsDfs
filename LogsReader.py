import csv
import re

def process_csv(input_file, Date, Call_id, Call_id_long, output_file):
    result = []

    with open(input_file, 'r') as csvfile:
        for line in csvfile:
            # Extract date, call ID, and long call ID if available
            date = None
            call_id = None
            call_id_long = None

            # Search for the specific call ID pattern
            match_call_id = re.search(r'callID=([0-9a-fA-F\-]+)', line)
            if match_call_id:
                call_id = match_call_id.group(1)

            # Search for the date pattern
            match_date = re.search(r'\b{}\b'.format(re.escape(Date)), line)
            if match_date:
                date = match_date.group()

            # Append to result if any of the search terms are found
            if call_id or date:
                result.append([date, call_id, call_id_long])

    # Write the results to the output file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Date', 'Call_id', 'Call_id_long'])  # Write header to output file
        for row in result:
            writer.writerow(row)

# Example usage:
input_file = 'callsSample.txt'
output_file = 'output.csv'
Date = input('Please enter Date to search: ')
Call_id = input('Please enter call id: ')
Call_id_long = input('Please enter long call id: ')

process_csv(input_file, Date, Call_id, Call_id_long, output_file)
