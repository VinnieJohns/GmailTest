from Support import helper

class MailboxPage():

    a = '//tr//span[@email=""]'
    emodji_in_mail_body = '//div[@dir="ltr"]//img[@goomoji]'
    delete_btn = '//div[@class="aeH"]//div[@act="10"]'
    checkbox = '//div[@role="checkbox"]//div[@class="T-Jo-auh"]'
    checked_checkbox = '//div[@role="checkbox" and @aria-checked="true"]//div[@class="T-Jo-auh"]'

    email_menu = '//div[@class="T-I J-J5-Ji T-I-Js-Gs aap T-I-awG T-I-ax7 L3"]'
    delete_mail_menu_item = '//div[@id="tm"]'

    def open_email_by_subject(self, subject):
        loc = '//span[contains(., "%s")]' % subject
        helper.wait_for_element_visible(loc)
        helper.click(loc)
        helper.wait_for_element_visible('//h2[contains(., "%s")]' % subject)
        print "Here!!!"

    def open_email_menu(self):
        helper.click(self.email_menu)
        helper.wait_for_element_visible(self.delete_mail_menu_item)

    def verify_emodji_count(self, count):
        assert len(helper.find_elements(self.emodji_in_mail_body)) == count

    def delete_mail_by_checkbox_by_subject(self, subject):
        self.open_email_by_subject(subject)
        self.open_email_menu()
        helper.click(self.delete_mail_menu_item)
        helper.wait_for_element_present(self.delete_btn)
        helper.click(self.delete_btn)
        helper.wait_for_element_not_visible('//span[contains(., "%s")]' % subject)




