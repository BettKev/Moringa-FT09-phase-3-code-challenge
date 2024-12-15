from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine







def display_records(cursor):
    """Fetch and display all records from the database."""
    print("\nMagazines:")
    cursor.execute('SELECT * FROM magazines')
    for record in cursor.fetchall():
        print(Magazine(record["id"], record["name"], record["category"]))

    print("\nAuthors:")
    cursor.execute('SELECT * FROM authors')
    for record in cursor.fetchall():
        print(Author(record["id"], record["name"]))

    print("\nArticles:")
    cursor.execute('SELECT * FROM articles')
    for record in cursor.fetchall():
        print(Article(record["id"], record["title"], record["content"], record["author_id"], record["magazine_id"]))

def main():
    # Initialize the database
    create_tables()

    # Collect user input with validation
    author_name = input("Enter author's name: ").strip()
    if not author_name:
        print("Author's name cannot be empty.")
        return

    magazine_name = input("Enter magazine name: ").strip()
    magazine_category = input("Enter magazine category: ").strip()
    if not magazine_name or not magazine_category:
        print("Magazine name and category cannot be empty.")
        return

    article_title = input("Enter article title: ").strip()
    article_content = input("Enter article content: ").strip()
    if not article_title or not article_content:
        print("Article title and content cannot be empty.")
        return

    # Connect to the database
    conn = get_db_connection()
    try:
        cursor = conn.cursor()

        # Create records
        author_id = Author.create_author(cursor, author_name)
        magazine_id = Magazine.create_magazine(cursor, magazine_name, magazine_category)
        create_article(cursor, article_title, article_content, author_id, magazine_id)

        conn.commit()

        # Display all records
        display_records(cursor)

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()
