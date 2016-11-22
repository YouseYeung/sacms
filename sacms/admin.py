from django.contrib import admin
from .models import Article, ResearchGroup

# Register Article class in admin site
admin.site.register(Article)
# Register ResearchGroup class in admin site
admin.site.register(ResearchGroup)
