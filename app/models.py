import uuid
from django.db import models
from django.utils.html import format_html


# Base model class that provides common fields and functionalities for other models to inherit from
class BaseModel(models.Model):
    # Unique identifier for each instance of the model
    id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, primary_key=True)

    # DateTimeField that automatically stores the creation time of an instance when it is first saved to the database
    created_at = models.DateTimeField(auto_now_add=True)

    # DateTimeField that automatically updates with the current time whenever the instance is saved or updated in the
    # database
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Specifies that this model is abstract, meaning it won't be created as a separate table in the database
        abstract = True


# Create your models here.
class Contact(BaseModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=150, unique=True)
    message = models.TextField()

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact"
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class News(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="image", null=True, blank=True)

    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def picture(self):
        if self.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(
                    self.image.url
                )
            )
        return "no_image"

    class Meta:
        db_table = "news"
        verbose_name = "News"
        verbose_name_plural = "News"


#
class Tarif(models.Model):
    tarif_name = models.CharField(max_length=200)
    final_field_1 = models.CharField(max_length=200)
    final_field_2 = models.CharField(max_length=200)
    final_field_3 = models.CharField(max_length=200)
    final_field_4 = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tarif_name


class TarifProduct(models.Model):
    tarif_id = models.ForeignKey(Tarif, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)

    class TurnoverChoices(models.IntegerChoices):
        INCLUDE = 1, "Включено"
        NOT_INCLUDED = 2, "Не включено"

    field_1 = models.IntegerField(choices=TurnoverChoices.choices)
    field_2 = models.IntegerField(choices=TurnoverChoices.choices)
    field_3 = models.IntegerField(choices=TurnoverChoices.choices)
    field_4 = models.IntegerField(choices=TurnoverChoices.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "serviceTariff"
        verbose_name = "ServiceTariff"
        verbose_name_plural = "ServiceTariffs"
