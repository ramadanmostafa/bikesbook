from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from custom_user.models import CustomUser
from garage.models import BicyceStyle, BicycleMake

# Create your tests here.
class TestFileSending(APITestCase):

    def test_file(self):
        self.data = {
            "country_code": "002",
            "mobile_number": "01116620840",
            "full_name": "Ramadan"
        }
        response = self.client.post(reverse("register"), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.data = {
            "pin_code":CustomUser.objects.get(mobile_number="01116620840").pin_code,
            "mobile_number":"01116620840"
        }
        response = self.client.post(reverse("chkactivation"), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.token = "token " + response.data["token"]
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

        BicyceStyle.objects.create(style="style_test", active=True)
        BicycleMake.objects.create(brand="brand_test", active=True)

        self.data = {
            "make": 1,
            "style": 1,
            "color": "red",
            "default": True
        }
        response = self.client.post(reverse("addbicycle"), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.data = {
            "start_lat": 12345,
            "start_lng": 65432,
            "bicycle": 1,
            "start_place": "Cairo"
        }


        response = self.client.post(reverse("startride"), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        ride_id = int(response.data["id"])
        self.data = {
            "id":ride_id,
            "end_lat": 12545,
            "end_lng": 9999,
            "distance": "55",
            "duration": "66",
            "max_speed": "77",
            "end_place": "Giza"

        }
        response = self.client.put(reverse("endride"), self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        file_path = "C:\\Users\\pc\\Desktop\\Projects\\Bikes Book\\bikesbook\\ride\\test.json"
        self.data = {
            "id": ride_id,
            "path_file": open(file_path) # {'file': ("test.json", open(file_path, 'rb'), 'text/json', {'Expires': '0'})}

        }
        response = self.client.put(
            reverse("ridefile"),
            self.data,
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)




