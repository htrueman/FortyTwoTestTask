from django.db import models

import datetime
from django.core.exceptions import ValidationError
from apps.hello.validators import validate_birthday


class MyData(models.Model):
    class Meta(object):
        verbose_name = "Personal Data"

    name = models.CharField(
        max_length=30)
    last_name = models.CharField(
        max_length=30)
    birthday = models.DateField(validators=[validate_birthday])
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


class RequestKeeperModel(models.Model):
    path = models.CharField(max_length=1024, verbose_name="path")
    method = models.CharField(max_length=6, verbose_name="method")
    date = models.DateTimeField(auto_now=True, verbose_name="date")
    is_viewed = models.BooleanField(default=False, verbose_name="is_viewed")

    class Meta:
        ordering = ['-date']
