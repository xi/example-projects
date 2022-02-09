import datetime

import requests
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .helpers import update_paper


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
    paper_identifier = models.CharField(
        _('Identifier'),
        help_text=_(
            'Identifier to a corresponding publication supported by Semantic '
            'Scholar (https://www.semanticscholar.org), e.g. DOI or ArXiv ID'
        ),
        max_length=32,
        blank=True,
    )
    paper_title = models.CharField(_('Paper'), max_length=64, blank=True)
    paper_url = models.URLField(_('Paper URL'), blank=True)
    paper_citations = models.IntegerField(_('Citations'), default=0)
    paper_timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_paper(self):
        if self.paper_identifier:
            delta = datetime.timedelta(days=7)
            if (
                not self.paper_timestamp
                or self.paper_timestamp < timezone.now() - delta
            ):
                try:
                    update_paper(self, self.paper_identifier)
                    self.save()
                except requests.RequestException:
                    pass

        return {
            'title': self.paper_title,
            'url': self.paper_url,
            'citations': self.paper_citations,
        }
