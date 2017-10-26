from django.contrib.auth import  login, logout
from django.contrib.auth.models import User
from django.views.generic import FormView, View, ListView
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404

from .models import Letter
from .forms import LetterForm, UserCreationFormWidget, AuthenticationFormWidget


def index_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/inbox/")
    return render(request, 'base_generic.html')


class LoginFormView(FormView):
    form_class = AuthenticationFormWidget
    template_name = "registration/login.html"
    success_url = "/inbox/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class UserListView(ListView):
    model = User
    template_name = 'users.html'
    ordering = ['username']


class SignUpView(FormView):
    form_class = UserCreationFormWidget
    template_name = 'registration/signup.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)


class InboxView(ListView):
    model = Letter
    template_name = 'inbox.html'
    context_object_name = 'letters'
    ordering = ['-pub_date']

    def get(self, request, *args, **kwargs):
        self.queryset = Letter.objects.filter(to__exact=request.user)
        return super(InboxView, self).get(request)


class SentView(ListView):
    model = Letter
    template_name = 'sent.html'
    context_object_name = 'letters'
    ordering = ['-pub_date']

    def get(self, request, *args, **kwargs):
        self.queryset = Letter.objects.filter(author__exact=request.user)
        return super(SentView, self).get(request)


class LetterDetailView(View):
    template_name = 'letter_detail.html'

    def get(self, request, letter_id, *args, **kwargs):
        letter = Letter.objects.get(id=letter_id)
        if request.user == letter.author or request.user == letter.to:
            return render(request, self.template_name, {'letter': letter})
        else:
            return Http404


class SendLetterView(FormView):
    form_class = LetterForm
    success_url = '/sent/'
    template_name = 'new_letter.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_letter = form.save(commit=False)
            new_letter.author = request.user
            new_letter.save()
            return HttpResponseRedirect(reverse("sent"))
        else:
            return render(request, self.template_name, {"form": form})