from django.db import models
from django.utils import timezone

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
