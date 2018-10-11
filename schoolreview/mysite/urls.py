from django.contrib import admin
from django.urls import include, path

from polls import views as pollsviews

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', pollsviews.home,name='home'),
    path('accounts/', include('accounts.urls',namespace="accounts")),
]
