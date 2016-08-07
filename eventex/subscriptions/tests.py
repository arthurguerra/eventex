from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use /subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def NOT_EXECUTE_test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 2)
        self.assertContains(self.resp, 'type="text"', 0)
        self.assertContains(self.resp, 'type="email"', 0)
        self.assertContains(self.resp, 'type="submit"', 1)

    def test_csrf(self):
        """Html must contain CSRF"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Arthur Guerra', cpf='12345678901',
                    phone='73-98833-8187', email='arthurjguerra@gmail.com')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

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
        self.assertIn('Arthur Guerra', self.email.body)
        self.assertIn('12345678901', self.email.body)
        self.assertIn('arthurjguerra@gmail.com', self.email.body)
        self.assertIn('73-98833-8187', self.email.body)


class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)


class SubscribeSuccessMessage(TestCase):
    def setUp(self):
        self.data = dict(name='Arthur Guerra', cpf='12345678901',
                    phone='73-98833-8187', email='arthurjguerra@gmail.com')
        self.resp = self.client.post('/inscricao/', self.data, follow=True)

    def test_message(self):
        self.assertContains(self.resp, 'Inscricao realizada com sucesso!')
