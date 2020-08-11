from django.contrib import admin

# Register your models here.
from .models import Chat

# This
admin.site.register(Chat)
#   OR
# @admin.register(Chat)
# class ChatAdmin(admin.ModelAdmin):
#     pass
