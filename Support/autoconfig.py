base_url = 'http://gmail.com'
timeout = 10

def_pass = 'Poiuty1!'
def_domain = '@gmail.com'

class Logins:
    def __init__(self, email, password, username=None, domain=None):
        self.email = email
        self.password = password
        self.username = username
        self.domain = domain

def_user = Logins('deftestmail199@gmail.com', def_pass, 'deftestmail199', def_domain)
sec_user = Logins('sectestmail81@gmail.com', def_pass, 'sectestmail81', def_domain)
third_user = Logins('thrdtestmail@gmail.com', def_pass, 'thrdtestmail', def_domain)
