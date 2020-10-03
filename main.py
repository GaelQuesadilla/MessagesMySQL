import pymysql as sql
import time

channel_info = ("Error", "Este es un mensaje de error" "", "")


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

    def OpenConection(self):
        self.conection.connect()
        self.cursor = self.conection.cursor()

    def CloseConnection(self):
        self.cursor.close()
        self.conection.close()

    def GetChannel(self, channel_search):
        self.cursor.execute(f"SELECT * FROM channels WHERE c_name = '{channel_search}';")
        channel_data = self.cursor.fetchall()
        return str(channel_data)

    def GetMessages(self, name_channel, message_limit):
        self.cursor.execute(f"SELECT * FROM {name_channel} ORDER BY message_id DESC LIMIT {message_limit};")
        all_messages = self.cursor.fetchall()
        return all_messages

    def LastMessage(self, name_channel):
        self.cursor.execute(f"Select message_id FROM {name_channel} ORDER BY message_id DESC LIMIT 1;")
        last_message = self.cursor.fetchone()
        return last_message


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
message_a = database.GetMessages(channel_info[3], 25)
for m in range(0, len(message_a)):
    message_p = message_a[-m - 1]
    print(f"{message_p[0]}|| {message_p[1]} -- {message_p[2]}")

database.CloseConnection()

message_l = int(message_a[0][0])

while True:

    time.sleep(7)

    database.OpenConection()
    message_l2 = int(database.LastMessage(channel_info[3])[0])
    if message_l != message_l2:
        limit = message_l2 - message_l
        message_s = database.GetMessages(channel_info[3], limit)

        for m in range(0, len(message_s)):
            message_p = message_s[-m - 1]
            print(f"{message_p[0]}|| {message_p[1]} -- {message_p[2]}")

        message_l = message_l2

    database.CloseConnection()
