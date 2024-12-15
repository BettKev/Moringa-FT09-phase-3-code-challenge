class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @staticmethod
    def create(cursor, title, content, author_id, magazine_id):
        cursor.execute(
            'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
            (title, content, author_id, magazine_id)
        )
        return cursor.lastrowid

    @staticmethod
    def update(cursor, article_id, title, content, author_id, magazine_id):
        cursor.execute(
            'UPDATE articles SET title = ?, content = ?, author_id = ?, magazine_id = ? WHERE id = ?',
            (title, content, author_id, magazine_id, article_id)
        )

    @staticmethod
    def delete(cursor, article_id):
        cursor.execute('DELETE FROM articles WHERE id = ?', (article_id,))

    def __repr__(self):
        return f'<Article {self.title}>'
