from django.contrib import admin
from .models import *
# Register your models here.
# a1

# user -> myuser - user1@lib

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(BookInstance)