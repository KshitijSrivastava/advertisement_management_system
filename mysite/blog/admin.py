from .models import Post,Comment
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields ="__all__"

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets

# Register your models here.

admin.site.register(User,MyUserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
