values_str = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
              "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x" "y", "z",
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

create_values = "(message_id INT(5) NOT NULL AUTO_INCREMENT," \
                " message_author VARCHAR(15) NOT NULL," \
                " message_content VARCHAR(40) NOT NULL," \
                " message_color VARCHAR(10) NOT NULL," \
                " PRIMARY KEY (message_id));"

auto_inserter = "(message_author, message_content, message_color)" \
                "VALUES('ADMI', '==Chat creado==', 'Yellow');"

