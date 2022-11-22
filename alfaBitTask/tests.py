from django.test import TestCase

from django.test import TestCase
from alfaBitTask.models import Lead, LeadState



class LeadTest(TestCase):


    def create_lead_object(self, name='first_lead_obj'):
        return Lead.objects.create(name=name)
    
    def create_lead_status_object(self, name='STATE_NEW'):
        return LeadState.objects.create(name=name)

    def test_create_lead_object(self):
        new_status = LeadState.objects.create(name='STATE_NEW')

        obj = self.create_lead_object()
        self.assertEqual(obj.state, new_status)

    def test_update_to_valid_statuses(self):
        in_progress_status = LeadState.objects.create(name='STATE_IN_PROGRESS')
        postponed_status = LeadState.objects.create(name='STATE_POSTPONED')
        done_status = LeadState.objects.create(name='STATE_DONE')

        obj = self.create_lead_object()

        Lead.status_update(obj, in_progress_status)
        self.assertEqual(obj.state, in_progress_status)
        Lead.status_update(obj, postponed_status)
        self.assertEqual(obj.state, postponed_status)
        Lead.status_update(obj, done_status)
        self.assertEqual(obj.state, done_status)

    def test_update_to_invalid_statuses(self):
        obj = self.create_lead_object()
        new = self.create_lead_status_object()

        in_progress_status = LeadState.objects.create(name='STATE_IN_PROGRESS')
        postponed_status = LeadState.objects.create(name='STATE_POSTPONED')
        done_status = LeadState.objects.create(name='STATE_DONE')
        
        status = Lead.status_update(obj, done_status)
        self.assertEqual(False, status)

        status = Lead.status_update(obj, postponed_status)
        self.assertEqual(False, status)

        status = Lead.status_update(obj, in_progress_status)
        self.assertEqual(True, status)





