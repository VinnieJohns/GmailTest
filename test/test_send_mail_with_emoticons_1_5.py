import random

from Support import autoconfig
from page import EmptyPage, WelcomePage


class Test:

    subject = None

    def test_send_mail_with_emoticons(self, app):
        empty_page = EmptyPage.EmptyPage()
        login_page = empty_page.open_login_page()
        welcome_page = login_page.login(autoconfig.def_user.email, autoconfig.def_user.password)
        write_page = welcome_page.open_send_mail_page()
        emodji_count = random.randint(2, 6)
        subject = "test_emoticons" + str(random.randint(100, 999))
        self.subject = subject
        write_page.send_mail_with_emoticons(autoconfig.def_user.email, emodji_count, subject)
        mailbox_page = welcome_page.open_incoming_mail()
        mailbox_page.open_email_by_subject(subject)
        mailbox_page.verify_emodji_count(emodji_count)


    def teardown(self):
        welcome_page = WelcomePage.WelcomePage()
        welcome_page.logout()
