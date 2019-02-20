from django.test import TestCase
from .models import Resources, Events
from django.urls import reverse

# Create your tests here.
# Testing Models
class ClubResourcesTest(TestCase):
    def test_stringOutput(self):
        clubresource=Resources(resourcename='Meeting')
        self.assertEqual(str(clubresource), clubresource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resources._check_meta.db_table), 'clubresource')
  
# Testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self)
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
  
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')
    
class TestGetEvents(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/getevents')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getevents'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('getevents'))
        self.assertTemplateUsed(response, 'club/events.html')