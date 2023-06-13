from note import NoteManager
from utils import clear_console

def main():
    note_manager = NoteManager()

    while True:
        clear_console()
        print("Заметки:")
        note_manager.print_notes()

        print("\nМеню:")
        print("1. Создать новую заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            note_manager.create_note()
        elif choice == "2":
            note_manager.edit_note()
        elif choice == "3":
            note_manager.delete_note()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()