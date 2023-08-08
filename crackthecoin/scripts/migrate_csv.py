import csv
from django.contrib.auth import get_user_model


User = get_user_model()
def import_users_from_csv(csv_file):
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            username = row[0]
            password = row[1]
            user = User(username=username)
            user.set_password(password)
            user.save()
            break

if __name__ == "__main__":
    csv_file_path = 'Invitados_Luciofest.csv'
    import_users_from_csv(csv_file_path)