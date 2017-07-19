from django.test import TestCase, Client
from .models import ToDoList
from django.urls import reverse
import json
# Create your tests here.

class ModelTestCase(TestCase):
    """Testing untuk models"""
    def setUp(self):
        self.todolist = ToDoList(activity='swimming', done=False)

    def test_model_can_create_todolist(self):
        old_count = ToDoList.objects.count()
        self.todolist.save()
        new_count = ToDoList.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    def test_view_can_send_initial_web(self):
        myclient = Client()
        response = myclient.get('/index/')
        self.assertEquals(response.status_code, 200)

    def test_view_can_add_new_data(self):
        myclient = Client()
        posted_dictionary = {'activity':'swimming', 'done':False}
        response = myclient.post('/index/post', json.dumps(posted_dictionary), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_view_can_delete_data(self):
        todolist = ToDoList(activity='swimming', done=False)
        todolist.save()
        myclient = Client()
        list_item_to_be_deleted = [{'activity':'swimming'}]
        response = myclient.post('/index/delete', json.dumps(list_item_to_be_deleted), content_type="application/json")
        self.assertEquals(response.status_code, 200)
