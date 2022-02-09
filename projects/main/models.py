from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    title = models.CharField(_('Title'), max_length=32)

    def __str__(self):
        return self.title


class DataType(models.Model):
    title = models.CharField(_('Title'), max_length=32)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(_('Title'), max_length=64)
    responsible_researcher = models.CharField(
        _('Responsible researcher'), max_length=32
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, verbose_name='Department'
    )
    data_type = models.ManyToManyField(DataType, verbose_name=_('Data type'))
    identifier = models.CharField(
        _('Identifier'),
        help_text=_(
            'Identifier to a corresponding publication supported by Semantic '
            'Scholar (https://www.semanticscholar.org), e.g. DOI or ArXiv ID'
        ),
        max_length=32,
        blank=True,
    )

    def __str__(self):
        return self.title
