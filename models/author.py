class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create(cursor, name):
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        return cursor.lastrowid

    @staticmethod
    def update(cursor, author_id, name):
        cursor.execute('UPDATE authors SET name = ? WHERE id = ?', (name, author_id))

    @staticmethod
    def delete(cursor, author_id):
        cursor.execute('DELETE FROM authors WHERE id = ?', (author_id,))

    def __repr__(self):
        return f'<Author {self.name}>'
