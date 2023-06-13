from django.urls import path
from appteste.views import BrandCreateViewSet
from appteste.views import BrandRetrieveUpdateDeleteViewSet
from appteste.views import BrandListViewSet
from appteste.views import RequestTestAPI

urlpatterns = {
    path("api/v1/brand/create", BrandCreateViewSet.as_view(), name="brand")

    path("api/v1/brand/<int:pk>/")

    path("api/v1/brand/<int:pk>/")

    path("api/v1/brand/<int:pk>/")
    
    path("api/v1/brand")
    
    path("api/v1/request/")
}