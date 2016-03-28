from django.db import models
from django.utils.translation import ugettext_lazy as _


class Script(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    source = models.TextField(_('Source'))

    class Meta:
        verbose_name = _('Script')
        verbose_name_plural = _('Scripts')

    def __unicode__(self):
        return self.name
