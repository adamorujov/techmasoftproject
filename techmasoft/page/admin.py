from django.contrib import admin
from page.models import (
    PageModel, ServiceModel, 
    PropertyModel, WorkModel, 
    SuggestionModel, PurposeModel, 
    TeamModel, CompanyModel,
    SkillModel, AccountModel,
    PageAccountsModel,
    )
from django.contrib.admin.sites import AdminSite

AdminSite.site_header = 'Techmasoft administrasiyası'
AdminSite.site_title = 'Techmasoft sayt administratoru'

class PageAccountInline(admin.TabularInline):
    model = PageAccountsModel
    extra = 1

@admin.register(PageModel)
class PageAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Səhifənin əsas elementləri', {
                'fields' : ('title', 'logo', 'favicon', 'slogan')
            }
        ),
        (
            'Banner elementləri', {
                'fields' : ('banner_title', 'banner_description', 'banner_image')
            },
        ),
        (
            'Digər məlumatlar', {
                'fields' : ('suggestion_description', 'companies_description', 'contact_image')
            },
        ),
        (
            'Əlaqə vasitələri', {
                'fields' : ('admin_phone_number', 'admin_whatsapp_number', 'corporative_email')
            }
        ),
    )
    inlines = [
        PageAccountInline,
    ]

class SkillInline(admin.TabularInline):
    model = SkillModel
    extra = 1

class AccountInline(admin.TabularInline):
    model = AccountModel
    extra = 1

@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
        AccountInline
    ]

admin.site.register(ServiceModel)
admin.site.register(PropertyModel)
admin.site.register(WorkModel)
admin.site.register(SuggestionModel)
admin.site.register(PurposeModel)
admin.site.register(CompanyModel)

def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

    for app in app_list:
        if app['app_label'] == 'page':
            ordering = {
                "Əsas səhifə": 1,
                "Xidmətlərimiz": 2,
                "Sayt Xüsusiyyətləri": 3,
                "İşlərimiz": 4,
                "Təkliflərimiz": 5,
                "Məqsədlərimiz": 6,
                "Komandamız": 7,
                "Bizimlə işləyən şirkətlər": 8
            }
            app['models'].sort(key=lambda x: ordering[x['name']])

        if app['app_label'] == 'auth':
            ordering = {
                "Istifadəçilər" : 1,
                "Qruplar" : 2,
            }
            app['models'].sort(key=lambda x: ordering[x['name']])

    return app_list

admin.AdminSite.get_app_list = get_app_list

