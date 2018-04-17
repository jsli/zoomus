__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"

import unittest

from zoomus import (
    components_v2,
    ZoomClientV2)


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ZoomClientTestCase))
    return suite


COMPONENTS_V2_LIST = ['user']

API_KEY = '_al9--GoSLeJREEXExH67A'

API_SECRET = 'kUYuuyjAHpMPaCc2dg4jV0WduhqRLDbOd3CE'

TOKEN_EXP = 3600

ACCESS_TOKEN = ZoomClientV2.generate_access_token(API_KEY, API_SECRET, TOKEN_EXP)

RESULT = {
    True: 'OK',
    False: 'FAIL'
}


def generate_client():
    client = ZoomClientV2(ACCESS_TOKEN)
    return client


class ZoomClientTestCase(unittest.TestCase):
    def check_result(self, tag, result, expected_result):
        print 'Test %s: %s' % (tag, RESULT[result == expected_result])
        self.assertEqual(result, expected_result)

    def test_init_sets_config(self):
        client = generate_client()
        self.assertEqual(
            client.config,
            {
                'access_token': ACCESS_TOKEN,
                'debug': True,
                'headers': {
                    'Content-Type': 'application/json; charset=utf-8',
                    'Accept-Type': 'application/json; charset=utf-8'
                }
            }
        )

    def test_init_creates_all_components(self):
        client = generate_client()
        self.assertEqual(
            set(COMPONENTS_V2_LIST),
            set(client.components.keys())
        )
        self.assertIsInstance(
            client.components['user'],
            components_v2.user.UserComponentV2
        )

    def test_can_get_access_token(self):
        client = generate_client()
        self.assertEqual(client.access_token, ACCESS_TOKEN)

    def test_can_set_access_token(self):
        client = generate_client()
        client.access_token = 'NEW-ACCESS-TOKEN'
        self.assertEqual(client.access_token, 'NEW-ACCESS-TOKEN')

    def test_can_get_user_component(self):
        client = generate_client()
        self.assertIsInstance(
            client.user,
            components_v2.user.UserComponentV2
        )

    def test_can_list_user(self):
        client = generate_client()
        result = client.user.list().status_code
        self.check_result('list user', result, 200)

    def test_can_create_user(self):
        client = generate_client()
        data = {
            "action": "create",
            "user_info": {
                "email": "lijinsong@xiaoyezi.com",
                "type": "1",
                "first_name": "1string",
                "last_name": "2string",
                "password": "3string"
            }
        }
        res = client.user.create(**data)
        result = res.status_code
        self.check_result('create user', result, 201)

    def test_can_retrieve_user(self):
        client = generate_client()
        result = client.user.retrieve('xWfyVOQKTpKfLnKWTkHQoQ').status_code
        self.check_result('retrieve user', result, 200)

    def test_can_retrieve_user_token(self):
        client = generate_client()
        result = client.user.retrieve_token('cqkltPzvTO2XfcnwQzUPqw').status_code
        self.check_result('retrieve user token', result, 200)

    def test_can_update_user(self):
        client = generate_client()
        data = {
            "first_name": "32321string",
            "last_name": "23232string",
            "password": "332string"
        }
        result = client.user.update('xWfyVOQKTpKfLnKWTkHQoQ', **data).status_code
        self.check_result('update user', result, 204)

    def test_can_delete_user(self):
        client = generate_client()
        params = {
            'action': 'delete'
        }
        result = client.user.delete('xWfyVOQKTpKfLnKWTkHQoQ', **params).status_code
        self.check_result('delete user', result, 204)

    def test_can_list_user_assistants(self):
        client = generate_client()
        result = client.user.list_assistants('cqkltPzvTO2XfcnwQzUPqw').status_code
        self.check_result('list user assistants', result, 200)


if __name__ == '__main__':
    unittest.main()
