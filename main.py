import time
import random
import vars_values as val
import os


def choice():
    return random.choice(val.values_str)


class DataBase(val.DataBaseConection):

    def CreateChannel(self, name, password):
        c_key = f"{choice()}{choice()}{choice()}{choice()}{choice()}"

        self.cursor.execute(f"INSERT INTO channels(c_name, c_password, c_key) VALUES('{name}', '{password}', '{c_key}');")
        self.conection.commit()

        self.cursor.execute(f"CREATE TABLE {c_key} {val.create_values}")
        self.conection.commit()

        print("Chat creado exitosamente")

        self.cursor.execute(f"INSERT INTO {c_key} {val.auto_inserter}")
        self.conection.commit()

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


database = DataBase(val.database_name)

channel_info = ("", "")
password_correct = False
connect = False
command = True
validate_count = False

while not connect:
    while command:
        channel_input = input("\n>A que canal deseas unirte             Escribe 'c' para crear un canal\n")
        if channel_input == "c":
            os.system("cls")
            while not validate_count:
                c_name_input = input("\nCual será el nombre del canal: ")
                c_password_input = input("\nCual sera su contraseña: ")
                count_name = len(c_name_input)
                count_password = len(c_password_input)
                if count_name <= 15 and count_password <= 15:
                    validate_count = True
                else:
                    print("Muy largo, la cantidad mayor de caracteres es 15")

                command = True

            try:
                validate = database.GetChannel(c_name_input)
                if validate == "()":
                    database.CreateChannel(c_name_input, c_password_input)
                else:
                    print("El canal ya existe")

            except Exception as e:
                print("Un error ha ocurrido")
                print(e)

        else:
            command = False

    try:
        channel = database.GetChannel(channel_input)
        channel = channel[1: -2]
        channel_info = eval(channel)

    except Exception as e:
        print("Ha ocurrido un error")
        print(e)
        command = True

    if channel_info[1] == "":
        print("Intenta de nuevo")
        command = True

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
    print(val.colors(message_p[3]) + f"{message_p[0]}|| {message_p[1]} -- {message_p[2]}")

database.CloseConnection()

message_l = int(message_a[0][0])

while True:

    time.sleep(3)

    database.OpenConection()
    message_l2 = int(database.LastMessage(channel_info[3])[0])
    if message_l != message_l2:
        limit = message_l2 - message_l
        message_s = database.GetMessages(channel_info[3], limit)

        for m in range(0, len(message_s)):
            message_p = message_s[-m - 1]
            print(val.colors(message_p[3]) + f"{message_p[0]}|| {message_p[1]} -- {message_p[2]}")

        message_l = message_l2

    database.CloseConnection()
