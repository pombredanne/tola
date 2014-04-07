from django.test import TestCase
from read.models import Read
from django.utils import timezone

# models test
class ReadTest(TestCase):

    def create_read(self, read_title="only a test", type="json",read_url="http://www.formhub.org",description="Test description"):
        return Read.objects.create(read_title=read_title, type=type,read_url=read_url,description=description,create_date=timezone.now())

    def test_whatever_creation(self):
        r = self.create_read()
        self.assertTrue(isinstance(r, Read))
        self.assertEqual(r.__unicode__(), r.read_title)