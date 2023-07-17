
from django.contrib import admin
from core.models import mainpost
# Register your models here.
class mainpostAdmin(admin.ModelAdmin):
    list_display=('title','publishdate','btnlink')

admin.site.register(mainpost,mainpostAdmin)    