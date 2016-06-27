from Support import helper
import subprocess
import sys

class WriteMailPage():

    to_input = '//textarea[@name="to"]'
    subjectbox = '//input[@name="subjectbox"]'
    paperclip_icon = '//div[@id=":ye"]'
    emoticons_icon = '//div[@id=":q9"]'
    emoticon = '//div[@class="a8I"]//div[@style=""]//button[@class="a8m"]'
    mail_text = '//div[@class="Am Al editable LW-avf"]'
    emodji_in_mail_text = mail_text + '//img[@goomoji]'
    send_mail_btn = '//div[@id=":nw"]'

    attach_file = '//div[@class="wG J-Z-I"]'
    alert_cancel = '//div[@role="alertdialog"]//button[@name="cancel"]'

    def send_mail_with_emoticons(self, address, emodji_count, subject=None):
        self.type_address(address)
        if subject is not None:
            self.type_subject(subject)
        self.choose_emoticons(emodji_count)
        self.press_send()

    def type_address(self, address):
        helper.type(self.to_input, address)

    def type_subject(self, subject):
        helper.type(self.subjectbox, subject)

    def press_attach_file(self):
        helper.click(self.attach_file)

    def open_emoticons_menu(self):
        helper.send_keys_for_open_emodji(self.subjectbox)
        helper.wait_for_element_visible(self.emoticon)

    def choose_emoticons(self, count):
        self.open_emoticons_menu()
        for i in range(count):
            helper.click(self.emoticon)
        assert len(helper.find_elements(self.emodji_in_mail_text)) == count

    def press_send(self):
        helper.send_keys_for_send_mail(self.subjectbox)
        helper.wait_for_element_not_visible(self.send_mail_btn)

    def send_mail_with_big_attach(self, address, subject=None):
        self.type_address(address)
        if subject is not None:
            self.type_subject(subject)
        self.press_attach_file()
        command = str(sys.path[0] + '\\test\\data\\file_uploader.exe %s' % str(sys.path[0] + '\\test\\data\\test_data'))
        try:
            subprocess.check_output(command)
        except:
            return
        helper.wait_for_element_visible(self.alert_cancel)
        helper.click(self.alert_cancel)
        helper.wait_for_element_not_visible(self.alert_cancel)



