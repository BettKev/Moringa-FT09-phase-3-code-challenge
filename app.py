from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def display_menu():
    """Display the CRUD menu."""
    print("\nMenu:")
    print("1. Create Author")
    print("2. Create Magazine")
    print("3. Create Article")
    print("4. Read All Records")
    print("5. Update Author")
    print("6. Update Magazine")
    print("7. Update Article")
    print("8. Delete Author")
    print("9. Delete Magazine")
    print("10. Delete Article")
    print("11. Exit")

def display_records(cursor):
    """Fetch and display all records."""
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
        while True:
            display_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == "1":
                name = input("Enter author's name: ").strip()
                if name:
                    author_id = Author.create(cursor, name)
                    print(f"Author created with ID: {author_id}")
                    conn.commit()
                else:
                    print("Author name cannot be empty.")

            elif choice == "2":
                name = input("Enter magazine name: ").strip()
                category = input("Enter magazine category: ").strip()
                if name and category:
                    magazine_id = Magazine.create(cursor, name, category)
                    print(f"Magazine created with ID: {magazine_id}")
                    conn.commit()
                else:
                    print("Magazine name and category cannot be empty.")

            elif choice == "3":
                title = input("Enter article title: ").strip()
                content = input("Enter article content: ").strip()
                author_id = input("Enter author ID: ").strip()
                magazine_id = input("Enter magazine ID: ").strip()
                if title and content and author_id.isdigit() and magazine_id.isdigit():
                    article_id = Article.create(cursor, title, content, int(author_id), int(magazine_id))
                    print(f"Article created with ID: {article_id}")
                    conn.commit()
                else:
                    print("Invalid input. Ensure all fields are provided and IDs are numeric.")

            elif choice == "4":
                display_records(cursor)

            elif choice == "5":
                author_id = input("Enter author ID to update: ").strip()
                name = input("Enter new author name: ").strip()
                if author_id.isdigit() and name:
                    Author.update(cursor, int(author_id), name)
                    print("Author updated successfully.")
                    conn.commit()
                else:
                    print("Invalid input.")

            elif choice == "6":
                magazine_id = input("Enter magazine ID to update: ").strip()
                name = input("Enter new magazine name: ").strip()
                category = input("Enter new magazine category: ").strip()
                if magazine_id.isdigit() and name and category:
                    Magazine.update(cursor, int(magazine_id), name, category)
                    print("Magazine updated successfully.")
                    conn.commit()
                else:
                    print("Invalid input.")

            elif choice == "7":
                article_id = input("Enter article ID to update: ").strip()
                title = input("Enter new article title: ").strip()
                content = input("Enter new article content: ").strip()
                author_id = input("Enter new author ID: ").strip()
                magazine_id = input("Enter new magazine ID: ").strip()
                if article_id.isdigit() and title and content and author_id.isdigit() and magazine_id.isdigit():
                    Article.update(cursor, int(article_id), title, content, int(author_id), int(magazine_id))
                    print("Article updated successfully.")
                    conn.commit()
                else:
                    print("Invalid input.")

            elif choice == "8":
                author_id = input("Enter author ID to delete: ").strip()
                if author_id.isdigit():
                    Author.delete(cursor, int(author_id))
                    print("Author deleted successfully.")
                    conn.commit()
                else:
                    print("Invalid input.")

            elif choice == "9":
                magazine_id = input("Enter magazine ID to delete: ").strip()
                if magazine_id.isdigit():
                    Magazine.delete(cursor, int(magazine_id))
                    print("Magazine deleted successfully.")
                    conn.commit()
                else:
                    print("Invalid input.")

            elif choice == "10":
                article_id = input("Enter article ID to delete: ").strip()
                if article_id.isdigit():
                    Article.delete(cursor, int(article_id))
                    print("Article deleted successfully.")
                    conn.commit()
                else:
                    print("Invalid input.")

            elif choice == "11":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()
