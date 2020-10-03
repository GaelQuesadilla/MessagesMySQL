import vars_values as val
import time
import os


class Datamessage(val.DataBaseConection):

    def GetUser(self, user_search):
        self.cursor.execute(f"SELECT * FROM users WHERE user_name = '{user_search}';")
        channel_data = self.cursor.fetchall()
        return str(channel_data)

    def CreateUser(self, name, password, color):
        self.cursor.execute(f"INSERT INTO users(user_name, user_password, user_color)VALUES('{name}', '{password}', '{color}');")
        self.conection.commit()

    def GetChannel(self, channel_search):
        self.cursor.execute(f"SELECT * FROM channels WHERE c_name = '{channel_search}';")
        channel_data = self.cursor.fetchall()
        return str(channel_data)

    def WriteMessage(self, channel_i,  author, content, color):
        self.cursor.execute(f"INSERT INTO {channel_i}(message_author, message_content, message_color)"
                            f"VALUES('{author}', '{content}', '{color}');")


database = Datamessage(val.database_name)

user_password_correct = False
user = True
user_init = True
color_correct = False
validate_count = False

while user:
    while user_init:
        user_input = input("\n>Cual es tu nombre             Escribe 'c' para crear una cuenta\n")
        user_init = False

        if user_input == "c":
            os.system("cls")
            while not validate_count:
                u_name_input = input("\nCual será el nombre de la cuenta: ")
                u_password_input = input("\nCual sera su contraseña: ")
                count_name = len(u_name_input)
                count_password = len(u_password_input)
                if count_name <= 15 and count_password <= 15:
                    validate_count = True
                else:
                    print("Muy largo, la cantidad mayor de caracteres es 15")

            print("\x1b[1;31m" + "\nRed", end="")
            print("\x1b[1;32m" + "   Green", end="")
            print("\x1b[1;33m" + "   Yellow", end="\n")
            print("\x1b[1;34m" + "Blue", end="")
            print("\x1b[1;35m" + "  Purple", end="")
            print("\x1b[1;37m" + "  Withe", end="")
            print("\x1b[;37m" + "", end="\n")

            while not color_correct:
                u_color_input = input("Escoje un color : ")
                if u_color_input == "Red" or u_color_input == "Green" or u_color_input == "Yellow":
                    color_correct = True

                elif u_color_input == "Blue" or u_color_input == "Purple" or u_color_input == "Withe":
                    color_correct = True

            command = True

            try:
                validate = database.GetUser(u_name_input)
                if validate_count != "()":
                    database.CreateUser(u_name_input, u_password_input, u_color_input)
                    print("Cuenta creada con exito")

            except Exception as e:
                print("Un error ha ocurrido")
                print(e)

        else:
            command = False

    try:
        user = database.GetUser(user_input)
        user = user[1: -2]
        user_info = eval(user)

    except Exception as e:
        print("Ha ocurrido un error")
        print(e)
        command = True
        user_info = ("", "")

    if user_info[1] == "":
        print("Intenta de nuevo")
        command = True

    else:
        while not user_password_correct:
            print("Escribe la contraseña")
            password_input = input()
            if password_input == user_info[2]:
                user = False
                user_password_correct = True

print("Has accedido a tu cuenta :D")


password_correct = False
connect = False
while not connect:

    channel_input = input("\n>A que canal deseas unirte")

    try:
        channel = database.GetChannel(channel_input)
        channel = channel[1: -2]
        channel_info = eval(channel)

    except Exception as e:
        print("Ha ocurrido un error")
        print(e)
        command = True
        channel_info = ("", "")

    if channel_info[1] == "":
        pass

    else:
        while not password_correct:
            print("Escribe la contraseña")
            password_input = input()
            if password_input == channel_info[2]:
                connect = True
                password_correct = True

                database.CloseConnection()

notification = "Has accedido al canal, ya puedes enviar mensajes"
u_color = val.colors(user_info[3])

while True:
    print("\x1b[;37m" + f"{notification}")
    print("======================================")
    print(u_color + f"{user_info[1]}:")
    message_input = input("")
    if len(message_input) > 40:
        os.system("cls")
        notification = "Escribiste un mensaje con mas de 40 cifras"
    elif len(message_input) == 0:
        os.system("cls")
        notification = "Enviaste un mensaje vacio"
    else:
        try:
            os.system("cls")
            database.OpenConection()
            database.WriteMessage(channel_info[3], user_input, message_input, user_info[3])

            database.CloseConnection()
            notification = "Mensaje enviado"

        except Exception as e:
            notification = e
            os.system("cls")
