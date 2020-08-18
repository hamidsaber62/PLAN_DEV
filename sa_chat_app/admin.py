from django.contrib import admin

# Register your models here.
from .models import Chat


# This
# admin.site.register(Chat)
#   OR
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'message', 'content_type', 'object_id', 'content_object', 'create_chat_datetime', 'seen_chat')
    # pass
