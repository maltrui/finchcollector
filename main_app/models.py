from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
ENJOYMENT = (
    ('Y', 'They enjoyed the meal'),
    ('N', 'They did not enjoy the meal')
)

class Finch(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Food(models.Model):
    date = models.DateField('meal date')
    meal = models.CharField(max_length=1,choices=MEALS, default=MEALS[0][0])
    enjoyedMeal = models.CharField(max_length=1,choices=ENJOYMENT,default=ENJOYMENT[1][0])
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date} and {self.get_enjoyedMeal_display()}"