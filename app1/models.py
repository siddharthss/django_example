from django.db import models


class Project(models.Model):
    """
    Manage project
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512, blank=True, null=True)

    def __unicode__(self):
        return '%s: %s' % (self.id, self.name)
