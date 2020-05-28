from  django.db.models import Max
from django.test import TestCase,Client

# Create your tests here.
from .models import Flight,Airport,Passenger

class FlightsTestCase(TestCase):

    def setUp(self):
        a1=Airport.objects.create(code="AAA", city="City A")
        a2=Airport.objects.create(code="BBB", city="City B")

        Flight.objects.create(origin=a1,destination=a2,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=200)
        Flight.objects.create(origin=a1,destination=a2,duration=-100)

    def flight_is_valid(self):
        a1=Airport.objects.get(code="AAA")
        a2=Airport.objects.get(code="BBB")
        f=Flight.objects.get(origin=a1,destination=a2,duration=100)
        self.assertTrue(f.flight_is_valid())

    def flight_is_not_valid(self):
        a1=Airport.objects.get(code="AAA")
        f=Flight.objects.get(origin=a1,destination=a1)
        self.assertFalse(f.flight_is_valid())

    def flight_is_not_valid(self):
        a1=Airport.objects.get(code="AAA")
        a2=Airport.objects.get(code="BBB")
        f=Flight.objects.get(origin=a1,destination=a2,duration=-100)
        self.assertFalse(f.flight_is_valid())

    def test_index(self):
        c= Client()
        response =c.get("/")
        self.assertEqual(response.status_code,200)
        print(f"{response.status_code}")
        self.assertEqual(response.context["flights"].count(),3)

    def test_valid_flight_page(self):
        a1=Airport.objects.get(code="AAA")
        f=Flight.objects.get(origin=a1,destination=a1)
        c=Client()
        response=c.get(f"/{f.id}")
        self.assertEqual(response.status_code,200)

    def test_invalid_flight(self):
        max_id=Flight.objects.all().aggregate(Max("id"))["id__max"]
        c=Client()
        response=c.get(f"/{max_id+1}")
        self.assertEqual(response.status_code,404)

if __name__== '__main__':
  main()
