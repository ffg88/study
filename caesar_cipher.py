"""
Caesar's Cipher is a very simple encryption technique where the letter is replaced by another a fixed amount of positions
down the alphabet.
"""


def caesar(input_text, shift_amount, direction):
    output_text = ''
    if direction == 'decode':
        shift_amount = shift_amount * -1
    for letter in input_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > 25:
                new_position = new_position % 26
            elif new_position < 0:
                new_position += 26
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print(f'Your {action}d message is: {output_text}')


alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'x', 'w', 'y', 'z')

while True:
    action = input('Type "encode" to encrypt, or type "decode" to decrypt:\n').lower()
    if action == 'encode' or action == 'decode':
        text = input('Type your message:\n').lower()
        while True:
            shift = input('Type the shift number:\n')
            try:
                shift = int(shift)
                break
            except ValueError:
                print('Error: use only integers.\n')
        caesar(text, shift, action)
        break
    else:
        print('Error: invalid option.\n')
