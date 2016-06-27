from Support import helper


class SettingsPage():

    add_forwarding_address = '//input[@act="add"]'
    new_forwarding_address_dialog = '//div[@role="alertdialog"]'
    new_forwarding_address_input = new_forwarding_address_dialog + '//input[@type="text"]'
    new_forwarding_address_confirm = new_forwarding_address_dialog + '//button[@name="next"]'

    submit_new_address = '//input[@type="submit"]'
    confirm_submitting_new_address = '//button[@name="ok"]'

    settings_pop_imap = '//a[@href="https://mail.google.com/mail/#settings/fwdandpop"]'

    def open_pop_imap_settings(self):
        helper.wait_for_element_visible(self.settings_pop_imap)
        helper.click(self.settings_pop_imap)

    def add_forwarding_mail(self, email):
        helper.wait_for_element_visible(self.add_forwarding_address)
        helper.click(self.add_forwarding_address)
        helper.wait_for_element_visible(self.new_forwarding_address_input)
        helper.type(self.new_forwarding_address_input, email)
        helper.click(self.new_forwarding_address_confirm)
        helper.wait_for_element_not_visible(self.new_forwarding_address_dialog)
        helper.select_window(1)
        helper.click(self.submit_new_address)
        helper.select_window(0)
        helper.click('//button[@name="ok"]')

    def generate_email_for_forwarding(self, user):
        nickname_salt = helper.random_string(6)
        email = user.username + '+' + nickname_salt + user.domain
        return email






