# -*- coding: utf-8 -*-

from django.test import TestCase
from django.urls import reverse


class TestEmptyResponses(TestCase):
    def test_empty_blog_list(self):
        response = self.client.get(reverse("post-list"))
        self.assertIn("No blog posts.".encode(), response.content)

    def test_missing_post_in_detail(self):
        response = self.client.get(reverse("post-detail", kwargs={"post_id": 484848}))
        self.assertEqual(response.status_code, 404)
