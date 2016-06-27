__author__ = 'VinnieJohns'
from Support import helper
import WelcomePage

class LoginPage:

    username = '//input[@id="Email"]'
    next_btn = '//input[@id="next"]'
    password = '//input[@id="Passwd"]'
    sign_in_btn = '//input[@id="signIn"]'

    account_choser_link = '//a[@id="account-chooser-link"]'
    another_account_btn = '//li[@class="rwJTzb oTR3Cf"]//a[@id="account-chooser-add-account"]'

    def login(self, username, password):
        if not helper.is_element_present(self.username):
            self.choose_another_account()
        if not helper.is_element_visible('//span[@id="reauthEmail" and contains(., "%s")]' % username):
            helper.type(loc=self.username, text=username)
            helper.click(self.next_btn)
        helper.wait_for_element_visible(self.password)
        helper.type(loc=self.password, text=password)
        helper.click(self.sign_in_btn)
        return WelcomePage.WelcomePage()

    def choose_another_account(self):
        helper.wait_for_element_visible(self.account_choser_link)
        helper.click(self.account_choser_link)
        helper.wait_for_element_visible(self.another_account_btn)
        helper.click(self.another_account_btn)
        helper.wait_for_element_visible(self.username)