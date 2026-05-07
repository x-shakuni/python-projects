print("""
                                         _       _  
                                        (_)     | |      
  ___ __ _  ___  ___  __ _ _ __      ___ _ _ __ | |__   ___ _ __ 
 / __/ _` |/ _ \\/ __|/ _` | '__|    / __| | '_ \\| '_ \\ / _ \\ '__|
| (_| (_| |  __/\\__ \\ (_| | |      | (__| | |_) | | | |  __/ |   
 \\___\\__,_|\\___||___/\\__,_|_|       \\___|_| .__/|_| |_|\\___|_|     
                                          | |
                                          |_|        
""")
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' or 'decode' to encode/decode letters: ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")