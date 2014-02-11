"""
oscar_stripe.urls
~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Xavier Ordoquy,
see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns('',
    url(r'^payment/', views.StripeView.as_view(), name='stripe-payment'),
)
