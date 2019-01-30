import unittest
import json
from app.test.base import BaseTestCase

def register_user(self):
    return self.client.post(
        '/user',
        data=json.dumps(dict(
            email='bane@email.com',
            username='oliver',
            password='123456'
        )),
        content_type='application/json'
    )

def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='bane@email.com',
            password='123456'
        ))
        content_type='application/json'
    )

class TestAuthBlueprint(BaseTestCase):
    def test_registered_user_login(self):
        with self.client:
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

    def test_valid_logout(self):
        with self.client:
            user_response = register_user(self)
            response_data = json.loads(user_response.data.decode())
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            login_response = login_user(self)
            data = json.loads(login_response.data.decode())
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

            response = self.client.post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer '+ json.loads(
                        login_response.data.decode()
                    ) ['Authorization']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            sefl.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()