from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import UserChangeForm
from users.models import User
 
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
 
class CustomUserAdmin(DefaultUserAdmin):
    form = CustomUserChangeForm
    add_form = DefaultUserAdmin.add_form
    model = User
    add_fieldsets = DefaultUserAdmin.add_fieldsets
    add_fieldsets[0][1]['fields'] += ('carnumber',)
 
admin.site.register(User, CustomUserAdmin)