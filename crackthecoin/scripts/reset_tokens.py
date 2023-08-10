import csv
from panel.models import Token


def reset_tokens():
    Token.objects.all().update(used=False, date_used=None, used_by=None)
    print("Tokens reseteados")