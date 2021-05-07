from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Subdivision(MPTTModel):
    # вся структура подразделениq хранится здесь
    # у создаваемого элемента есть родитель из этой же модели (либо None)
    subdivision_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children_subdivision')
    def __str__(self):
        return 'Podrazdelenie: ' + self.subdivision_name

    class MPTTMeta:
        order_insertion_by = ['subdivision_name']


class Position(models.Model):
    # должности
    # здесь нет иерархии, это просто перечень возможных должностей для того или иного подразделения
    # создавая должность мы ей выбираем в качестве родителя подразделение из модели Subdivision
    employment_position = models.CharField(max_length=200)
    salary = models.IntegerField()
    parent = models.ForeignKey(Subdivision, on_delete=models.CASCADE, related_name='children_position')

    def __str__(self):
        return 'Dolzhnost: ' + self.employment_position


class Persone(models.Model):
    # здесь нет иерархии, тут указываются личные данные человека
    # а в качестве родителя указывается конкретная должность из модели Position
    name = models.CharField(max_length=50)
    tax_id_inn = models.CharField(max_length=12, unique=True)
    # employment_position = models.CharField(max_length=200)
    employment_start_date = models.DateTimeField(auto_now_add=False)
    # date_added = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True, related_name='children_persone')

    def __str__(self):
        return str(self.id) + ' Name: ' + self.name
