# -*- coding: utf-8 -*-
import pytest
from flaskr import flaskr

@pytest.fixture
def client():
  flaskr.app.config['TESTING'] = True
  client = flaskr.app.test_client()
  return client

def test_urls(client):
  r = client.get('/')
  assert r.status_code == 200

def test_login(client):
  r = client.get('/login')
  assert r.status_code == 200

def test_logout(client):
  r = client.get('/logout')
  assert r.status_code == 302

def test_add(client):
  r = client.post('/add')
  assert r.status_code == 401
