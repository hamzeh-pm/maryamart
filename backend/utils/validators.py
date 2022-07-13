from django.core.exceptions import ValidationError


def validate_mobile(value):
    if len(value) != 10:
        raise ValidationError("mobile number must be 10 digit")

    if not value.isdigit():
        raise ValidationError("mobile number must only contains digits")
