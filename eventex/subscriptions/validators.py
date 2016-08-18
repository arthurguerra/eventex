from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas numeros', 'cpf_digits')


def validate_cpf_length(value):
    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 numeros', 'cpf_length')
