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
SIZE = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)
class Twig(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  size = models.CharField(max_length=1,choices=SIZE,default=SIZE[1][0])

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('twig_details', kwargs={'pk': self.id})


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