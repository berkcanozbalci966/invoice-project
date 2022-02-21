from turtle import position
from django.contrib import admin
from .models import Invoice,Tag
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

# Register your models here.

class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields = ('id','name')


class TagAdmin(ExportActionMixin,admin.ModelAdmin):
    resource_class = TagResource

class InvoiceResource(resources.ModelResource):
    profile = Field()
    receiver = Field()
    created = Field()
    closed = Field()
    positions = Field()
    total_amount = Field()
    class Meta:
        model = Invoice
        fields = ('id','profile','receiver','number','completion_date','issue_date','payment_date','created','closed','positions','total_amount')

    def dehydrate_profile(self,object):
        return object.profile.user.username

    def dehydrate_receiver(self,object):
        return object.receiver.name
    def dehydrate_created(self,object):
        # date only
        return object.created.strftime("%d-%m-%y")

    def dehydrate_closed(self,object):
        return str(object.closed)
    
    def dehydrate_positions(self,object):
        positions_list = [position.title for position in object.positions]
        positions_string = ", ".join(positions_list)
        return positions_string

    def dehydrate_total_amount(self,object):
        return object.total_amount



class InvoiceAdmin(ExportActionMixin,admin.ModelAdmin):
    resource_class = InvoiceResource

admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Tag,TagAdmin)
