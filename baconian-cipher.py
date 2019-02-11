import os

lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
          'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
          'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
          'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
          'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa',
          'Z': 'bbaab', '\n': 'bbbbb'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += lookup[letter]
        else:
            cipher += ' '

    return cipher


def decrypt(cipher):
    message = ''
    i = 0

    while i < len(cipher) - 4:
        substr = cipher[i:i + 5]
        if substr[0] != ' ':
            message += list(lookup.keys())[list(lookup.values()).index(substr)]
            i += 5
        else:
            message += ' '
            i += 1

    return message


def hide_cipher(text, encrypted_message):
    if letters_count(text) >= letters_count(encrypted_message) + 5:

        text_symbols = list(text)
        encr_message_symbols = list(encrypted_message)

        iter_encr_mes = 0
        iter_text = 0

        while iter_encr_mes < len(encr_message_symbols):

            if text_symbols[iter_text].isalpha():
                if encr_message_symbols[iter_encr_mes].isalpha():
                    if encr_message_symbols[iter_encr_mes].lower() == 'a':
                        text_symbols[iter_text] = text_symbols[iter_text].lower()
                    else:
                        text_symbols[iter_text] = text_symbols[iter_text].upper()
                iter_encr_mes += 1

            iter_text += 1

        number_of_last_letters = 0

        while number_of_last_letters != 5:
            if text_symbols[iter_text].isalpha():
                text_symbols[iter_text] = text_symbols[iter_text].upper()
                number_of_last_letters += 1

            iter_text += 1

        return ''.join(text_symbols)
    else:
        return None


def decrypt_message(text):
    end_of_message = 0
    encrypted_message = ""
    text_symbols = list(text)
    index = 0

    while end_of_message != 5:
        if text_symbols[index].isalpha():
            if text_symbols[index].islower():
                encrypted_message += "a"
                end_of_message = 0
            elif text_symbols[index].isupper():
                encrypted_message += "b"
                end_of_message += 1
        index += 1

    print(encrypted_message)
    return decrypt(encrypted_message)


def letters_count(text):
    count = 0

    for letter in text:
        if letter.isalpha():
            count += 1

    return count


def message_cleanup(message):
    message_simbols = list(message)
    clean_message = ''

    for s in message_simbols:
        if s.isalpha():
            clean_message += s

    return clean_message


def main():
    while True:
        print("\n1) Encrypt")
        print("2) Decrypt")
        print("3) Exit\n")
        movement = input("Enter type of operation: ")

        if movement == "3":
            break
        elif movement == "1":
            message = message_cleanup(input("\nEnter text that will be encrypted: "))

            path = input("\nEnter the path to txt files for encrypting (Such as ./input): ")
            if not path.endswith("/"):
                path += "/"
            arr = get_list_files(path)

            if len(arr) == 0:
                print("This path: " + path + " is empty or does not exist!")
                break

            print("\n")
            for el in arr:
                print(str(arr.index(el)) + ") " + el)

            index = int(input("\nSelect number of txt file: "))

            text_file = path + arr[index]
            with open(text_file, 'r') as myfile:
                text = myfile.read()
                encrypted_data = hide_cipher(text, encrypt(message.upper()))

                if not (encrypted_data is None):
                    if not os.path.exists("./output/"):
                        os.makedirs("./output/")

                    folder_of_output_file = "./output/" + arr[index]
                    with open(folder_of_output_file, 'w') as newFile:
                        newFile.write(encrypted_data)

                    print("\n\nSuccessful encrypt\n")
                    print("")
                else:
                    print("\nSomething wrong\n")
        else:
            arr = os.listdir("./output/")
            index = 0

            print("\n")
            for el in arr:
                print(str(index) + ") " + el)
                index += 1

            index = int(input("\nSelect number of txt file: "))

            text_file = "./output/" + arr[index]
            with open(text_file, 'r') as myfile:
                text = myfile.read()
                decrypted_data = decrypt_message(text)

                print("Decrypted message: \n" + decrypted_data)


def get_list_files(dir):
    if os.path.exists(dir):
        return os.listdir(dir.strip())

    return []


if __name__ == '__main__':
    main()
