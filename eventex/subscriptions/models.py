from django.db import models
from eventex.subscriptions.validators import validate_cpf, validate_cpf_length


class Subscription(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    cpf = models.CharField(max_length=11, verbose_name='CPF', validators=[validate_cpf, validate_cpf_length])
    email = models.EmailField(verbose_name='Mail', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Telephone #', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    paid = models.BooleanField(default=False, verbose_name='Pago')

    class Meta:
        verbose_name_plural = 'subscriptions_eventex'
        verbose_name = 'subscription_eventex'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
