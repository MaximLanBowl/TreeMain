from django.db import models


class MenuItem(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
