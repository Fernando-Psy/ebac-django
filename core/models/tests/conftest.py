import pytest
from factory.django import DjangoModelFactory
import factory
from django.contrib.auth.models import User
from core.models import Post  # Certifique-se de usar o import correto para seu modelo


# -------------------------------

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall('set_password', 'password123')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    slug = factory.Faker('slug')
    author = factory.SubFactory(UserFactory)
    body = factory.Faker('paragraph')
    status = 0  # Valor padrão correto

# -------------------------------

@pytest.fixture
def user_factory():
    return UserFactory

@pytest.fixture
def post_factory():
    return PostFactory