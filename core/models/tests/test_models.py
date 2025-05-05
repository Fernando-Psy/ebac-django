# test_models.py

import pytest
from django.utils import timezone
from core.models import Post  # Importe seu modelo real

@pytest.mark.django_db
def test_post_creation(post_factory):
    post = post_factory.create()
    assert isinstance(post, Post)
    assert post.title
    assert post.slug
    assert post.author
    assert post.body
    assert isinstance(post.publish, timezone.datetime)
    assert isinstance(post.created, timezone.datetime)
    assert isinstance(post.update_on, timezone.datetime)
    assert post.status == 0