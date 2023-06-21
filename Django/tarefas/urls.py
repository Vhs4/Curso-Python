from django.urls import path
from appteste.views import BrandCreateViewSet
from appteste.views import BrandRetrieveUpdateDeleteViewSet
from appteste.views import BrandListViewSet
from appteste.views import RequestTestAPI
from .docs import schema_view

urlpatterns = [
    path("api/v1/brand/create", BrandCreateViewSet.as_view(), name="brand_create" ),

    path("api/v1/brand/<int:pk>/retrieve", BrandRetrieveUpdateDeleteViewSet.as_view(), name="brand_retrieve" ),

    path("api/v1/brand/<int:pk>/update", BrandRetrieveUpdateDeleteViewSet.as_view(), name="brand_update" ),

    path("api/v1/brand/<int:pk>/destroy", BrandRetrieveUpdateDeleteViewSet.as_view(), name="brand_destroy" ),

    path("api/v1/brand/list", BrandListViewSet.as_view(), name="brand_list" ),

    path("api/v1/request/", RequestTestAPI.as_view(), name="brand_test" ),
    
    path('docs/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]