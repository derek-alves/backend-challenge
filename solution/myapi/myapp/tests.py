import json

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase

from myapp.models import Place
from myapp.serializers import PlaceSerializer


class ViewsTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(ViewsTestCase, cls).setUpClass()
        mixer.blend('myapp.Place')

    def test_create_place(self):
        data = {"name": "Test name1", "slug": "Test-slug", "city": "Test city", "state": "Test state"}
        response = self.client.post("/place/", data=data)
        data["slug"] = "Wrong slug"
        bad_response = self.client.post("/place/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(bad_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_places(self):
        response = self.client.get("/place/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_specific_place(self):
        response = self.client.get("/place/1/")
        response_not_found = self.client.get("/place/2/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_not_found.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_place(self):
        response = self.client.put("/place/1/", data={"name": "updated name", "slug": "updated-slug"})
        response_not_found = self.client.put("/place/2/", data={"name": "updated name"})
        bad_response = self.client.put("/place/1/", data={"slug": "updated slug"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["slug"], "updated-slug")
        self.assertEqual(response_not_found.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(bad_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_destroy_place(self):
        response = self.client.delete("/place/1/")
        response_not_found = self.client.delete("/place/2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_not_found.status_code, status.HTTP_404_NOT_FOUND)
