# to change the kivy default settings
# we use this module config
from kivy.config import Config

# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', '0')

# fix the width of the window
Config.set('graphics', 'width', '540')

# fix the height of the window
Config.set('graphics', 'height', '960')

import kivy

kivy.require('2.0.0')

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import *
from kivy.core.window import Window

import json
import requests
import urllib3
from charset_normalizer import *
import idna
import PIL
from helper_files import dbmodels as db
from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from kivymd.uix.snackbar import Snackbar


# ==============================================================================
# CONSTANTS & CONNECTION STRINGS
# ==============================================================================
URL = "http://localhost:8000/api/"

Builder.load_file("kv_files/main.kv")
Builder.load_file("kv_files/signup.kv")
Builder.load_file("kv_files/login.kv")
Builder.load_file("kv_files/dashboard.kv")
Builder.load_file("kv_files/manage_profile.kv")


# ==============================================================================
# WELCOME SCREEN
# ==============================================================================
class WelcomeScreen(Screen):
    pass

# ==============================================================================
# SignUp SCREEN
# ==============================================================================
class SignUpScreen(Screen):

    def signup():
        email = self.ids.email.text
        password = self.ids.passwd.text
        first_name = self.ids.first_name.text


# ==============================================================================
# LOGIN SCREEN
# ==============================================================================
class LoginScreen(Screen):
    #
    # Check authorization/credentials by connecting to the API Endpoint
    def check_login(self):
        """
        username = self.ids.username.text
        password = self.ids.passwd.text

        payload = {'username': username, 'password': password}
        req = requests.post(URL+"check_login", data=payload)
        data = json.loads(req.text)

        if data["ret"]:
            try:
                result = db.session.query(db.User).one()

                payload = {'user_id': result.id, 'email': result.email, 'first_name': result.first_name, 'last_name':result.last_name}
                req = requests.post(URL+"update_profile_details", data=payload)
                ret_data = json.loads(req.text)

                if ret_data["ret"]:
                    print("Data is updated")
                else:
                    print("try later")

            except NoResultFound:
                obj = db.User(
                    id = data["user_id"],
                    username = data["username"],
                    first_name = data["first_name"],
                    last_name = data["last_name"],
                    email = data["email"],
                    logged_on = datetime.now(),
                    is_online = True,
                )
                db.session.add(obj)
                db.session.commit()

        print(username, password)
        """
        self.manager.current = "dashboard"

# ==============================================================================
# MENU SCREEN
# ==============================================================================
class MenuScreen(Screen):
    pass


# ==============================================================================
# DASHBOARD SCREEN
# ==============================================================================
class Dashboard(Screen):
    pass


# ==============================================================================
# DASHBOARD SCREEN
# ==============================================================================
class Profile(Screen):
    pass


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

# ==============================================================================
# Main APP
# ==============================================================================
class OnlineDental(MDApp, Screen):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return ScreenManagement()

    def show_menu(self, *args, **kwargs):
        self.root.current = "menulist"

    def logout(self):
        try:
            result = db.session.query(db.User).one()
            db.session.query(db.User).filter(db.User.id == result.id).update({'is_online': False, 'logged_on':None})
            db.session.commit()
        except NoResultFound:
            pass
        self.root.current = "login"


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == '__main__':
    # Create database tables in the local system to store data for the app
    db.create_db()

    # run the application
    OnlineDental().run()