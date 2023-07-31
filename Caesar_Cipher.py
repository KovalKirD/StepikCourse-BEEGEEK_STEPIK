# Шифр Цезеря
# ASCII РУ 1040 - 1071(Прописные) 1072 - 1103(Строчные)
# MOSCH_EN = 26 мощность
# MOSCH_RU = 32 мощность

direction = int(input('Шифрование(1) или Дешифрование(2)?'))  # Направление 1/2
language = input('Русский(ru) или Английский(en)')            # Язык алфавита ru/en
shift_step = int(input('Шаг сдвига:'))                        # Шаг сдвига (со сдвигом вправо)
text = input('Текст:')                                        # Текст

if direction == 1:  # Шифрование y=(x+k)

    if language == 'en':  # Если Английский
        resalt_text = ''  # Зашифрованный текст
        for char in text:
            if char.isalpha():  # Если буква
                step = ord(char) + shift_step
                if (step > 122 and ord(char) > 96) or (step > 90 and ord(char) < 91):
                    step -= 26
                    resalt_text += chr(step)
                else:           # Если символ
                    resalt_text += chr(step)
            else:
                resalt_text += char
        print(resalt_text)

    if language == 'ru':  # Если Русский
        resalt_text = ''  # Зашифрованный текст
        for char in text:
            if char.isalpha():  # Если буква
                step = ord(char) + shift_step
                if (step > 1071 and ord(char) < 1072) or (step > 1103 and ord(char) < 1104):
                    step -= 32
                    resalt_text += chr(step)
                else:  # Если символ
                    resalt_text += chr(step)
            else:
                resalt_text += char
        print(resalt_text)

elif direction == 2:  # Дешифрование x=(y-k)

    if language == 'ru':  # Если Русский
        resalt_text = ''  # Дешифрованный текст
        for char in text:
            if char.isalpha():  # Если буква
                step = ord(char) - shift_step
                if (step < 1072 and ord(char) > 1071) or (step < 1040 and ord(char) < 1072):
                    step += 32
                    resalt_text += chr(step)
                else:           # Если символ
                    resalt_text += chr(step)
            else:
                resalt_text += char
        print(resalt_text)

    elif language == 'en':  # Если Английский

        resalt_text = ''  # Дешифрованный текст
        for char in text:
            if char.isalpha():  # Если буква
                step = ord(char) - shift_step
                if (step < 97 and ord(char) > 96) or (step < 65 and ord(char) > 64):
                    step += 26
                    resalt_text += chr(step)
                else:           # Если символ
                    resalt_text += chr(step)
            else:
                resalt_text += char
        print(resalt_text)