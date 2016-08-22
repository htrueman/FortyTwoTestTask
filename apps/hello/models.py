from django.db import models

from apps.hello.validators import validate_birthday

import StringIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


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
    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='img/')

    def save(self, *args, **kwargs):
        SamePhoto = False
        if self.photo:
            size = (200, 200)
            person = MyData.objects.get(id=self.id)
            if person.photo == self.photo:
                SamePhoto = True
            image = Image.open(StringIO.StringIO(self.photo.read()))
            (width, height) = image.size
            if (width > 200) or (height > 200):
                image.thumbnail(size, Image.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='jpeg', quality=70)
            output.seek(0)
            self.photo = InMemoryUploadedFile(
                output,
                'ImageField', "%s.jpg" %
                              self.photo.name.split('.')[0],
                'image/jpeg', output.len, None)
        try:
            this = MyData.objects.get(id=self.id)
            if this.photo == self.photo or SamePhoto:
                self.photo = this.photo
            else:
                this.photo.delete(save=False)
        except:
            pass
        super(MyData, self).save(*args, **kwargs)

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
