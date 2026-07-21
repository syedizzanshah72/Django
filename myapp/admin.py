from django.contrib import admin
from myapp.models import ChaiVariety ,Chai_Review,Store,Chai_Certificate
# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = Chai_Review
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varietes',)

class Chai_CertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number')
    list_display_links = ('chai',)

admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Chai_Certificate,Chai_CertificateAdmin)
