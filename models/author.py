class Author:
    def __init__(self, id, name):
        self.id = id
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) <= 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = value

    def articles(self, cursor):
        """Fetch all articles by the author."""
        query = """
        SELECT * FROM articles WHERE author_id = ?
        """
        cursor.execute(query, (self.id,))
        return cursor.fetchall()

    def magazines(self, cursor):
        """Fetch all unique magazines the author has contributed to."""
        query = """
        SELECT DISTINCT magazines.* FROM magazines
        JOIN articles ON magazines.id = articles.magazine_id
        WHERE articles.author_id = ?
        """
        cursor.execute(query, (self.id,))
        return cursor.fetchall()

    def __repr__(self):
        return f'<Author {self.name}>'