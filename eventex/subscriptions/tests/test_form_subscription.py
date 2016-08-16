from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'cpf_digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'cpf_length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        # ARTHUR Guerra -> Arthur Guerra
        form = self.make_validated_form(name='ARTHUR Guerra')
        self.assertEqual('Arthur Guerra', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is an optional field"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optiona(self):
        """Phone is an optional field"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Either one email or phone must be provided"""
        form = self.make_validated_form(email='', phone='')

        # __all__ eh um erro do formulario, quando nem email nem telephone sao
        # informados, nao eh erro de nenhum dos campos, eh erro do form
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorMessage(self, form, field, msg):
        self.assertListEqual([msg], form.errors[field])

    def make_validated_form(self, **kwargs):
        valid_data = dict(name='Arthur Guerra', cpf='12345678901',
                          email='arthurjguerra@gmail.com', phone='73-988338187')

        data = dict(valid_data, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
