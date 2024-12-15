class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def create_author(cursor, name):
        """Create an author and return the ID."""
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        return cursor.lastrowid

    def __repr__(self):
        return f'<Author {self.name}>'
