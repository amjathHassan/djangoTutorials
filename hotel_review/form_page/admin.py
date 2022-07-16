from django.contrib import admin

# Register your models here.

from .models import SignUpFormDB, ModelFormDB
admin.site.register(SignUpFormDB)
admin.site.register(ModelFormDB)