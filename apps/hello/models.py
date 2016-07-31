from django.db import models

import datetime
from django.core.exceptions import ValidationError


class MyData(models.Model):
    class Meta(object):
        verbose_name = "Personal Data"

    name = models.CharField(
        max_length=30)
    last_name = models.CharField(
        max_length=30)
    birthday = models.DateField()
    bio = models.TextField(
        max_length=256,
        blank=True,
        null=True)
    email = models.EmailField(
        max_length=30)
    jabber = models.EmailField(
        max_length=30)
    skype = models.CharField(
        max_length=30)
    other_conts = models.TextField(
        max_length=256,
        blank=True,
        null=True)

    def save(self, *args, **kwargs):
        if self.birthday > datetime.datetime.now().date():
            raise ValidationError(u'Please write your real date of birth!')
        super(MyData, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.last_name)

