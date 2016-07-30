import json
import datetime
from django.core.exceptions import ValidationError


def validate_birthday(value):
    if value > datetime.datetime.now().date():
        raise ValidationError("Please write your real date of birth!")
    return "Done"

# by the time when passing data to birthday field this field doesn't
# contain any data and it can't be sent to the validator
# so we parse data from fixture to aviod that problem

with open('apps/hello/fixtures/initial_data.json') as data_file:
    data = json.load(data_file)
    for jo in data:
        birth_str = data[0]['fields']['birthday']
birth = datetime.datetime.strptime(birth_str, "%Y-%m-%d").date()
