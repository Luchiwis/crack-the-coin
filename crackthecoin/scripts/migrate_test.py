
from django.contrib.auth import get_user_model

# try example
User = get_user_model()

new_user = User.objects.create_user(username='Lucio Petrucci')
new_user.set_password('test')
new_user.save()