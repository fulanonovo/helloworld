from django.db import models

# Create your models here.
class Livro(models.Model):
	nome = CharField(max_length=200)