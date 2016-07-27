from django.db import models


class MyData(models.Model):
    class Meta(object):
        verbose_name = "Personal Data"

    name = models.CharField(
        max_length=30)
    last_name = models.CharField(
        max_length=30)
    birthday = models.DateField()
    bio = models.CharField(
        max_length=256,
        blank=True,
        null=True)
    email = models.CharField(
        max_length=30)
    jabber = models.CharField(
        max_length=30)
    skype = models.CharField(
        max_length=30)
    other_conts = models.CharField(
        max_length=256,
        blank=True,
        null=True)

    def __unicode__(self):
        return u"%s %s" % (self.name, self.last_name)