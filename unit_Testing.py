
import unittest
from app import app
from app import Investor



# response1 = [
#     {
#         "InvestorEmail": "ahmed@hotmail.com",
#         "InvestorName": "ahmed",
#         "InvestorPhone": "0503733067"
#     },
#     {
#         "InvestorEmail": "lotfi@hotmail.com",
#         "InvestorName": "lotfi",
#         "InvestorPhone": "0503733067"
#     },
#     {
#         "InvestorEmail": "dob@hotmail.com",
#         "InvestorName": "dob",
#         "InvestorPhone": "0503733067"
#     }
# ]

class FlaskTest(unittest.TestCase):

    # Testing the model Investor
    def test_createClass(self):
        newInvestor = Investor("Ahmed", "Ahmedlarbiofficial@gmail.com",'0503733067')
        self.assertEqual(newInvestor.name, "Ahmed")
        self.assertEqual(newInvestor.email, "Ahmedlarbiofficial@gmail.com")
        self.assertEqual(newInvestor.phone, "0503733067")



    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/show/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_indexContent(self):
        tester = app.test_client(self)
        response = tester.get('/show/')
        self.assertEqual(response.content_type, "application/json")


    # def test_indexResponse(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/show/')
    #     print(response)


    def test_createPass(self):
        tester = app.test_client(self)
        response = tester.post('/create/ahmed/ahmedlarbi@gmail.com/0503733067')
        self.assertEqual(response.status_code,200)


    def test_deletePass(self):
        tester = app.test_client(self)
        response = tester.delete('/delete/ahmedlarbi2@gmail.com')
        self.assertEqual(response.status_code,400)

    def test_deleteFail(self):
        tester = app.test_client(self)
        response = tester.delete('/delete/ahmedlarbi2@gmail.com')
        self.assertNotEqual(response.status_code,200)

    def test_filter(self):
        tester = app.test_client(self)
        response = tester.get('/filter/email=ahmedlarbi@gmail.com')
        self.assertEqual(response.status_code,200)

    def test_modify(self):
        tester = app.test_client(self)
        response = tester.post('/modify/email=ahmedlarbi@gmail.com,name=ali')
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()