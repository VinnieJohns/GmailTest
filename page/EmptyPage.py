import subprocess
import sys

import LoginPage
import os.path
from Support import helper, autoconfig


class EmptyPage:

    def open_login_page(self):
        helper.open(autoconfig.base_url)
        return LoginPage.LoginPage()

    def create_big_file(self):
        command = "fsutil file createnew %stest_data 26214401" % str(sys.path[0] + '\\test\\data\\')
        try:
            subprocess.check_output(command)
        except:
            return

    def delete_big_file(self):
        file = str(sys.path[0] + '\\test\\data\\') + "test_data"
        try:
            os.remove(file)
        except:
            return
