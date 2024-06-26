from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class PlantCategory(models.Model):
    name = models.CharField(
        max_length=100, help_text=_("Enter the name of the plant category.")
    )
    description = models.TextField(
        help_text=_("Provide a description for the plant category."),
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="plant_categories/",
        help_text=_("Upload an image for the plant category."),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Plant Category"
        verbose_name_plural = "Plant Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PlantFeatures(models.Model):
    name = models.CharField(
        max_length=50, help_text=_("Enter the name of the plant features.")
    )

    class Meta:
        verbose_name = "Plant Feature"
        verbose_name_plural = "Plant Features"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Plant(models.Model):
    class IndoorOutdoorChoices(models.TextChoices):
        INDOOR = "Indoor", _("Indoor")
        OUTDOOR = "Outdoor", _("Outdoor")

    class SizeChoices(models.TextChoices):
        SMALL = "Small", _("Small")
        MEDIUM = "Medium", _("Medium")
        LARGE = "Large", _("Large")
        EXTRA_LARGE = "Extra Large", _("Extra Large")

    title = models.CharField(
        max_length=100, help_text=_("Enter the name of the plant.")
    )

    category = models.ForeignKey(
        PlantCategory,
        on_delete=models.CASCADE,
        help_text=_("Select the category for the plant."),
    )
    indoor_or_outdoor = models.CharField(
        max_length=10,
        choices=IndoorOutdoorChoices.choices,
        help_text=_("Select whether the plant is meant for indoor or outdoor use."),
    )
    size = models.CharField(
        max_length=20,
        choices=SizeChoices.choices,
        help_text=_("Select the size of the plant."),
    )
    description = models.TextField(help_text=_("Provide a description for the plant."))
    care_instructions = models.TextField(
        help_text=_("Provide care instructions for the plant.")
    )
    features = models.ManyToManyField(
        PlantFeatures,
        help_text=_("Select the features that describe the plant."),
        blank=True,
    )
    tags = TaggableManager(help_text=_("Add tags that describe the plant."), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

    def __str__(self):
        return self.title


class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="plant_images/", help_text=_("Upload an image for the plant.")
    )
    short_description = models.CharField(
        max_length=255,
        help_text=_("Enter a short description for the image."),
        blank=True,
        null=True,
    )


class PlanterCategory(models.Model):
    name = models.CharField(
        max_length=100, help_text=_("Enter the name of the planter category.")
    )
    description = models.TextField(
        help_text=_("Provide a description for the planter category.")
    )
    image = models.ImageField(
        upload_to="planter_categories/",
        help_text=_("Upload an image for the planter category."),
    )

    class Meta:
        verbose_name = "Planter Category"
        verbose_name_plural = "Planter Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PlanterFeatures(models.Model):
    name = models.CharField(
        max_length=50, help_text=_("Enter the name of the planter features.")
    )

    class Meta:
        verbose_name = "Planter Feature"
        verbose_name_plural = "Planter Features"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Planter(models.Model):
    model = models.CharField(
        max_length=100, help_text=_("Enter the model of the planter.")
    )
    size = models.CharField(
        max_length=20, help_text=_("Enter the size of the planter.")
    )
    description = models.TextField(
        help_text=_("Provide a description for the planter.")
    )
    short_description = models.CharField(
        max_length=255,
        help_text=_("Enter a short description for the plant."),
        blank=True,
        null=True,
    )
    features = models.ManyToManyField(
        PlanterFeatures,
        help_text=_("Select the features that describe the planter."),
        blank=True,
    )
    color = models.CharField(
        max_length=50, help_text=_("Enter the color of the planter.")
    )
    category = models.ForeignKey(
        PlanterCategory,
        on_delete=models.CASCADE,
        help_text=_("Select the category for the planter."),
    )
    is_custom = models.BooleanField(
        default=False, help_text=_("Check if the planter is custom-made.")
    )
    tags = TaggableManager(
        help_text=_("Add tags that describe the planter."), blank=True
    )

    class Meta:
        verbose_name = "Planter"
        verbose_name_plural = "Planters"
        ordering = ["model"]

    def __str__(self):
        return self.model


class PlanterImage(models.Model):
    planter = models.ForeignKey(Planter, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="planter_images/", help_text=_("Upload an image for the planter.")
    )
    short_description = models.CharField(
        max_length=255,
        help_text=_("Enter a short description for the image."),
        blank=True,
        null=True,
    )


class ServiceCategory(models.Model):

    class TypeChoices(models.TextChoices):
        COMMERCIAL = "Commercial", _("Commercial")
        RESIDENTIAL = "Residential", _("Residential")

    no = models.PositiveIntegerField(
        unique=True, help_text=_("Enter the number of the service category.")
    )

    type = models.CharField(
        default=TypeChoices.RESIDENTIAL,
        null=True,
        blank=True,
        max_length=20,
        choices=TypeChoices.choices,
        help_text=_("Select the type of service."),
    )

    title = models.CharField(
        max_length=100, help_text=_("Enter the title of the service category.")
    )

    description = models.TextField(
        help_text=_("Provide a description for the service category."),
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to="service_categories/",
        help_text=_("Upload an image for the service category."),
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ["title", "type"]
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
        ordering = ["no"]

    def __str__(self):
        return f"{self.type}-{self.title}"


class Service(models.Model):

    title = models.CharField(
        max_length=100, help_text=_("Enter the title of the service.")
    )

    description = models.TextField(
        help_text=_("Provide a description for the service."),
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to="services/",
        help_text=_("Upload an image for the service."),
        null=True,
        blank=True,
    )

    budget_range = models.CharField(
        max_length=50,
        help_text=_("Enter the budget range for the service."),
        null=True,
        blank=True,
    )

    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        help_text=_("Select the category for the service."),
    )

    tags = TaggableManager()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Ideas(models.Model):
    title = models.CharField(
        max_length=100, help_text=_("Enter the title of the idea.")
    )
    description = models.TextField(help_text=_("Provide a description for the idea."))
    image = models.ImageField(
        upload_to="ideas/",
        help_text=_("Upload an image for the idea."),
        null=True,
        blank=True,
    )
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Idea"
        verbose_name_plural = "Ideas"
        ordering = ["title"]

    def __str__(self):
        return self.title
