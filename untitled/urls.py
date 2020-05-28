"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings


import cms.views as cms_view
from django.urls import include

urlpatterns = [
    #path('img_filter/', cms_view.ImgFilterView.kernel_cell, 'kernel_cell'),

    url(r'^admin/', admin.site.urls),
    url(r'^', cms_view.ImgFilterView.as_view()),  # URLとViewを組み合わせる！
    url(r'^img_filter/', cms_view.ImgFilterView.as_view()),  # URLとViewを組み合わせる！
    # path('img_filter', cms_view.ImgFilterView.as_view(), name='img_filter')

    # path('success/url/', cms_view.success),
    # path('file_upload/', include('file_upload.urls')),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
