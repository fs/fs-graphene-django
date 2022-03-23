import pytest

from graphene_django_pretty.types.base import BaseDjangoModelUnion, BaseDjangoObjectType
from tests.django_setup.models import Article, Author, Post


class PostType(BaseDjangoObjectType):

    class Meta:
        model = Post
        fields = '__all__'


class ArticleType(BaseDjangoObjectType):

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
    class TextUnion(BaseDjangoModelUnion):

        class Meta:
            types = (PostType, ArticleType)

    assert TextUnion.resolve_type(data[0], None) == ArticleType
    assert TextUnion.resolve_type(data[1], None) == PostType
