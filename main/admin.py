from django.contrib import admin

from .models import Illness,Drug,Post,Reply


admin.site.register(Illness)
admin.site.register(Drug)
admin.site.register(Post)
admin.site.register(Reply)
