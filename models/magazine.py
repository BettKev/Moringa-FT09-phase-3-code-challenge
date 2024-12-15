class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) <= 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def create_magazine(cursor, name, category):
        """Create a magazine and return the ID."""
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (name, category))
        return cursor.lastrowid

    def __repr__(self):
        return f'<Magazine {self.name}>'
