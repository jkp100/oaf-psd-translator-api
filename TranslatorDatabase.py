import sqlite3
import argparse

class TranslatorDatabase:

    def __init__(self, db_path="translations.db"):
        try:
            self.conn = sqlite3.connect(db_path)
            self.create_table()
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS translations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_text TEXT,
            detected_language TEXT,
            translated_text TEXT,
            source_lang TEXT,
            target_lang TEXT
        );
        '''
        try:
            self.conn.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def add_translation(self, original_text, detected_language, translated_text, source_lang, target_lang):
        query = '''
        INSERT INTO translations (original_text, detected_language, translated_text, source_lang, target_lang)
        VALUES (?, ?, ?, ?, ?);
        '''
        try:
            self.conn.execute(query, (original_text, detected_language, translated_text, source_lang, target_lang))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding translation: {e}")

    def get_all_translations(self):
        query = 'SELECT translated_text FROM translations;'
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving translations: {e}")

    def reset_database(self):
        query = 'DELETE FROM translations;'
        try:
            self.conn.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error resetting database: {e}")


    def close_connection(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing connection: {e}")

    def main():
        parser = argparse.ArgumentParser(description='Translator Database Script')
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
