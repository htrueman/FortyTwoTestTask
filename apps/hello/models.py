from django.db import models

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

    def __unicode__(self):
        return u"%s %s" % (self.name, self.last_name)


class RequestKeeperModel(models.Model):
    name = models.URLField(default='')
    method = models.CharField(max_length=6, default='')
    date = models.DateTimeField(auto_now=True, verbose_name="date")
    status = models.IntegerField(max_length=3, default=1)
    author = models.CharField(
        max_length=256,
        verbose_name="author",
        default="anonymous")

    def __str__(self):
        return self.name
