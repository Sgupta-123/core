from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('generic-student/',studentgeneric.as_view()),
    path('generic-student/<id>/',studentgeneric1.as_view()),
    path('register/',RegisterUser.as_view()),
    path('student/',StudentAPI.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', home),
    #            path('student/', post_student),
               path('get-book/', get_book),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
