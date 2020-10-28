
from behave import given, when, then, step
import requests
import token
import json
import responses
import pyfacebook
import datetime


from six import iteritems


#access_token = "testdata/base/"

#BASE_PATH = "testdata/facebook/apidata/photos/"

@given(u'set URL,access token')')
@pytest.mark.usefixtures("setup")
def APIPagetest(testcase):
    BASE_PATH = "testdata/facebook/apidata/pages/"
    BASE_URL = "https://graph.facebook.com/{}/".format(pyfacebook.Api.VALID_API_VERSIONS[-1])

def access_token_setup(self):
        self.api = pyfacebook.Api(
            long_term_token="token"
        )

    with open(BASE_PATH + "single_default_page.json", "rb") as f:
        SINGLE_PAGE_INFO_1 = json.loads(f.read().decode("utf-8"))
    with open(BASE_PATH + "single_fields_page.json", "rb") as f:
        SINGLE_PAGE_INFO_2 = json.loads(f.read().decode("utf-8"))


@then(u'get page id,page cover id, page.cover.id, page.category_list)
def testPage(self):

        with self.assertRaises(pyfacebook.PyFacebookException):
            self.api.get_page_info()

        page_id = "1234567"
        with responses.RequestsMock() as m:
            m.add("GET", self.BASE_URL + page_id, json=self.SINGLE_PAGE_INFO_1)
            page = self.api.get_page_info(
                page_id=page_id,
        )
            self.assertEqual(page.id, "1234567")
            self.assertEqual(page.cover.id, "11111111111")
            self.assertEqual(len(page.category_list), 2)
            self.assertEqual(page.start_info.date.year, 2020)
            self.assertEqual(page.picture.height, 50)

        # test fields
        page_username = "facebookapp"
        with responses.RequestsMock() as m:
            m.add("GET", self.BASE_URL + page_username, json=self.SINGLE_PAGE_INFO_2)
            page = self.api.get_page_info(
                username=page_username,
                fields="id,name,username,fan_count",
                return_json=True
            )

            self.assertEqual(page["username"], page_username)
            self.assertEqual(page["fan_count"], 23232323)



            for _id, data in iteritems(res1):
                self.assertIn(_id, ids)
                self.assertIn(_id.lower(), [data.id, data.username.lower()])

            res2 = self.api.get_pages_info(
                ids=",".join(ids),
                return_json=True
            )

