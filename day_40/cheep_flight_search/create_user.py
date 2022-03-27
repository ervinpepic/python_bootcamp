from urllib import response
import requests


SHEETY_API = ""
class CreateUser:
    def create_user(self):
        params = {
            "user": {
                "firstName": input("Enter your name: "),
                "lastName": input("Enter your last name: "),
                "email": input("Enter your email: "),
                "email_check": input("Enter your email again: "),
            }
        }
        if params['user']['email'] == params['user']['email_check']:
            requests.post(url=SHEETY_API, json=params)
            print("Welcome to the club")
        else:
            print("Your email does not matches")
