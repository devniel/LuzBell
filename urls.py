from django.conf.urls import patterns, include, url
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('apps.main.urls', namespace="main")),
    url(r'^admin/', include(admin.site.urls)),
)