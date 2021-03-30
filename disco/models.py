from django.db import models

# Create your models here.
from django.utils.timezone import now


class SoftDeleteMixin(models.Model):
    deleted = models.DateTimeField(blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.deleted = now()
        self.save(update_fields=['deleted'])

    class Meta:
        abstract = True