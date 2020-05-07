from django.db import models
from django.urls import reverse 
# Create your models her
class Catalog(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'catalog'
		verbose_name_plural = 'catalogs'

	def __str__(self):
		return self.name

class Category(models.Model):
	catalog = models.ForeignKey(Catalog, related_name='catalogs', on_delete=models.CASCADE, default=None)
	image = models.ImageField(upload_to='products/Category/', blank=True)	
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product:product_list_by_category', args=[self.slug])

class Product(models.Model):

	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	available = models.BooleanField(default=True)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	front_view = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) 
	back_view = models.ImageField(upload_to='products/%Y/%m/%d', blank=True )
	right_view = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	left_view = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	qty = models.PositiveIntegerField(default=0)
	sold = models.PositiveIntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)
	discount_rate = models.DecimalField(default=0, decimal_places=0, max_digits=10)
	final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product:product_detail', args=[self.id, self.slug])


