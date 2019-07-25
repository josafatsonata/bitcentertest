import os
import sys


class Properties:

    URL = "https://bitwebsite-frontend-dev.herokuapp.com/"

    @staticmethod
    def select_driver():
        platforms = {
            'linux': '/chromedriverlinux',
            'linux1': '/chromedriverlinux',
            'linux2': '/chromedriverlinux',
            'darwin': '/chromedriverMac',
            'win32': '\\chromedriver.exe'
        }
        if sys.platform not in platforms:
            return sys.platform

        return os.path.dirname(os.path.abspath(__file__)) + platforms[sys.platform]
