from django.test import Client, TestCase
from django.urls import reverse

from feedback.forms import FeedbackForm


class FeedbackFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_if_form_in_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_text_label(self):
        name_label = self.form.fields['text'].label
        self.assertEqual('Текст вашего сообщения', name_label)

    def test_text_help_text(self):
        text_help_text = self.form.fields['text'].help_text
        self.assertEqual('Введите ваше сообщение', text_help_text)

    def test_redirect(self):
        response = Client().post(reverse('feedback:feedback'))
        self.assertRedirects(response, reverse('feedback:feedback'))
