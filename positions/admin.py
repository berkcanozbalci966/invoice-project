from django.contrib import admin
from .models import Position

from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

# Register your models here.

class PositionResource(resources.ModelResource):
    invoice = Field()
    description = Field()
    class Meta:
        model = Position
        field = ('id','invoice','title','description','amount','created')

    def dehydrate_invoice(self,object):
        return object.invoice.number

    def dehydrate_description(self,object):
        if(object.description == ''):
            return '-'
        return object.description


class PositionAdmin(ExportActionMixin,admin.ModelAdmin):
    resource_class = PositionResource



admin.site.register(Position,PositionAdmin)
