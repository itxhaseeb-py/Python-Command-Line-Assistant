import os
import random

def command_help():
    print('''
    🔹 Available Commands:
  1. greet              → Greets you
  2. calculate          → Opens calculator
  3. save note          → Save a note
  4. read note          → Read all saved notes
  5. string tools       → String operations
  6. open folder        → Opens a folder
  7. show files         → Lists current directory files
  8. history            → Show command history
  9. game               → Play guessing game
 10. quit               → Exit the assistant
 11. command help       → Show all commands
 ''')

def calculate():
    q = int(input('Enter the 1st number: '))
    op = input('Enter the operation (+, -, *, %): ')
    w = int(input('Enter the 2nd number: '))
    if op == '+':
        print(f'Result: {q + w}')
    elif op == '-':
        print(f'Result: {q - w}')
    elif op == '*':
        print(f'Result: {q * w}')
    elif op == '%':
        print(f'Result: {q % w}')
    else:
        print('❌ Operation not found')

def save_note():
    note = input('Enter the note to save: ')
    with open('note.txt', 'a') as f:
        f.write(note + '\n')
    print('✅ Note saved to note.txt')

def read_note():
    try:
        with open('note.txt', 'r') as f:
            content = f.read()
            print('📄 Saved Notes:\n' + content)
    except FileNotFoundError:
        print('❌ Note not found.')

def string_tools():
    e = input('Enter the string: ')
    print('Length:', len(e))
    print('Uppercase:', e.upper())
    print('Lowercase:', e.lower())
    print('Reversed:', e[::-1])
    word = input('Enter the word to find: ')
    print('Found at index:', e.find(word))

def open_folder():
    path = input('Enter the folder path (like D:\\): ')
    if os.path.exists(path):
        try:
            os.startfile(path)
            print(f'📂 Folder opened: {path}')
        except Exception as e:
            print(f'❌ Could not open folder: {e}')
    else:
        print('⚠️ Path not found. Please check the folder path.')


def show_files():
    print('📁 Folder & files:')
    for ind, i in enumerate(os.listdir()):
        print(f'{ind}. {i}')

def game():
    number = random.randint(1, 10)
    try:
        your_guess = int(input('Enter the guess number (1–10): '))
        if your_guess == number:
            print('🎉 Good job! You are the winner.')
        else:
            print(f'😢 Sorry, the correct number was {number}. Try again!')
    except ValueError:
        print('❌ Invalid input. Please enter a number.')

command_history = []

if __name__ == '__main__':
    print('🤖 Welcome to Python Assistant, Silent Emperor!')
    command_help()

    while True:
        command = input('\nEnter command: ').lower()
        command_history.append(command)

        if command == 'greet':
            print("🙋‍♂️ Hello Silent Emperor! How can I serve you today?")
        elif command == 'calculate':
            calculate()
        elif command == 'save note':
            save_note()
        elif command == 'read note':
            read_note()
        elif command == 'string tools':
            string_tools()
        elif command == 'open folder':
            open_folder()
        elif command == 'show files':
            show_files()
        elif command == 'game':
            game()
        elif command == 'history':
            for cmd, t in enumerate(command_history):
                print(f'{cmd}. {t}')
        elif command == 'command help':
            command_help()
        elif command == 'quit':
            print('👋 Thank you for using me, Silent Emperor!')
            break
        else:
            print('❌ Sorry, command not found.')
