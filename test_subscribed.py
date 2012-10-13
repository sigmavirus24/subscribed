#!/usr/bin/env python

from subscribed import app
from unittest import TestCase, main

SUCCESS = '200 OK'
REDIRECT = '302 FOUND'


class TestSubscribed(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def assert_valid_redirect(self, resp):
        assert resp.status == REDIRECT
        assert 'Location' in resp.headers
        assert 'http://localhost/' == resp.headers['Location']

    def test_index(self):
        resp = self.app.get('/')
        assert resp.status == SUCCESS

    def test_good_user(self):
        resp = self.app.get('/sigmavirus24')
        assert resp.status == SUCCESS

    def test_bad_user(self):
        # Orgs
        self.assert_valid_redirect(self.app.get('/github'))
        # Non-existant user (as of 2012-10-13)
        self.assert_valid_redirect(self.app.get('/sigmavirus240'))

    def test_good_repo(self):
        resp = self.app.get('/sigmavirus24/github3.py')
        assert resp.status == SUCCESS

    def test_bad_repo(self):
        self.assert_valid_redirect(self.app.get('/sigmavirus24/github3.py0'))


if __name__ == '__main__':
    main()
