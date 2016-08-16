from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    email = models.EmailField(verbose_name='Mail')
    phone = models.CharField(max_length=20, verbose_name='Telephone #')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    paid = models.BooleanField(default=False, verbose_name='Pago')

    class Meta:
        verbose_name_plural = 'subscriptions_eventex'
        verbose_name = 'subscription_eventex'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
