class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @staticmethod
    def create(cursor, name, category):
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        return cursor.lastrowid

    @staticmethod
    def update(cursor, magazine_id, name, category):
        cursor.execute('UPDATE magazines SET name = ?, category = ? WHERE id = ?', (name, category, magazine_id))

    @staticmethod
    def delete(cursor, magazine_id):
        cursor.execute('DELETE FROM magazines WHERE id = ?', (magazine_id,))

    def __repr__(self):
        return f'<Magazine {self.name}>'
