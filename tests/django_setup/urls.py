from django.urls import path

from graphene_django_pretty.views import PrettyGraphQLView

urlpatterns = [
    path('graphql/batch', PrettyGraphQLView.as_view(batch=True)),
    path('graphql', PrettyGraphQLView.as_view(graphiql=True)),
]
