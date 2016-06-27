# coding=utf-8
from Support import helper
import WriteMailPage, MailboxPage, SettingsPage


class WelcomePage():

    userpic_btn = '//a[@href="https://accounts.google.com/SignOutOptions?hl=ru&continue=https://mail.google.com/mail&service=mail"]'
    username = '//input[@id="Email"]'
    logout_btn = '//a[@id="gb_71"]'
    account_choser_link = '//a[@id="account-chooser-link"]'
    another_account_btn = '//li[@class="rwJTzb oTR3Cf"]//a[@id="account-chooser-add-account"]'

    write_mail_btn = '//div[@role="button" and @class="T-I J-J5-Ji T-I-KE L3"]'
    incoming_mail_btn = '//a[@href="https://mail.google.com/mail/#inbox"]'

    settings_menu_btn = '//div[@class="aos T-I-J3 J-J5-Ji"]'
    setings_menu_item = '//div[@id="ms"]//div[@class="J-N-Jz"]'
    settings_page = "https://mail.google.com/mail/#settings"

    def open_send_mail_page(self):
        helper.click(self.write_mail_btn)
        return WriteMailPage.WriteMailPage()

    def open_incoming_mail(self):
        helper.click(self.incoming_mail_btn)
        return MailboxPage.MailboxPage()

    def open_settings(self):
        helper.open(self.settings_page)
        return SettingsPage.SettingsPage()

    def logout(self):
        helper.click(self.userpic_btn)
        helper.wait_for_element_visible(self.logout_btn)
        helper.click(self.logout_btn)
        helper.get_alert()
        helper.wait_for_element_visible(self.account_choser_link)
        helper.click(self.account_choser_link)
        helper.wait_for_element_visible(self.another_account_btn)
        helper.click(self.another_account_btn)
        helper.wait_for_element_visible(self.username)

