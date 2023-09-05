# from django.test import TestCase, Client
# from django.contrib.auth.models import User
# from .models import Profile
#
#
# class ProfileViewTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.login(username='testuser', password='testpassword')
#
#     def test_profile_view_get(self):
#         self.profile = Profile.objects.create(username=self.user.username, user=self.user)
#         response = self.client.get('/user/profile/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'profile.html')
#
#     def test_profile_view_post_valid_form(self):
#         profile = Profile.objects.create(user=self.user)
#         data = {"username": "new_username"}
#         response = self.client.post('/user/profile/', data)
#         self.assertEqual(response.status_code, 302)
#         updated_profile = Profile.objects.get(user=self.user)
#         self.assertEqual(updated_profile.username, 'new_username')
#         self.assertTrue(updated_profile.profile_image)
#
#     def test_profile_view_invalid_form(self):
#         profile = Profile.objects.create(user=self.user)
#         data = {"username": ''}
#         response = self.client.post('/user/profile/', data=data)
#         self.assertEqual(response.status_code, 200)
#         form = response.context['form']
#         # print(form.errors)
#         self.assertTrue(form.errors)
