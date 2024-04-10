from django.urls import path

from shop.apps import ShopConfig
from shop.views import FactoryCreateApiView, FactoryListApiView, RetailListApiView, RetailCreateApiView, \
    EntrepreneurCreateApiView, EntrepreneurListApiView, EntrepreneurDestroyApiView, \
    EntrepreneurUpdateApiView, RetailUpdateApiView, RetailDestroyApiView

app_name = ShopConfig.name

urlpatterns = [
    path('factory/create/', FactoryCreateApiView.as_view(), name='factory-create'),
    path('factory/list/', FactoryListApiView.as_view(), name='factory-list'),
    path('retail/list/', RetailListApiView.as_view(), name='retail-list'),
    path('retail/create/', RetailCreateApiView.as_view(), name='retail-create'),
    path('entrepreneur/list/', EntrepreneurListApiView.as_view(), name='entrepreneur-list'),
    path('entrepreneur/create/', EntrepreneurCreateApiView.as_view(), name='entrepreneur-create'),
    path('entrepreneur/<int:pk>/update/', EntrepreneurUpdateApiView.as_view(), name='entrepreneur-update'),
    path('entrepreneur/<int:pk>/delete/', EntrepreneurDestroyApiView.as_view(), name='entrepreneur-delete'),
    path('retail/<int:pk>/update/', RetailUpdateApiView.as_view(), name='retail-update'),
    path('retail/<int:pk>/delete/', RetailDestroyApiView.as_view(), name='retail-delete'),
]