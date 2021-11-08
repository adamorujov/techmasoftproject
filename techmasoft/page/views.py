from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from page.models import PageModel, ServiceModel, PropertyModel, WorkModel, SuggestionModel, PurposeModel, ContactModel, TeamModel, CompanyModel, PageAccountsModel
from page import models
from datetime import date
from datetime import datetime

class PageView(View):

    def get(self, request):
        if not self.request.user.is_staff:
            models.PageView.objects.create(view_month=date.today().month, view_year=date.today().year)

        page = PageModel.objects.first()
        services = ServiceModel.objects.order_by('id')
        properties = PropertyModel.objects.order_by('id')
        works = WorkModel.objects.order_by('-id')
        suggestions = SuggestionModel.objects.order_by('id')
        purposes = PurposeModel.objects.order_by('id')
        team_members = TeamModel.objects.order_by('id')
        companies = CompanyModel.objects.order_by('-id')
        contact_messages = ContactModel.objects.filter(is_new=True)
        page_accounts = PageAccountsModel.objects.order_by('id')

        context = {
            'page' : page,
            'services' : services,
            'properties' : properties,
            'works' : works,
            'suggestions' : suggestions,
            'purposes' : purposes,
            'team_members' : team_members,
            'companies' : companies,
            'contact_messages' : contact_messages,
            'contact_messages_length' : len(contact_messages),
            'page_accounts' : page_accounts,
        }

        return render(request, 'pages/page.html', context)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        country_code = request.POST.get('num')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        ContactModel.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            country_code=country_code,
            telephone_number=phone_number,
            message=message
        )

        messages.success(request, 'Mesajınız müvəffəqiyyətlə göndərildi. Sizinlə tezliklə əlaqə saxlanılacaq.')
        return render(request, 'pages/messagesent.html')

class MessagesListView(LoginRequiredMixin, View):
    login_url = '/'
    
    def get(self, request):

        date_value = request.GET.get('date')

        new_messages = ContactModel.objects.order_by('-id').filter(is_new=True)
        old_messages = ContactModel.objects.order_by('-id').filter(is_new=False)
        page = PageModel.objects.first()

        if date_value:
            date_value = datetime.strptime(date_value, "%Y-%m-%d").date()
            page_daily_view = models.PageView.objects.filter(view_day = date_value)
            page_monthly_view = models.PageView.objects.filter(view_month = date_value.month, view_year=date_value.year)
            page_yearly_view = models.PageView.objects.filter(view_year = date_value.year)
            default_date = date_value.strftime("%Y-%m-%d")
        else:
            page_daily_view = models.PageView.objects.filter(view_day = date.today())
            page_monthly_view = models.PageView.objects.filter(view_month = date.today().month, view_year=date.today().year)
            page_yearly_view = models.PageView.objects.filter(view_year = date.today().year)
            default_date = date.today().strftime("%Y-%m-%d")

        context = {
            'new_messages' : new_messages,
            'old_messages' : old_messages,
            'page' : page,

            'default_date': default_date,
            'page_daily_view': page_daily_view,
            'page_monthly_view': page_monthly_view,
            'page_yearly_view': page_yearly_view,
        }

        return render(request, 'pages/messages.html', context)

    def post(self, request):
        new_messages = ContactModel.objects.order_by('-id').filter(is_new=True)
        old_messages = ContactModel.objects.order_by('-id').filter(is_new=False)
        choice = request.POST.get('choice')

        if choice == 'archive':
            new_messages.update(is_new=False)
        elif choice == 'delete':
            old_messages.delete()

        return redirect('messages')
    

def archive(request, id):
    message = ContactModel.objects.get(id=id)
    message.is_new = False
    message.save()

    return redirect('messages')

def delete(request, id):
    message = ContactModel.objects.get(id=id)
    message.delete()

    return redirect('messages')