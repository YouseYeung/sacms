from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# News article
class Article(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def edit(self, title=None, author=None, text=None, published_date=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if published_date is not None:
            self.published_date = published_date
        self.save()

    def __str__(self):
        return self.title

class ResearchGroup(models.Model):
    # Research Group name
    name = models.CharField(max_length=1000)
    # Research Group leader, must be a staff of the site
    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        # only staff can be leader of a ResearchGroup
        limit_choices_to={'is_staff': True},
        related_name = '+',
    )
    # Research Group personnel
    personnel = models.ManyToManyField(
        User,
        # TODO: Only users in group LabUser can be in here
        limit_choices_to={'groups__name': 'LabUser'},
        # validation-related, will accept empty value
        blank=True,
        related_name = '+',
    )
    # Research Directions
    directions = models.CharField(max_length=1000)
    # Researching Projects
    projects = models.CharField(max_length=1000)
    # Published Papers
    papers = models.TextField()

    def __str__(self):
        return self.name
