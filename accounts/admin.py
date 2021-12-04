from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ('image','admin_photo','address','address_ar',)
    readonly_fields = ['admin_photo','address','image']


admin.site.register(Profile,ProfileAdmin)

