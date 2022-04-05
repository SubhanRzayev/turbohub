from django.contrib import admin

from core.models import Address,About,Car, ConditionCategory,Image,CarCategory
# Register your models here.



class CarsImageInline(admin.TabularInline):
    model = Image
    extra = 10

@admin.register(Car)
class OffersAdmin(admin.ModelAdmin):
    list_display = ['name','price','mileage','condition','brend','kilometres','colour','transmission','category','categories','image_tag',]
    readonly_fields = ('image_tag',)
    inlines = [CarsImageInline]
    
    
    
@admin.register(Address)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['address','phone_number','working_hours',]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['content',]
    
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['cars_image','image_tag',]
    readonly_fields = ('image_tag',)
    
@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]    


@admin.register(ConditionCategory)
class ConditionCategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    

    
    









