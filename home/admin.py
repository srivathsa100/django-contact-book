from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ("FirstName", "LastName", "Email", "ContactNumber")
    search_fields = ("FirstName", "LastName", "Email", "ContactNumber")

admin.site.register(Contact, ContactAdmin)
