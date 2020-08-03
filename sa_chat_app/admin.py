from django.contrib import admin

# Register your models here.
from .models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass
