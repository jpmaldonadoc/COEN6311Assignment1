from django.contrib import admin
from ConferenceManager.models import attendee, Event, Room
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ("NameEvent","Time","NameRoom")
    search_fields = ("NameEvent","Time","NameRoom")

class attendeeAdmin(admin.ModelAdmin):
    list_display = ("Name","phonenumber","email", "speaker")
    search_fields = ("Name","phonenumber","email", "speaker")

class RoomAdmin(admin.ModelAdmin):
    list_display = ("NameRoom","Address")
    search_fields = ("NameRoom", "Address")


admin.site.register(attendee, attendeeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Room, RoomAdmin)



