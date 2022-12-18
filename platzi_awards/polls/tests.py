
import datetime

from django.utils import timezone
from django.urls.base import reverse
from django.test import TestCase

from .models import Question

# Create your tests here.

class QuestionModelTests (TestCase):
    def setUp (self):
        """ SetUp a simple Question """
        self.question = Question(
            question_str='Test Question',
            publication_date=timezone.now()
        )

    def test_with_recently_published_question (self):
        """ Check if was_published_recently returns True is the question is from "right now" """
        self.assertTrue(self.question.was_published_recently())

    def test_with_old_questions (self):
        """ Check if was_published_recently returns False if the question is 1 day or older """
        test_time = timezone.now() - datetime.timedelta(days=1)

        self.question.publication_date = test_time

        self.assertFalse(self.question.was_published_recently())

    def test_with_future_questions (self):
        """ Check if was_published_recently returns False is the question is from the Future """

        test_time = timezone.now() + datetime.timedelta(days=30)

        self.question.publication_date = test_time

        self.assertFalse(self.question.was_published_recently())


class IndexPollsViewTests (TestCase):
    def setUp (self):
        """ SetUp the connection and http response """
        self.response = self.client.get(reverse('polls:q_index'))

    def test_connection (self):
        """ Check if there's a good 200 http conection """
        self.assertEqual(self.response.status_code, 200)

    def test_no_questions (self):
        """ Check if there's no questions, the view will display the No questions message """
        self.assertContains(self.response, 'No Polls are Available')
        self.assertQuerysetEqual(self.response.context['latest_question_list'], [])

    def test_questions (self):
        """ Check if there's questions, the view will display them correctly """

        # Create Test Questions
        Question(question_str='Test_1', publication_date=timezone.now()).save()
        Question(question_str='Test_2', publication_date=timezone.now()).save()
        Question(question_str='Test_3', publication_date=timezone.now()).save()

        # Re Connect to URL
        self.response = self.client.get(reverse('polls:q_index'))

        # Check Questions
        self.assertContains(self.response, 'Test_1')
        self.assertContains(self.response, 'Test_2')
        self.assertContains(self.response, 'Test_3')

        self.assertQuerysetEqual(
            self.response.context['latest_question_list'], 
            Question.objects.all()[::-1] # Reverse List Order
        )
    
    def test_non_display_of_future_questions (self):
        """ Check if there's questions, and avoid displaying the ones from the future """
        # Create Question
        test_time = timezone.now() + datetime.timedelta(days=30)
        Question(question_str='Future Question Test', publication_date=test_time).save()

        Question(question_str='Test_1', publication_date=timezone.now()).save()
        Question(question_str='Test_2', publication_date=timezone.now()).save()
        Question(question_str='Test_3', publication_date=timezone.now()).save()

        # Reload View
        self.response = self.client.get(reverse('polls:q_index'))

        # Check Question
        self.assertNotContains(self.response, 'Future Question Test')
        
        for question in self.response.context['latest_question_list']: 
            self.assertNotEqual(question.question_str, 'Future Question Test')


class QuestionDetailViewTests (TestCase):
    def test_future_question_details (self):
        """ Checks if question is from the future, and returns 404 """
        test_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_str='future question', publication_date=test_time)
        future_question.save()

        url = reverse('polls:q_info', args=[future_question.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_past_question_details (self):
        """ Check if Question is from the past, and check if it's displaying its str """
        test_time = timezone.now() - datetime.timedelta(days=10)
        past_question = Question(question_str='past question', publication_date=test_time)
        past_question.save()

        url = reverse('polls:q_info', args=[past_question.id])
        response = self.client.get(url)

        self.assertContains(response, past_question.question_str)