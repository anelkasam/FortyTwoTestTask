from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    birthday = models.DateField()
    bio = models.TextField(max_length=300)
    contacts = models.TextField(max_length=300)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.id = 1
        super(Contacts, self).save()
