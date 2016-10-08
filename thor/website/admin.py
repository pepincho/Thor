from django.contrib import admin

from .models import City, Place, Event, UserProfile
from .models import EventUser


# Register your models here.


admin.site.register(City)
admin.site.register(Place)
admin.site.register(Event)

admin.site.register(UserProfile)

admin.site.register(EventUser)
