import csv
from panel.models import Token


def import_tokens_from_csv(csv_file):
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            code = row[0]
            token = Token(code=code)
            token.save()
            print("migrated:", token.code)

if __name__ == "__main__":
    csv_file_path = 'scripts/tokens.csv'
    import_tokens_from_csv(csv_file_path)