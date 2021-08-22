from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    telephone_number = models.CharField(max_length=100, null=True)
    max_people = models.SmallIntegerField(default=0)
    actual_people = models.SmallIntegerField(default=0)
    address = models.CharField(max_length=100, null=True)

    @property
    def is_full(self):
        return self.actual_people >= self.max_people

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return self.name


class Action(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self, action):
        return (f"{action} at: {self.datetime} in {self.store.name}'s store")


class Entry(Action):
    
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return super().__str__('Entry')


class Exit(Action):

    class Meta:
        verbose_name = 'Exit'
        verbose_name_plural = 'Exits'

    def __str__(self):
        return super().__str__('Exit')


