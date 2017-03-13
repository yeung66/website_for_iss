from django.contrib import admin
from models import Time, Message, Team
# Register your models here.
class Message_admin(admin.ModelAdmin):
    list_display = ('title', 'type')

class Team_admin(admin.ModelAdmin):
    list_display = ('teamName', 'type')

admin.site.register(Time)
admin.site.register(Message, Message_admin)
admin.site.register(Team, Team_admin)


