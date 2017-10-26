from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^registration/$', views.SignUpView.as_view(), name='registration'),
    url(r'^users/$', views.UserListView.as_view(), name='users'),
    url(r'^inbox/$', views.InboxView.as_view(), name='inbox'),
    url(r'^sent/$', views.SentView.as_view(), name='sent'),
    url(r'^letters/(?P<letter_id>\d+)/$', views.LetterDetailView.as_view(), name='letter'),
    url(r'^letters/new_letter/$', views.SendLetterView.as_view(), name='new_letter'),
]