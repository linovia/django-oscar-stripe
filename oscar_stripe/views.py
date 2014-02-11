"""
oscar_stripe.views
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Xavier Ordoquy,
see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.views.generic import FormView


class StripeView(FormView):
    template_name = 'oscar_stripe/form.html'

    def form_valid(form):
        email = form.cleaned_data['stripeEmail']
        token = form.cleaned_data['stripeToken']
        print email, token