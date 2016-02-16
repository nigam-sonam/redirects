from django.contrib import admin
from .models import Redirects
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('redirect_from','redirect_to','url_status')

admin.site.register(Redirects,RegisterAdmin)
