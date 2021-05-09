from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Subdivision(MPTTModel):
    # вся структура подразделений хранится здесь
    # у создаваемого элемента есть родитель из этой же модели (либо None)
    subdivision_name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children_sub')
    def __str__(self):
        return f'Podrazdelenie: {self.subdivision_name}'

    #def all_positions_to_string(self):
        #return ", ".join([Position.employment_position for employment_position in self.children_position.all()])

    class MPTTMeta:
        order_insertion_by = ['subdivision_name']


class Position(models.Model):
    # должности
    # здесь нет иерархии, это просто перечень возможных должностей
    employment_position = models.CharField(max_length=200, null=True, blank=True)
    salary = models.IntegerField()

    def __str__(self):
        return f'Dolzhnost: {self.employment_position}'


class Persone(models.Model):
    # здесь нет иерархии, тут указываются личные данные человека
    # а в качестве внешних ключей указывается конкретная должность из модели Position
    # и конкретное подразделение
    name = models.CharField(max_length=50, null=True, blank=True)
    tax_id_inn = models.CharField(max_length=12, unique=True)
    employment_start_date = models.DateTimeField(auto_now_add=False)
    employee_position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children_position')
    employee_subdivision = TreeForeignKey(Subdivision, on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children_subdivision')

    def __str__(self):
        return str(self.id) + ' Name: ' + self.name
