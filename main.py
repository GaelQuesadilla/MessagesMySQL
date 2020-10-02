import pymysql as sql
import time


class DataBase:
    def __init__(self, db):
        self.db = db

        self.conection = sql.connect(
            host="bgdw8pqbnrolcqwdgor0-mysql.services.clever-cloud.com",
            user="u8lkyccigwbsm4ss",
            password="6vJrSIB1M8Vvd15jSmM3",
            db=self.db
        )
        self.cursor = self.conection.cursor()

    def GetChannel(self, channel_search):
        self.conection.connect()
        self.cursor = self.conection.cursor()
        self.cursor.execute(f"SELECT * FROM channels WHERE c_name = '{channel_search}';")
        channel_info = self.cursor.fetchall()
        self.cursor.close()
        self.conection.close()
        return str(channel_info)

    def GetAllMessages(self, name_channel):
        self.conection.connect()
        self.cursor = self.conection.cursor()
        self.cursor.execute(f"SELECT * FROM {name_channel} ORDER BY message_id DESC LIMIT 25;")
        all_messages = self.cursor.fetchall()
        self.cursor.close()
        self.conection.close()
        return all_messages


database = DataBase("bgdw8pqbnrolcqwdgor0")

password_correct = False
connect = False
while not connect:
    channel_input = input("\n>A que canal deseas unirte: ")

    try:
        channel = database.GetChannel(channel_input)
        channel = channel[1: -2]
        channel_info = eval(channel)

    except Exception as e:
        print("Ha ocurrido un error")
        channel_info = ("", "")
        print(e)

    if channel_info[1] == "":
        print("Intenta de nuevo")

    else:
        while not password_correct:
            print("Escribe la contraseña")
            password_input = input()
            if password_input == channel_info[2]:
                connect = True
                password_correct = True

print("Has accedido :D")
message_a = database.GetAllMessages(channel_info[3])
for m in range(0, len(message_a)):
    message_p = message_a[-m - 1]
    print(f"{message_p[0]}|| {message_p[1]} -- {message_p[2]}")


while True:
    time.sleep(7)

