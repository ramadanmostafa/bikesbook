from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser, Subscriber,Contact, Setting
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('mobile_number', 'password')}),
        (_('Personal info'), {'fields': ('username', 'first_name',
                                         'last_name', 'avatar','membership_id','mobile_number','pin_code')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',)}
         ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('mobile_number', 'first_name', 'last_name', 'is_staff')
    search_fields = ('mobile_number', 'first_name', 'last_name')
    ordering = ('email',)


class SubscriberAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_joined'  # updated
    search_fields = ['full_name', 'email', 'country']
    list_display = ['full_name', 'email', 'country', 'date_joined']
    list_filter = ['country', 'date_joined']
    readonly_fields = ['date_joined']

    class Meta:
        model = Subscriber


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'message_date'  # updated
    search_fields = ['name', 'email', 'subject']
    list_display = ['name', 'email', 'subject', 'message_date']
    list_filter = ['message_date']
    readonly_fields = ['message_date']

    class Meta:
        model = Contact


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['Allow_bikers_join', 'gps_acc','user']
    list_filter = ['Allow_bikers_join']

    class Meta:
        model = Setting


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Setting, SettingsAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Contact, ContactAdmin)
