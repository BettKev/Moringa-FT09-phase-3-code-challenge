from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

# Function to display records in the database
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

    # Connect to the database
    conn = get_db_connection()
    try:
        cursor = conn.cursor()

        # Example CRUD operations for testing purposes
        print("Creating records...")
        author_id = Author.create(cursor, "John Doe")
        magazine_id = Magazine.create(cursor, "Tech Monthly", "Technology")
        article_id = Article.create(cursor, "AI Trends", "Exploring AI in 2024", author_id, magazine_id)

        print("\nDisplaying records after creation:")
        display_records(cursor)

        print("\nUpdating records...")
        Author.update(cursor, author_id, "Jane Doe")
        Magazine.update(cursor, magazine_id, "Tech Weekly", "Science and Technology")
        Article.update(cursor, article_id, "AI Innovations", "Deep dive into AI", author_id, magazine_id)

        print("\nDisplaying records after update:")
        display_records(cursor)


        #Uncomment this section to test the delete functionality implementation
        
        # print("\nDeleting records...")
        # Article.delete(cursor, article_id)
        # Author.delete(cursor, author_id)
        # Magazine.delete(cursor, magazine_id)

        # print("\nDisplaying records after deletion:")
        # display_records(cursor)

        conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()
