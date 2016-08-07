from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        # caso de sucesso (nenhum erro no form)
        if form.is_valid():
            form.full_clean()

            body = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)

            mail.send_mail('Confirmacao de Inscricao',
                           body,
                           'contato@eventex.com.br',
                           ['contato@eventex.com.br', form.cleaned_data['email']])

            messages.success(request, 'Inscricao realizada com sucesso!')

            return HttpResponseRedirect('/inscricao/')

        # caso invalido do form
        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
