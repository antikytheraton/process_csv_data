import csv

PATH = 'zip_codes.csv'

def extract_data_from_csv(*columns):
    with open(PATH) as f:
        reader = csv.reader(f)
        for row in reader:
            for column in columns:
                print(row[column])

# extract_data_from_csv(4)            # states
# extract_data_from_csv(4, 3, 13)        # municipality
extract_data_from_csv(1, 2)         # settlements
# extract_data_from_csv(6)            # zip codes
# extract_data_from_csv(0)            # zone codes
