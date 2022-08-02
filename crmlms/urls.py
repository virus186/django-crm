from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

admin.site.site_header = "CRM LMS Admin"
admin.site.index_title = "Welcome to CRM LMS"
admin.site.site_title = "CRM LMS"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', include('crm.urls'))
]
