from morse_code import morse
from functions import verify_text,program


text=input("Enter the text you want to convert into morse code: ").upper()
verify=verify_text(text,morse)
program(text,morse,verify)

