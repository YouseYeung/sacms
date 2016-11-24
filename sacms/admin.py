from django.contrib import admin
from .models import Article, ResearchGroup, Meeting

# Register Article class in admin site
admin.site.register(Article)
# Register ResearchGroup class in admin site
admin.site.register(ResearchGroup)

# Register Meeting class in admin site
admin.site.register(Meeting)