from django.db import models
from django.shortcuts import redirect

class PageModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='Səhifə başlığı')
    logo = models.ImageField(upload_to='images/', verbose_name='Loqo', blank=True, null=True)
    page_keywords = models.TextField(blank=True, null=True, verbose_name="Açar sözlər")
    page_description = models.TextField(blank=True, null=True, verbose_name="Təsvir")
    favicon = models.ImageField(upload_to='images/', verbose_name='İkon', blank=True, null=True)
    slogan = models.CharField(max_length=250, verbose_name='Sloqan', blank=True, null=True)
    banner_title = models.CharField(max_length=250, verbose_name='Banner başlığı')
    banner_description = models.TextField(verbose_name='Banner mətni')
    suggestion_description = models.TextField(verbose_name='Təklif bölməsi izahı', blank=True, null=True)
    companies_description = models.TextField(verbose_name='Şirkətlər bölməsi izahı', blank=True, null=True)
    admin_phone_number = models.CharField(max_length=25, blank=True, null=True, verbose_name='Telefon nömrəsi')
    admin_whatsapp_number = models.CharField(max_length=25, blank=True, null=True, verbose_name='Whatsapp nömrəsi')
    corporative_email = models.EmailField(max_length=100, verbose_name='Korporativ email', blank=True, null=True)

    class Meta:
        verbose_name = 'Səhifə'
        verbose_name_plural = 'Əsas səhifə'
        

    def __str__(self):
        return "Səhifə"

    def save(self, *args, **kwargs):
        if not self.pk and PageModel.objects.exists():
            return redirect('homepage')
        return super().save(*args, **kwargs)

class PageView(models.Model):
    view_day = models.DateField(auto_now_add=True, verbose_name="Baxış tarixi")
    view_month = models.IntegerField(default=0, verbose_name="Baxış ayı")
    view_year = models.IntegerField(default=0, verbose_name="Baxış ili")

    class Meta:
        verbose_name = "Baxış"
        verbose_name_plural = "Baxışlar"

    def __str__(self):
        return self.id

class PageAccountsModel(models.Model):
    social_media = models.CharField(max_length=50, verbose_name='Sosial media')
    account_link = models.URLField(max_length=250, verbose_name='Hesab linkləri')
    page = models.ForeignKey(PageModel, on_delete=models.CASCADE, verbose_name='Səhifə', related_name='page_accounts')

    class Meta:
        verbose_name = 'Hesab'
        verbose_name_plural = 'Sosial media hesabları'

    def __str__(self):
        return self.social_media



class ServiceModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='Ad')
    content = models.TextField(verbose_name='Məzmun')
    image = models.ImageField(upload_to='images/', verbose_name='Şəkil')

    class Meta:
        verbose_name = 'Xidmət'
        verbose_name_plural = 'Xidmətlərimiz'

    def __str__(self):
        return self.title

class PropertyModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='Ad')
    content = models.TextField(verbose_name='Məzmun')

    class Meta:
        verbose_name = 'Xüsusiyyət'
        verbose_name_plural = 'Sayt Xüsusiyyətləri'

    def __str__(self):
        return self.title

class WorkModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='Ad')
    content = models.TextField(verbose_name='Məzmun')
    image = models.ImageField(upload_to='images/', verbose_name='Şəkil')
    site_url = models.URLField()

    class Meta:
        verbose_name = 'İş'
        verbose_name_plural = 'İşlərimiz'

    def __str__(self):
        return self.title

class SuggestionModel(models.Model):
    DIRECTIONS = (
        ('L', 'Sol'),
        ('R', 'Sağ'),
    )
    title = models.CharField(max_length=250, verbose_name='Ad')
    content = models.TextField(verbose_name='Məzmun')
    image = models.ImageField(upload_to='images/', verbose_name='Şəkil')
    suggestion_direction = models.CharField(max_length=1, choices=DIRECTIONS, default='L', verbose_name='İstiqamət')

    class Meta:
        verbose_name = 'Təklif'
        verbose_name_plural = 'Təkliflərimiz'

    def __str__(self):
        return self.title

class PurposeModel(models.Model):
    title = models.CharField(max_length=250, verbose_name='Ad')
    content = models.TextField(verbose_name='Məzmun')
    image = models.ImageField(upload_to='images/', verbose_name='Şəkil')

    class Meta:
        verbose_name = 'Məqsəd'
        verbose_name_plural = 'Məqsədlərimiz'

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ad')
    last_name = models.CharField(max_length=50, verbose_name='Soyad')
    email = models.EmailField(max_length=100, verbose_name='Email')
    country_code = models.CharField(max_length=8, default='+994', verbose_name='Ölkə kodu')
    telephone_number = models.CharField(max_length=15, verbose_name='Telefon nömrəsi')
    message = models.TextField(verbose_name='Mesaj')
    message_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Göndərilmə tarixi')
    is_new = models.BooleanField(verbose_name='Yeni', default=True)

    class Meta:
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'

    def __str__(self):
        return self.first_name + " " + self.last_name


class TeamModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ad')
    last_name = models.CharField(max_length=50, verbose_name='Soyad')
    image = models.ImageField(upload_to='images/', default='images/avatar-big.png')
    branch_title = models.CharField(max_length=100, verbose_name='Peşə')

    class Meta:
        verbose_name = 'Üzv'
        verbose_name_plural = 'Komandamız'

    def __str__(self):
        return self.first_name + " " + self.last_name

class SkillModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Bacarıq')
    skill_owner = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name='skills')

    class Meta:
        verbose_name = 'Bacarıq'
        verbose_name_plural = 'Bacarıqlar'

    def __str__(self):
        return self.title

class AccountModel(models.Model):
    social_media = models.CharField(max_length=50, verbose_name='Sosial media')
    account_link = models.URLField(verbose_name='Hesab URL-i')
    owner = models.ForeignKey(TeamModel, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        verbose_name = 'Hesab'
        verbose_name_plural = 'Hesablar'

    def __str__(self):
        return self.social_media


class CompanyModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ad')
    logo = models.ImageField(upload_to='images/', verbose_name='Loqo')

    class Meta:
        verbose_name = 'Şirkət'
        verbose_name_plural = 'Bizimlə işləyən şirkətlər'

    def __str__(self):
        return self.name
    