from django.test import TestCase
from .models import Resources, Events
from django.urls import reverse

# Create your tests here.
# Testing Models
class ClubResourcesTest(TestCase):
    def test_stringOutput(self):
        clubresource=Resources(resourcename='Meet')
        self.assertEqual(str(clubresource), clubresource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resources._meta.db_table), 'clubresource')

class ClubEventsTest(TestCase):
    def test_stringOutput(self):
        clubevents=Events(eventname='Party')
        self.assertEqual(str(clubevents), clubevents.eventname)

    def test_tablename(self):
        self.assertEqual(str(Events._meta.db_table), 'clubevents')

class ClubCommentsTest(TestCase):
    def test_stringOutput(self):
        clubcomments=Comments(commenttitle='Be there!')
        self.assertEqual(str(clubcomments), clubcomments.reviewtitle)

    def test_tablename(self):
        self.assertEqual(str(Comments._meta.db_table), 'clubcomments')

# Testing Views & Templates
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self)
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
  
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')
    
class TestGetDetails(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/eventdetail')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('details'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('eventdetail'))
        self.assertTemplateUsed(response, 'club/details.html')

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
        
class TestNewEvent(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/newevent')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('newevent'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('newevent'))
        self.assertTemplateUsed(response, 'club/newevent.html')
     
class TestLoginMessage(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/loginmessage')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('loginmessage'))
        self.assertTemplateUsed(response, 'club/loginmessage.html')
    
class TestLogOutMessage(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/logoutmessage')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('logoutmessage'))
        self.assertTemplateUsed(response, 'club/logoutmessage.html')
    
class TestLogin(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/registration/login')
        self.assertEqual(response.status_code, 200)
  
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')
    
class New_Event_Form_Test(TestCase):

    # Valid Form Data
    def test_eventForm_is_valid(self):
        form = EventForm(data={'eventname': "Meeting", 'resources': "something", 'user': "Steve", 'evententrydate': "2018-12-17", 'eventurl': "http:google.com", 'eventdescription': "event description goes here"})
        self.assertTrue(form.is_valid())
    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = EventForm(data={'eventname': "Meeting", 'resources': "something", 'user': "Steve", 'evententrydate': "2018-12-17", 'eventurl': "http:google.com", 'eventdescription': "event description goes here"})
        self.assertFalse(form.is_valid())
