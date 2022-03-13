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

import json
import requests
import urllib3
from charset_normalizer import *
import idna
import PIL

from datetime import datetime

import kivy

kivy.require('2.0.0')



from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import *
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, ButtonBehavior
from kivymd.uix.toolbar import MDToolbar

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from helper_files import dbmodels as db
from helper_files.custom_widgets import CredententialsErrorSnackbar

#
# COLOR CONSTANTS

bg_alert = (1, 99/255, 71/255, 1)

# ==============================================================================
# CONSTANTS & CONNECTION STRINGS
# ==============================================================================
URL = "http://localhost:8000/api/"

Builder.load_file("kv_files/main.kv")
Builder.load_file("kv_files/signup.kv")
Builder.load_file("kv_files/login.kv")
Builder.load_file("kv_files/dashboard.kv")
Builder.load_file("kv_files/manage_profile.kv")
Builder.load_file("kv_files/custom_widgets.kv")


# ==============================================================================
# WELCOME SCREEN
# ==============================================================================
class WelcomeScreen(Screen):
    pass


# ==============================================================================
# SignUp SCREEN
# ==============================================================================
class SignUpScreen(Screen):

    def signup(self):
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
            self.manager.current = "dashboard"
        else:
            snackbar = CredententialsErrorSnackbar(
                bg_color = bg_alert,
                text = "Invalid Credentials. Please",
                snackbar_x = "10dp",
                snackbar_y = "10dp",
            )
            snackbar.size_hint_x = (Window.width - (snackbar.snackbar_x * 2)) / Window.width
            snackbar.size_hint_y = 0.2
            snackbar.open()
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
# MAIN TOOLBAR
# ==============================================================================
class MainToolbar(MDToolbar):
    def show_menu(self, *args, **kwargs):
        self.parent.parent.manager.current = "menulist"


# ==============================================================================
# PROFILE SCREEN
# ==============================================================================
class Profile(Screen):
    
    BLUR_COLOR = (255/255.0, 140/255.0, 0/255.0, 0.2)
    BLUR_TEXT_COLOR = (0, 0, 0, 1)
    
    ACTIVE_COLOR = (255/255.0, 140/255.0, 0/255.0, 1)
    ACTIVE_TEXT_COLOR = (1, 1, 1, 1)
    
    
    #
    #================================================================    
    def button_press(self):
        if self.ids.profile_tab.status:
            self.ids.profile_tab.background_color = self.BLUR_COLOR
            self.ids.profile_tab.color= self.BLUR_TEXT_COLOR
            
            self.ids.profile_gallery_tab.background_color = self.ACTIVE_COLOR
            self.ids.profile_gallery_tab.color = self.ACTIVE_TEXT_COLOR
            
        else:
            self.ids.profile_tab.background_color = self.ACTIVE_COLOR
            self.ids.profile_tab.color = self.ACTIVE_TEXT_COLOR
            
            self.ids.profile_gallery_tab.background_color = self.BLUR_COLOR
            self.ids.profile_gallery_tab.color = self.BLUR_TEXT_COLOR
            
        self.ids.profile_tab.status = not(self.ids.profile_tab.status)
        self.ids.profile_gallery_tab.status = not(self.ids.profile_tab.status)
        
    #
    #================================================================    
    def button_press2(self):
        if self.ids.profile_gallery_tab.status:
            self.ids.profile_gallery_tab.background_color = self.BLUR_COLOR
            self.ids.profile_gallery_tab.color = self.BLUR_TEXT_COLOR
            
            self.ids.profile_tab.background_color = self.ACTIVE_COLOR
            self.ids.profile_tab.color = self.ACTIVE_TEXT_COLOR
        else:
            self.ids.profile_gallery_tab.background_color = self.ACTIVE_COLOR
            self.ids.profile_gallery_tab.color = self.ACTIVE_TEXT_COLOR
            
            self.ids.profile_tab.background_color = self.BLUR_COLOR
            self.ids.profile_tab.color = self.BLUR_TEXT_COLOR
            
        self.ids.profile_gallery_tab.status = not(self.ids.profile_gallery_tab.status)
        self.ids.profile_tab.status = not(self.ids.profile_gallery_tab.status)
        
        


# ==============================================================================
# CSREEN MANAGER
# ==============================================================================
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
