import csv

STRING = "electr"

def remove_rows_from_csv(input_file, output_file, removal_condition):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            if not removal_condition(row):
                writer.writerow(row)

# Define the removal condition
def should_remove_row(row):
    return STRING in row['AcceptedItems']

input_file = 'repair.csv'
output_file = 'repaircleaned.csv'
remove_rows_from_csv(input_file, output_file, should_remove_row)
print(f"Cleaned CSV saved as {output_file}")
