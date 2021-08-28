from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from page.models import PageModel, ServiceModel, PropertyModel, WorkModel, SuggestionModel, PurposeModel, ContactModel, TeamModel, CompanyModel, PageAccountsModel


class PageView(View):

    def get(self, request):
        page = PageModel.objects.first()
        services = ServiceModel.objects.all()
        properties = PropertyModel.objects.all()
        works = WorkModel.objects.order_by('-id')
        suggestions = SuggestionModel.objects.all()
        purposes = PurposeModel.objects.all()
        team_members = TeamModel.objects.all()
        companies = CompanyModel.objects.order_by('-id')
        contact_messages = ContactModel.objects.filter(is_new=True)
        page_accounts = PageAccountsModel.objects.all()

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
        new_messages = ContactModel.objects.order_by('-id').filter(is_new=True)
        old_messages = ContactModel.objects.order_by('-id').filter(is_new=False)
        page = PageModel.objects.first()

        context = {
            'new_messages' : new_messages,
            'old_messages' : old_messages,
            'page' : page,
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