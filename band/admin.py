from django.contrib import admin
from .models import Concert, Member

# Register your models here.
admin.site.register(Concert)
admin.site.register(Member)