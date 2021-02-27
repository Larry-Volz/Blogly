from unittest import TestCase
from app import app
from flask import session

class BloglyTestCase(TestCase):
    def test_users_view(self):
        """ test if /users returns html file with phrase 'Add a user'"""
        with app.test_client() as test_server:
            resp = test_server.get('/users')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Add a user', html)  

    def test_users_new(self):
        '''test to see if /users/new  with GET method returns an html file'''
        with app.test_client() as test_server:
            resp = test_server.get('/users/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<input type="url" name="img_url" placeholder="URL for image (opt)"', html) 

    def test_users_new_post(self):
        '''test to see if /users/new with method = POST redirect properly to users'''
        with app.test_client() as test_server:
            resp = test_server.post('/users/new',   	# send via POST to color form @app.route('/fav-color')
                            data={'first_name': 'Zaphod'})	#simulating the data the form would have returned
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, 'users-and-form-link.html')

    # test to see if /users/1 return html file with style="display:inline;">Edit</button>

    # test to see if /users/1/edit method= ["POST"] returns a redirect code
