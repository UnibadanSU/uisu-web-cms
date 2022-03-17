from django.contrib.auth import get_user_model
from django.test import tag
import graphene
from graphene_django import DjangoObjectType

from news import models


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile


class ArticleType(DjangoObjectType):
    class Meta:
        model = models.Article


class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class ExecutiveType(DjangoObjectType):
    class Meta:
        model = models.Executive

class Query(graphene.ObjectType):
    all_articles = graphene.List(ArticleType)
    all_executives = graphene.List(ExecutiveType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    article_by_slug = graphene.Field(ArticleType, slug=graphene.String())
    article_by_author = graphene.List(ArticleType, username=graphene.String())
    article_by_tag = graphene.List(ArticleType, tag=graphene.String())

    def resolve_all_articles(root, info):
        return (
            models.Article.objects.prefetch_related("tags").select_related("author").all()
        )

    def resolve_all_executives(root, info):
        return models.Executive.objects.all()

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_article_by_slug(root, info, slug):
        return (
            models.Article.objects.prefetch_related("tags").select_related("author").get(slug=slug)
        )

    def resolve_articles_by_author(root, info, username):
        return (
            models.Article.objects.prefetch_related("tags").select_related("author").filter(author__user__username=username)
        )

    def resolve_articles_by_tag(root, info, tag):
        return (
            models.Article.objects.prefetch_related("tags").select_related("author").filter(tags__name__iexact=tag)
        )


schema = graphene.Schema(query=Query)