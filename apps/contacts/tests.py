from django.test import TestCase

from models import Contacts

class MyTests(TestCase):
    def test_init(self):
        contact = Contacts.objects.create(name='Lena', surname='Dmitrieva',
                                          birthday='1999-12-31', bio='Some',
                                          contacts='some')
        self.assertEqual(contact.id, 1)
