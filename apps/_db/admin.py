from django.contrib import admin
from _db.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
