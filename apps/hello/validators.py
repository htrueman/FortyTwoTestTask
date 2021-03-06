import datetime
from django.core.exceptions import ValidationError


def validate_birthday(value):
    if value > datetime.datetime.now().date():
        raise ValidationError("Please, write your real date of birth!")
    return "OK"


def validate_name_fields(value):
    if not value.isalpha():
        raise ValidationError(
                                "This field should contain "
                                "alphabetic characters only!")
    return "OK"
