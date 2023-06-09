from django.db import models

class Link(models.Model):
    nome = models.CharField(max_length = 255)
    url = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.nome} = {self.url}'