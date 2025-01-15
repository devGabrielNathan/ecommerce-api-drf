from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from ecommerce.users.views.address import (
    AddressGenericListCreate,
    AddressGenericRetrieveUpdateDestroy,
)
from ecommerce.users.views.phone import (
    PhoneGenericListCreate,
    PhoneGenericRetrieveUpdateDestroy,
)
from ecommerce.users.views.supplier import (
    SupplierGenericListCreate,
    SupplierGenericRetrieveUpdateDestroy,
)
from ecommerce.users.views.user import (
    UserAccess,
    UserLoginObtainPairView,
    UserLogoutApiView,
)

urlpatterns = [
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path('login/', UserLoginObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserAccess.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserAccess.as_view(), name='user-detail'),
    path(
        'suppliers/', SupplierGenericListCreate.as_view(), name='supplier-list'
    ),
    path(
        'suppliers/<uuid:pk>/',
        SupplierGenericRetrieveUpdateDestroy.as_view(),
        name='supplier-detail',
    ),
    path(
        'addresses/', AddressGenericListCreate.as_view(), name='address-list'
    ),
    path(
        'addresses/<uuid:pk>/',
        AddressGenericRetrieveUpdateDestroy.as_view(),
        name='address-detail',
    ),
    path('phones/', PhoneGenericListCreate.as_view(), name='phone-list'),
    path(
        'phones/<uuid:pk>/',
        PhoneGenericRetrieveUpdateDestroy.as_view(),
        name='phone-detail',
    ),
]
