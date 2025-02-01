import pymysql

def db_connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="9959730693@Gm",
        database="voting_system"
    )