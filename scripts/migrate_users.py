import csv
from django.contrib.auth import get_user_model

csv_file_path = 'scripts/Invitados_Luciofest.csv'

User = get_user_model()

def import_users_from_csv(csv_file = csv_file_path):
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                username = row[0]
                password = row[1]
                user = User(username=username)
                user.set_password(password)
                user.save()
                print("migrated:", user.username, user.password)
            except Exception as e:
                print("error:", e)
                continue

if __name__ == "__main__":
    csv_file_path = 'scripts/Invitados_Luciofest.csv'
    import_users_from_csv(csv_file_path)