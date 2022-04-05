from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.urls import reverse


# Create your models here.



class Car(models.Model):
    #relation
    categories = models.ForeignKey('CarCategory',on_delete=models.CASCADE,blank=True,null=True,related_name='car_categories')
    category = models.ForeignKey('ConditionCategory',on_delete=models.CASCADE,blank=True,null=True,related_name='condition_categories')
    
    name = models.CharField(max_length=200,blank=True,null=True)
    price = models.CharField(max_length=200,blank=True,null=True)
    mileage = models.CharField(max_length=200,blank=True,null=True)
    car_image = models.ImageField(upload_to='media')
    condition = models.CharField(max_length=200,blank=True,null=True)
    brend = models.CharField(max_length=100)
    dealer_comments = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, verbose_name='Slug', unique=True, blank=True, null=True)
    kilometres = models.CharField(max_length=60)
    colour = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    drive_type = models.CharField(max_length=100)
    
    in_depth_specifications1 = RichTextUploadingField()
    in_depth_specifications2 = RichTextUploadingField()
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("core:offers_detail", kwargs={
            "slug": self.slug
        })

    
    class Meta:
        verbose_name_plural = 'Cars'
                
        
    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.car_image.url))
    
    
class ConditionCategory(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(unique=True)
    
    
    
    def __str__(self):
        return self.name
 
    def get_absolute_url(self):
        return reverse('core:offer_category', args=[self.slug,])
    
    
    class Meta:
        verbose_name_plural = 'ConditionCategories'    


    
class CarCategory(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(unique=True)
    image=models.ImageField(upload_to='media')
    
    
     


    def get_absolute_url(self):
        return reverse('core:car_category', args=[self.slug,])
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'CarCategories'
    




    



class Address(models.Model):
    address = models.CharField(max_length=200,blank=True,null=True)
    phone_number = models.CharField(max_length=200,default='(123) 456-7890')
    working_hours = RichTextUploadingField()
    call_us = models.CharField(max_length=200,default='+1 (289) 788-9196')
     
    
    
    def __str__(self):
        return self.address
    

class About(models.Model):
    content = RichTextUploadingField()
    
    
class Image(models.Model):
    cars_image = models.ForeignKey(Car,on_delete=models.CASCADE,blank=True,null=True,related_name='cars_image')
    image = models.ImageField(upload_to='images')
    

    def image_tag(self):
        return mark_safe('<img src="{}" height="100" width="100"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    
    
