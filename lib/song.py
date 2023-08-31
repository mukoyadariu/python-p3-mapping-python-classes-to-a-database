from lib.config import CURSOR

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album
        self.id = None  # Assign an ID when saved to the database

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        ''')

    def save(self):
        CURSOR.execute('''
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        ''', (self.name, self.album))
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
