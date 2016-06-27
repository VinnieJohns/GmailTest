from Support import autoconfig
from page import EmptyPage, WelcomePage


class Test:

    def incomplete_test_forwarding(self, app):
        empty_page = EmptyPage.EmptyPage()
        login_page = empty_page.open_login_page()
        welcome_page = login_page.login(autoconfig.sec_user.email, autoconfig.sec_user.password)
        settings_page = welcome_page.open_settings()
        settings_page.open_pop_imap_settings()
        forwarding_email = settings_page.generate_email_for_forwarding(autoconfig.third_user)
        settings_page.add_forwarding_mail(forwarding_email)
        welcome_page.open_incoming_mail()
        # unfortunately test is not complete yet...


    def teardown(self):
        welcome_page = WelcomePage.WelcomePage()
        welcome_page.logout()
