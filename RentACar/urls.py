<<<<<<< HEAD

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
=======
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 11112e836c1e89970a62c440bd0123f475fbb2c2


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('account/', include(('account.urls', 'account'), namespace='account')),
=======
    path('', include(('main.urls', 'main'), namespace='main')),
>>>>>>> 11112e836c1e89970a62c440bd0123f475fbb2c2

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
