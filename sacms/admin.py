from django.contrib import admin
from .models import Article, ResearchGroup, Meeting

# Admin class for Article
class ArticleAdmin(admin.ModelAdmin):
    pass

# Admin class for ResearchGroup
class ResearchGroupAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(ResearchGroupAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # only list those groups whose leader is the current user
        return qs.filter(leader=request.user)

# Register Article class in admin site
admin.site.register(Article, ArticleAdmin)
# Register ResearchGroup class in admin site
<<<<<<< HEAD
admin.site.register(ResearchGroup)

# Register Meeting class in admin site
admin.site.register(Meeting)
=======
admin.site.register(ResearchGroup, ResearchGroupAdmin)
>>>>>>> c14fb47d645e8bade2df180f51efcb9d8c2f8731
