class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self._title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = value

    def create_article(cursor, title, content, author_id, magazine_id):
        """Create an article and return the ID."""
        cursor.execute(
        'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
        (title, content, author_id, magazine_id)
        )
        return cursor.lastrowid

    def __repr__(self):
        return f'<Article {self.title}>'
