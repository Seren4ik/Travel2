from django.core.exceptions import ValidationError
from django.db import models

from Cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название маршрута")
    travel_times = models.PositiveSmallIntegerField(verbose_name="Общее время в пути")
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="route_from_city_set",
                                  verbose_name="Из какого города")
    to_city = models.ForeignKey("Cities.City", on_delete=models.CASCADE, related_name="route_to_city_set",
                                  verbose_name="В какой города")

    trains = models.ManyToManyField('trains.Train', verbose_name="Поезда")

    def __str__(self):
        return f'Маршрут: {self.name} из города {self.from_city} в город {self.to_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = "Маршруты"
        ordering = ["travel_times"]

    # def clean(self):
    #     if self.from_city == self.to_city:
    #         raise ValidationError("Измените город прибытия")
    #     qs = Train.objects.filter(from_city = self.from_city, to_city=self.to_city,
    #                               travel_time=self.travel_time).exclude(pk=self.pk)
    #
    #     if qs.exists():
    #         raise ValidationError("Измените время")
    #
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)

