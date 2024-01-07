import sqlite3
import argparse

#Create Database
class TranslatorDatabase:

    def __init__(self, db_path="translations.db"):
        try:
            self.conn = sqlite3.connect(db_path)
            self.create_table()
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    #Function to Create SQL Table & Query
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS translations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_to_translate TEXT,
            source_lang TEXT,
            translated_text TEXT,

            target_lang TEXT
        );
        '''
        try:
            self.conn.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    #Function to add translations to database
    def add_translation(self, conversation):
        query = '''
        INSERT INTO translations (text_to_translate, source_lang, translated_text, target_lang)
        VALUES (?, ?, ?, ?);
        '''
        try:
            self.conn.execute(query, conversation)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding translation: {e}")

    # Function to get all translations
    def get_all_translations(self):
        query = 'SELECT text_to_translate, translated_text FROM translations;'
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving translations: {e}")
            return None


    #Function to Reset Database
    def reset_database(self):
        query = 'DELETE FROM translations;'
        try:
            self.conn.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error resetting database: {e}")

    #Function to close connection to Database
    def close_connection(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")

    #Function to serve as entry point for SQLite to store translations
    @staticmethod
    def main():
        #Define command line argument parser to handle command-line arguments
        parser = argparse.ArgumentParser(description='Translator Database Script')
        #Create an instance of TranslatorDatabase class, resets the database and then closes the connection
        parser.add_argument('--reset', action='store_true', help='Reset the database')
        args = parser.parse_args()

        if args.reset:
            db = TranslatorDatabase()
            db.reset_database()
            print("Database reset successfully.")
            db.close_connection()
        else:
            print("Use --reset to reset the database.")

if __name__ == "__main__":
    TranslatorDatabase.main()
