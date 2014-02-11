"""
oscar_stripe.forms
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Xavier Ordoquy,
see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django import forms

# Form should match what the real stripe form expects
class StripeForm(forms.Form):
    stripeEmail = forms.CharField()
    stripeToken = forms.CharField()
