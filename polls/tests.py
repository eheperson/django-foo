from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from polls.models import Question

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)

# ----------------------------------------------------------------------------------------

# create a Question instance with pub_date 30 days in the future
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
# was it published recently?
future_question.was_published_recently()


from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
# create an instance of the client for our use
client = Client()


# get a response from '/'
response = client.get('/')
# Not Found: /
# we should expect a 404 from that address; if you instead see an
# "Invalid HTTP_HOST header" error and a 400 response, you probably
# omitted the setup_test_environment() call described earlier.

print(response.status_code) 
#404


# on the other hand we should expect to find something at '/polls/'
# we'll use 'reverse()' rather than a hardcoded URL
from django.urls import reverse
response = client.get(reverse('polls:index'))

print(response.status_code) 
#200

print(response.content) 
#b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'

print(response.context['latest_question_list'])
# <QuerySet [<Question: What's up?>]>