import pymysql
from crawling import REALTIME

class DB_HELPER():
    def __init__(self, host = '13.209.6.72', user = 'test', passwd = 'qkqhdi12', db = 'testdb'):
        self.connection = pymysql.connect(
            host = host,
            user = user,
            passwd = passwd,
            db= db,
            charset = 'utf8'
        )
        self.data = REALTIME()


    def read_tables(self, dbname='testdb', table_name = 'soo2'):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM {};".format(table_name)
        cursor.execute(sql)
        result = cursor.fetchall()

        return result
    
    def update_tables(self, dbname='testdb', table_name = 'news'):

        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM soo2;"
        cursor.execute(sql)

        sql = "INSERT INTO soo2 (rt_rank, trend) Values (%s, %s)"
        val = [(int(key), value) for key, value in self.data()]

        cursor.executemany(sql, val)


a = REALTIME()
val = [(int(key), value) for key, value in a()]
val
k = DB_HELPER()
k.update_tables()
k.read_tables() 

sql = 'INSERT INTO soo2(rt_rank, trend) VALUES (1, "박시연")'
val = (1, '박시연')
cursor.execute(sql)

