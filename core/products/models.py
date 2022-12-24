from django.db import models



class Categorie(models.Model):
    name = models.CharField('Nombre',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Gender(models.Model):
    name = models.CharField('Nombre',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Genders'
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'



class Product(models.Model):
    name = models.CharField('Nombre', max_length=100)
    description = models.TextField('Descripción')
    price = models.FloatField('Precio', default=0)
    image = models.ImageField('Imagen', blank=True, upload_to='products',null=True)
    stock = models.IntegerField('Stock', default=0)
    categories = models.ManyToManyField(Categorie, blank=True,related_name='Categorias')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    created = models.DateTimeField('Creado', auto_now_add=True)
    updated = models.DateTimeField('Modificado', auto_now=True)

    def __str__(self):
        return f'{self.name} ${self.price} -> stock :{self.stock} '

    class Meta:
        db_table = 'Product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'