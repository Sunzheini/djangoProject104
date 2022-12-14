from django.db import models


class Employees(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        max_length=20,
    )

    age = models.IntegerField()

    years_of_experience = models.PositiveIntegerField()

    review = models.TextField()

    start_date = models.DateTimeField()

    email = models.EmailField()

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'If: {self.pk}; Name: {self.fullname}'




