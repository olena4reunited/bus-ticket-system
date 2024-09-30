from django.db import models


class Bus(models.Model):
    info = models.CharField(max_length=255, null=True)
    num_seats = models.IntegerField()

    class Meta:
        verbose_name = 'buses'

    @property
    def is_small(self):
        return self.num_seats <= 20

    def __str__(self):
        return f"Bus {self.info} (id= {self.id})"
