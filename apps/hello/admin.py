from django.contrib import admin
from .models import MyData, RequestKeeperModel, Signal

admin.site.register(MyData)
admin.site.register(RequestKeeperModel)
admin.site.register(Signal)
