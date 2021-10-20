from kivymd.uix.snackbar import BaseSnackbar

from kivy.properties import StringProperty, NumericProperty

#
#
class CredententialsErrorSnackbar(BaseSnackbar):
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")
