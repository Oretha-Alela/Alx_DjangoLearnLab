from django.test import TestCase

# Create your tests here.
import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    return User.objects.create_user(username="testuser", password="password")

def test_create_post(api_client, create_user):
    api_client.force_authenticate(user=create_user)
    response = api_client.post('/api/posts/', {'title': 'Test Post', 'content': 'Content here'})
    assert response.status_code == 201





import pytest
from rest_framework.test import APIClient
from accounts.models import CustomUser

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_users():
    user1 = CustomUser.objects.create_user(username="user1", password="password")
    user2 = CustomUser.objects.create_user(username="user2", password="password")
    return user1, user2

def test_follow_user(api_client, create_users):
    user1, user2 = create_users
    api_client.force_authenticate(user=user1)
    response = api_client.post(f'/accounts/follow/{user2.id}/')
    assert response.status_code == 200
    assert user2 in user1.following.all()

def test_unfollow_user(api_client, create_users):
    user1, user2 = create_users
    user1.following.add(user2)
    api_client.force_authenticate(user=user1)
    response = api_client.post(f'/accounts/unfollow/{user2.id}/')
    assert response.status_code == 200
    assert user2 not in user1.following.all()
