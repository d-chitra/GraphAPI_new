
from behave import given, when, then, step
import requests
import json
import responses
import pyfacebook
import datetime
import token

from six import iteritems



#access_token = "testdata/base/"

#BASE_PATH = "testdata/facebook/apidata/photos/"

@pytest.mark.usefixtures("setup")
@given(u 'set URL,access token')
def step_impl(context):
    global BASE_URL
    BASE_URL = "https://graph.facebook.com/{}/".format(pyfacebook.Api.VALID_API_VERSIONS[-1])
def access_token_setup(self):
    self.api = pyfacebook.Api(
    long_term_token="token"
    )

#BASE_PATH = "testdata/facebook/apidata/photos/"

    with open(BASE_PATH + "photos_page_1.json", "rb") as f:
        PHOTO_PAGED_1 = json.loads(f.read().decode("utf-8"))
    with open(BASE_PATH + "photos_page_2.json", "rb") as f:
        PHOTO_PAGED_2 = json.loads(f.read().decode("utf-8"))

    with open(BASE_PATH + "photo_info.json", "rb") as f:
        PHOTO_INFO = json.loads(f.read().decode("utf-8"))
    with open(BASE_PATH + "photos_info.json", "rb") as f:
        PHOTOS_INFO = json.loads(f.read().decode("utf-8"))


@when(u'set post photos request to the /{page-id}/feed endpoint')
def photosetup(self):
        self.api = pyfacebook.Api(
            app_id="12345678",
            app_secret="secret",
            long_term_token="token",
            version="v8.0"
        )

def testGetPhotosByObject(self):
        object_id = "5555555555"



@then(u 'get photos count')
#test count
with responses.RequestsMock() as m:
    m.add("GET", self.BASE_URL + object_id + "/photos", json=self.PHOTO_PAGED_1)
    m.add("GET", self.BASE_URL + object_id + "/photos", json=self.PHOTO_PAGED_2)

    photos = self.api.get_photos_by_object(
        object_id=object_id,
        count=None,
        limit=5,
    )
    self.assertEqual(len(photos), 10)

#Test count is none
with responses.RequestsMock() as m:
    m.add("GET", self.BASE_URL + object_id + "/photos", json=self.PHOTO_PAGED_1)
    m.add("GET", self.BASE_URL + object_id + "/photos", json=self.PHOTO_PAGED_2)

    photos = self.api.get_photos_by_object(
        object_id=object_id,
        count=None,
        limit=5,
    )
    self.assertEqual(len(photos), 10)

# POST Test Scenario
def testGetPhotoInfo(self):
    photo_id = "333333333"

    with responses.RequestsMock() as m:
        m.add("GET", self.BASE_URL + photo_id, json=self.PHOTO_INFO)

        photo = self.api.get_photo_info(
            photo_id=photo_id,
        )
        self.assertEqual(photo.id, photo_id)
        self.assertEqual(photo.album.id, "77777859")

        photo_json = self.api.get_photo_info(
            photo_id=photo_id,
            return_json=True
        )
        self.assertEqual(photo_json["id"], photo_id)


def testGetPhotos(self):
    ids = ["33333333", "3333444444"]

    with responses.RequestsMock() as m:
        m.add("GET", self.BASE_URL, json=self.PHOTOS_INFO)

        photo_dict = self.api.get_photos(
            ids=ids,
        )
        for _id, data in iteritems(photo_dict):
            self.assertIn(_id, ids)
            self.assertEqual(_id, data.id)

    with responses.RequestsMock() as m:
        m.add("GET", self.BASE_URL, json=self.PHOTOS_INFO)
        photo_dict = self.api.get_photos(
            ids=ids,
            return_json=True
        )
        for _id, data in iteritems(photo_dict):
            self.assertIn(_id, ids)
            self.assertEqual(_id, data["id"])





