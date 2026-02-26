from django.contrib import admin

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('image')
