django-oscar-stripe
===================

Getting Started
---------------

Add the following variables to your settings file:

    STRIPE_SECRET_KEY = 'xxx'
    STRIPE_PUBLIC_KEY = 'yyy'

Next you need to add the Stripe's urls:

    from stripe.dashboard.app import application as stripe_app

    urlpatterns = ('',
        ...
        # Optional
        (r'^dashboard/stripe/', include(stripe_app.urls)),
        ...
    )

If want the dashboard view, you'll need in your settings:

    from django.utils.translation import ugettext_lazy as _
    OSCAR_DASHBOARD_NAVIGATION.append({
        'label': _('Stripe'),
        'icon': 'icon-globe',
        'children': [
            {
                'label': _('Stripe transactions'),
                'url_name': 'stripe-list',
            },
        ]
    })

