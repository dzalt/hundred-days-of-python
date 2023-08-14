from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):

    result = ""

    # difference between encrypt and decrypt is only + and -
    # (+ = shift forward, - = shift backward)
    # multiply shift with -1 to make it negative
    if direction == "decode":
        shift *= -1
    
    for letter in text:
        if letter in alphabet:
            start_pos = alphabet.index(letter)
            # result += alphabet[start_pos + shift] 
            # if shift pass through "z" it will produce a bug
            result += alphabet[(start_pos + shift) % 26]
        else:
            # this is for symbol
            result += letter

    print(f"Here's the {direction}d result: {result}")


print(logo)
is_end = False

while not is_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    if input("Type 'yes' to if you want to go again. Otherwise type 'no'.\n") == "no":
        print("Goodbye")
        is_end = True
