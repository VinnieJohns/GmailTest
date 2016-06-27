import random

from Support import autoconfig
from page import EmptyPage, WelcomePage


class Test:

    def setup(self):
        empty_page = EmptyPage.EmptyPage()
        empty_page.delete_big_file()
        empty_page.create_big_file()
        login_page = empty_page.open_login_page()
        login_page.login(autoconfig.def_user.email, autoconfig.def_user.password)


    def test_send_mail_big_attach(self, app):
        welcome_page = WelcomePage.WelcomePage()
        mail_page = welcome_page.open_send_mail_page()
        subject = "test_big_attach" + str(random.randint(100, 999))
        mail_page.send_mail_with_big_attach(autoconfig.def_user.email, subject)


    def teardown(self):
        empty_page = EmptyPage.EmptyPage()
        empty_page.delete_big_file()
        welcome_page = WelcomePage.WelcomePage()
        welcome_page.logout()
