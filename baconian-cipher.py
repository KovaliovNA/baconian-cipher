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


def message_cleanup(message):
    message_simbols = list(message)
    clean_message = ''

    for s in message_simbols:
        if s.isalpha():
            clean_message += s

    return clean_message


def decrypt(message):
    decipher = ''
    i = 0

    while True:
        if i < len(message) - 4:
            substr = message[i:i + 5]
            if substr[0] != ' ':
                decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
                i += 5

            else:
                decipher += ' '
                i += 1
        else:
            break

    return decipher


def letters_count(text):
    count = 0

    for letter in text:
        if letter.isalpha():
            count += 1

    return count


def hide_cipher(data, encrypted_message):
    if letters_count(data) >= letters_count(encrypted_message) + 5:

        list_data = list(data)
        list_encrypted_message = list(encrypted_message)

        iter_encr_mes = 0
        iter_data_from_file = 0

        while iter_encr_mes <= len(list_encrypted_message) - 1:

            if list_data[iter_data_from_file].isalpha():
                if list_encrypted_message[iter_encr_mes].isalpha():
                    if list_encrypted_message[iter_encr_mes].lower() == 'a':
                        list_data[iter_data_from_file] = list_data[iter_data_from_file].lower()
                    else:
                        list_data[iter_data_from_file] = list_data[iter_data_from_file].upper()
                iter_encr_mes += 1

            iter_data_from_file += 1

        number_of_last_letters = 0

        while number_of_last_letters != 5:
            if list_data[iter_data_from_file].isalpha():
                list_data[iter_data_from_file] = list_data[iter_data_from_file].upper()
                number_of_last_letters += 1

            iter_data_from_file += 1

        return ''.join(list_data)
    else:
        return None


def decrypt_message(data):
    end_of_message = 0
    encrypted_message = ""
    list_data = list(data)
    index = 0

    while end_of_message != 5:
        if list_data[index].isalpha():
            if list_data[index].islower():
                encrypted_message += "a"
                end_of_message = 0
            else:
                if list_data[index].isupper():
                    encrypted_message += "b"
                    end_of_message += 1
        index += 1

    print(encrypted_message)
    return decrypt(encrypted_message)


def main():
    while True:
        print("\n1) Encrypt")
        print("2) Decrypt")
        print("3) Exit\n")
        movement = input("Enter type of operation: ")
        if movement == "3":
            break
        else:
            if movement == "1":
                message = message_cleanup(input("\nEnter text that will be encrypted: "))

                path = input("\nEnter the path to txt files for encrypting: ")
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
                    data = myfile.read()
                    encrypted_data = hide_cipher(data, encrypt(message.upper()))

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
                    data = myfile.read()
                    decrypted_data = decrypt_message(data)

                    print("Decrypted message: \n" + decrypted_data)


def get_list_files(dir):
    if os.path.exists(dir):
        return os.listdir(dir.strip())

    return []


if __name__ == '__main__':
    main()
