from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30)
    craeted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class product(models.Model):
    mainimage = models.ImageField(upload_to="product")  # All product realated fields will be stored in this area
    name = models.CharField(max_length=265)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    preview_text = models.TextField(max_length=300, verbose_name="Preview_text")
    details_text = models.TextField(max_length=1000, verbose_name="Description")
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

    class Meta:
        ordering = [
            "created"
        ]  # product will get the data from the data base last will be the frst
