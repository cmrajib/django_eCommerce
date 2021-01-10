from django.db import models

from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
from accounts.models import User


class Product(models.Model):

    CONDITION_TYPE = (
        ("New" , "New") ,
        ("Used" , "Used")
    )

    ## contain all the products informations
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100 , choices=CONDITION_TYPE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL , null=True,
                                 related_name='product_category')
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL , null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image1 = models.ImageField(upload_to='main_product/')
    image2 = models.ImageField(upload_to='main_product/', blank=True, null=True)
    image3 = models.ImageField(upload_to='main_product/', blank=True, null=True)
    image4 = models.ImageField(upload_to='main_product/', blank=True, null=True)
    image5 = models.ImageField(upload_to='main_product/', blank=True, null=True)
    image6 = models.ImageField(upload_to='main_product/', blank=True, null=True)
    image7 = models.ImageField(upload_to='main_product/', blank=True, null=True)
    image8 = models.ImageField(upload_to='main_product/', blank=True, null=True)
    image9 = models.ImageField(upload_to='main_product/', blank=True, null=True)
    image10 = models.ImageField(upload_to='main_product/', blank=True, null=True)


    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True  , null=True)


    # def save(self , *args , **kwargs):
    #     if not self.slug and self.name :
    #         self.slug = slugify(self.name)
    #     super(Product , self).save(*args , **kwargs)


    def __str__(self):
        return self.name



# class ProductImages(models.Model):
#     product = models.ForeignKey(Product , on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='products/' , blank=True , null=True)
#
#     def __str__(self):
#         return self.product.name
#
#     class Meta:
#         verbose_name = 'Product Image'
#         verbose_name_plural = 'Product Images'




class Category(models.Model):
    ## for product category
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/' , blank=True , null=True)

    slug = models.SlugField(blank=True  , null=True)


# product_category is the relation name defined in the product table
    def product_count(self):
        return self.product_category.all().count()


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name



class Brand(models.Model):
    ## for product brand
    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name
