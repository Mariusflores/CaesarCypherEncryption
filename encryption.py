
file_to_encrypt = open("sample.txt", "r")
encrypted_file = open("encrypted.txt", "w")
file_text = file_to_encrypt.read()


sample = "Hello world"


def caesar_cypher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            char_code = ord(char)
            shifted_code = (char_code + shift - 65) % 26 + 65
            cipher_text += chr(shifted_code)
        else:
            cipher_text += char
    encrypted_file.write(cipher_text)


caesar_cypher(file_text, 4)
