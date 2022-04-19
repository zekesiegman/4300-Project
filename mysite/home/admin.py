from django.contrib import admin
from .models import Profile
from .models import Item
from .models import Cart

# Register your models here.

admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Cart)
