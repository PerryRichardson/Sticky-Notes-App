from django.test import TestCase
from django.urls import reverse
from notes.models import Note, Author

class NoteTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note.",
            author=self.author
        )

    def test_note_list_view(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is a test note.")

    def test_note_create_view(self):
        response = self.client.post(reverse("note_create"), {
            "title": "New Note",
            "content": "New note content.",
            "author": self.author.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(Note.objects.last().title, "New Note")

    def test_note_update_view(self):
        response = self.client.post(reverse("note_update", args=[self.note.pk]), {
            "title": "Updated Title",
            "content": "Updated content.",
            "author": self.author.id
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Title")

    def test_note_delete_view(self):
        response = self.client.post(reverse("note_delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.pk).exists())
