import json
import datetime
from utils import get_current_datetime

class Note:
    def __init__(self, note_id, title, body, created_at=None, updated_at=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at or get_current_datetime()
        self.updated_at = updated_at or get_current_datetime()

class NoteManager:
    def __init__(self):
        self.notes = []
        self.next_note_id = 1

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")

        note = Note(self.next_note_id, title, body)
        self.notes.append(note)
        self.next_note_id += 1

    def edit_note(self):
        note_id = int(input("Введите ID заметки для редактирования: "))
        note = self.find_note_by_id(note_id)

        if note:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note.title = title
            note.body = body
            note.updated_at = get_current_datetime()
            print("Заметка успешно отредактирована!")
        else:
            print("Заметка с таким ID не найдена.")

    def delete_note(self):
        note_id = int(input("Введите ID заметки для удаления: "))
        note = self.find_note_by_id(note_id)

        if note:
            self.notes.remove(note)
            print("Заметка успешно удалена!")
        else:
            print("Заметка с таким ID не найдена.")

    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def print_notes(self):
        for note in self.notes:
            print(f"ID: {note.note_id}")
            print(f"Заголовок: {note.title}")
            print(f"Текст: {note.body}")
            print(f"Дата создания: {note.created_at}")
            print(f"Дата изменения: {note.updated_at}")
            print("-" * 30)

    def save_notes_to_file(self, filename):
        data = []
        for note in self.notes:
            data.append({
                "note_id": note.note_id,
                "title": note.title,
                "body": note.body,
                "created_at": note.created_at,
                "updated_at": note.updated_at
            })

        with open(filename, "w") as file:
            json.dump(data, file)

    def load_notes_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    note = Note(
                        item["note_id"],
                        item["title"],
                        item["body"],
                        item["created_at"],
                        item["updated_at"]
                    )
                    self.notes.append(note)

        except FileNotFoundError:
            pass