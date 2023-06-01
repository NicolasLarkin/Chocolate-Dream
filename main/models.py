from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    date_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='category')
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.title}'
    
    

    #Product.objects.filter(category =2)
    


