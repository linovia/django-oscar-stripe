"""
oscar_stripe.models
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 by Xavier Ordoquy,
see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.db import models
from django.utils.translation import ugettext as _

from oscar.core.compat import AUTH_USER_MODEL


class StripeToken(models.Model):
    """
    Model representing a Token for strip API
    """
    user = models.ForeignKey(AUTH_USER_MODEL,
        related_name='stripe_token',
        verbose_name=_("User"))
    token = models.CharField(max_length=128)

    def __unicode__(self):
        return u'Token %s' % self.token

    class Meta:
        abstract = True
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")
