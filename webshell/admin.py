from django.contrib import admin
from .forms import ScriptForm
from .models import Script


class ScriptAdmin(admin.ModelAdmin):
    form = ScriptForm
    change_form_template = 'webshell/change_form.html'

admin.site.register(Script, ScriptAdmin)