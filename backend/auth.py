import ldap3
import re

def check_login(login, password):
    if not re.match("^[\.\w-]*$", login):
        return False
    try:
        conn = ldap3.Connection("ldaps://ldap-may.l.postgrespro.ru:636", "cn=%s,dc=postgrespro,dc=ru" % (login), password)
        conn.open()
        return conn.bind()
    except:
        return False

if __name__ == "__main__":
    pass
