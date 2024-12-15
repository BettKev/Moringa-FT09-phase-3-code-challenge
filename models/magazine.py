class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

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

    def articles(self, cursor):
        """Fetch all articles in this magazine."""
        query = "SELECT * FROM articles WHERE magazine_id = ?"
        cursor.execute(query, (self.id,))
        return cursor.fetchall()
    
    def contributors(self, cursor):
        """Fetch all unique authors who have contributed to this magazine."""
        query = """
        SELECT DISTINCT authors.* FROM authors
        JOIN articles ON authors.id = articles.author_id
        WHERE articles.magazine_id = ?
        """
        cursor.execute(query, (self.id,))
        return cursor.fetchall()

    def article_titles(self, cursor):
        """Fetch all article titles for this magazine."""
        query = "SELECT title FROM articles WHERE magazine_id = ?"
        cursor.execute(query, (self.id,))
        return [row['title'] for row in cursor.fetchall()]

    def contributing_authors(self, cursor):
        """Fetch authors with more than 2 articles in this magazine."""
        query = """
        SELECT authors.* FROM authors
        JOIN articles ON authors.id = articles.author_id
        WHERE articles.magazine_id = ?
        GROUP BY authors.id
        HAVING COUNT(articles.id) > 2
        """
        cursor.execute(query, (self.id,))
        return cursor.fetchall()

    def __repr__(self):
        return f'<Magazine {self.name}>'