from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Sheetmusic(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    composer_firstname = models.CharField(max_length=254)
    composer_lastname = models.CharField(max_length=254)
    arranger = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.name

    def pdf_file_name(self):
        return os.path.basename(self.pdf_file)
