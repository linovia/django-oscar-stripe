"""
oscar_stripe.templatetags.stripe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Xavier Ordoquy,
see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def stripe_form(context):
    return """
<form action="{%% url 'stripe-payment' %%}" class="payment-details form-horizontal" method="POST">
    {%% csrf_token %%}
    <script
        src="https://checkout.stripe.com/checkout.js" class="stripe-button"
        data-key="%s"
        data-amount="%i"
        data-name="%s"
        data-description="%s"
        data-image="/128x128.png">
    </script>
    {{ stripe_form.as_p }}
</form>
""" % (context['STRIPE_PUBLIC_KEY'], 2000, "Demo site", "2 widgets ($20.00)")
