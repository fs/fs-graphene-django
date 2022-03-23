import pytest
from graphene_django import DjangoObjectType

from graphene_django_pretty.types.base import BaseUnion
from tests.django_setup.models import Article, Author, Post


class PostType(DjangoObjectType):

    class Meta:
        model = Post
        fields = '__all__'


class ArticleType(DjangoObjectType):

    class Meta:
        model = Article
        fields = '__all__'


@pytest.fixture()
def data():
    author = Author.objects.create(name='test')
    return (
        Article.objects.create(author=author, text='test'),
        Post.objects.create(author=author, text='test'),
    )


@pytest.mark.django_db()
def test_union(data):

    class TextUnion(BaseUnion):

        class Meta:
            types = (PostType, ArticleType)

    assert TextUnion.resolve_type(data[0], None) == ArticleType
    assert TextUnion.resolve_type(data[1], None) == PostType
