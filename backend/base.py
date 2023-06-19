import psycopg2
import psycopg2.extras


class Model:
    def __init__(self):
        self.connection = psycopg2.connect("host=127.0.0.1 dbname=postgres user=komii")
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def keys_get(self):
        self.cursor.execute("SELECT id, name, pub_key FROM keys")
        return self.cursor.fetchall()
    
    def keys_add(self, name, key, pub_key):
        self.cursor.execute("INSERT INTO keys (name, key, pub_key) VALUES (%s, %s, %s)",
                                (name, key, pub_key)
                            )
        self.connection.commit()

    def keys_delete(self, id):
        self.cursor.execute("DELETE FROM keys WHERE id = %s",
                                (str(id))
                            )
        self.connection.commit()



    def scripts_get(self):
        self.cursor.execute("SELECT id, name, script FROM scripts")
        return self.cursor.fetchall()
    
    def scripts_add(self, name, script, user_login):
        self.cursor.execute("INSERT INTO scripts (name, script, user_login) VALUES (%s, %s, %s)",
                                (name, script, user_login)
                            )
        self.connection.commit()

    def scripts_delete(self, id):
        self.cursor.execute("DELETE FROM scripts WHERE id = %s",
                                (str(id))
                            )
        self.connection.commit()



    def servers_get(self):
        self.cursor.execute("SELECT servers.id, servers.name, servers.host, servers.port, servers.user_login FROM servers")
        return self.cursor.fetchall()
    
    def servers_get_with_key(self):
        self.cursor.execute("SELECT server.id, server.name, server.host, server.port, server.user_login, server.key_id, keys.key, keys.pub_key, server.script_id, scripts.script FROM servers JOIN keys ON key_id = keys.id JOIN scripts ON script_id = scripts.id")
        return self.cursor.fetchall()
    
    def servers_add(self, name, host, port, user_login, key_id, script_id):
        self.cursor.execute("INSERT INTO servers (name, host, port, user_login, key_id, script_id) VALUES (%s, %s, %s, %s, %s, %s)",
                                (name, host, str(port), user_login, str(key_id), str(script_id))
                            )
        self.connection.commit()

    def servers_delete(self, id):
        self.cursor.execute("DELETE FROM servers WHERE id = %s",
                                (str(id))
                            )
        self.connection.commit()

if __name__ == "__main__":
    pass

