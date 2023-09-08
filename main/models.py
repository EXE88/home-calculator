from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class ProjectInputs(models.Model):

    build_quality_choices = (
    (0, 'استاندارد'),
    (1, 'خوب'),
    (2, 'عالی'),
    )
    city_choices = (
        # انتخاب‌های مرتبط با شهرها...
    )
    lobby_choices = (
        (True, 'دارد'),
        (False, 'ندارد'),
    )
    type_of_structure_choices = (
        (0, 'بتنی'),
        (1, 'فولادی'),
    )
    roof_type_choices = (
        (0, 'تیرچه بتنی'),
        (1, 'تیرچه فولادی'),
    )
    created = models.DateTimeField(auto_now=True,null=False,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30,null=False,blank=False)
    build_quality = models.PositiveSmallIntegerField(choices=build_quality_choices,null=False,blank=False)
    city = models.PositiveSmallIntegerField(null=False,blank=False)
    area = models.PositiveSmallIntegerField(null=False,blank=False)
    width = models.PositiveSmallIntegerField(null=False,blank=False)
    length = models.PositiveSmallIntegerField(null=False,blank=False)
    floor = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(14)],null=False,blank=False)
    underground_floor = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],null=False,blank=False)
    lobby = models.BooleanField(choices=lobby_choices,null=False,blank=False)
    type_of_structure = models.PositiveSmallIntegerField(choices=type_of_structure_choices,null=False,blank=False)
    roof_type = models.PositiveSmallIntegerField(choices=roof_type_choices,null=False,blank=False)
    