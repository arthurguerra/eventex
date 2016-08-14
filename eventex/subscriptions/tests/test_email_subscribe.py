from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Arthur Guerra', cpf='12345678901',
                    phone='73-98833-8187', email='arthurjguerra@gmail.com')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmacao de Inscricao'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'arthurjguerra@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Arthur Guerra',
            '12345678901',
            'arthurjguerra@gmail.com',
            '73-98833-8187',
        ]

        for c in contents:
            with self.subTest():
                self.assertIn(c, self.email.body)
