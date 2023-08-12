from django.contrib import admin

# Register your models here.
from app.models import User, Contact, HotelStaff, Room,  Blog

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(HotelStaff)
admin.site.register(Room)