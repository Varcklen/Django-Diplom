from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Service, Portfolio, History, Staff, Partner, Contact

# Register your models here.
class ImageMixin():
    image_width = 50

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='{self.image_width}px'>")

class BaseAdminVision(admin.ModelAdmin):
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

    list_filter = ('is_visible',)
    search_fields = ('name',)

#Admin Classes
@admin.register(Service)
class ServiceAdmin(BaseAdminVision):
    list_display = ('id', 'name', 'image_link', 'description', 'is_visible', 'sort')
    list_editable = ('image_link', 'description', 'is_visible', 'sort')
    
    
@admin.register(Portfolio)
class PortfolioAdmin(BaseAdminVision, ImageMixin):
    list_display = ('id', 'name', 'image_tag', 'client', 'category', 'small_desc', 'description', 'is_visible', 'sort')
    list_editable = ( 'small_desc', 'description', 'client', 'category', 'is_visible', 'sort')

@admin.register(History)
class HistoryAdmin(BaseAdminVision, ImageMixin):
    list_display = ('id', 'name', 'image_tag', 'date', 'description', 'is_visible', 'sort')
    list_editable = ('description', 'date', 'is_visible', 'sort')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin, ImageMixin):
    list_display = ('id', 'first_name', 'last_name', 'image_tag', 'role', 'twitter_link', 'facebook_link', 'linkedin_link', 'is_visible', 'sort')
    list_editable = ('role', 'twitter_link', 'facebook_link', 'linkedin_link', 'is_visible', 'sort')
    list_display_links = ('id', 'first_name', 'last_name')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    
    list_filter = ('is_visible',)
    search_fields = ('first_name', 'last_name',)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin, ImageMixin):
    list_display = ('id', 'image_tag', 'link', 'is_visible', 'sort')
    list_editable = ('link', 'is_visible', 'sort')
    list_filter = ('is_visible',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin, ImageMixin):
    list_display = ('id', 'twitter_link', 'facebook_link', 'linkedin_link')
    list_editable = ('twitter_link', 'facebook_link', 'linkedin_link')