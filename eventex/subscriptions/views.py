from django.views.generic import DetailView, CreateView
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateMixin
from eventex.subscriptions.models import Subscription


class EmailCreateView(EmailCreateMixin, CreateView):
    def form_valid(self, form):
        response = super().form_valid(form)
        self.send_mail()
        return response


new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmacao de Inscricao')

detail = DetailView.as_view(model=Subscription)
