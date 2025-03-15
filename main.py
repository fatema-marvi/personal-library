import json
class BookCollection:
    '''A class to represent a collection of books.'''

    def __init__(self):
        '''Initializes the collection with an empty list of books.'''
        self.book_list = []
        self.storage_file = 'books_data.json'
        self.read_from_file()

    def read_from_file(self):
        '''Reads the book data from the storage file.'''
        try:
            with open(self.storage_file, 'r') as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        '''Saves the book data to the storage file.'''
        with open(self.storage_file, 'w') as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        '''Creates a new book and adds it to the collection.'''
        book_title = input('Enter the title of the book: ')
        book_author = input('Enter the author of the book: ')
        publication_year = input('Enter the publication year of the book: ')
        book_genre = input('Enter the genre of the book: ')
        is_read = input('Have you read this book? (yes/no): ').strip().lower() == 'yes'

        new_book = {
            'title': book_title,
            'author': book_author,
            'publication_year': publication_year,
            'genre': book_genre,
            'is_read': is_read,
            'reading_progress': 0
        }
        self.book_list.append(new_book)
        self.save_to_file()
        print('The book has been added to the collection.')

    def delete_book(self):
            '''Removes a book from the collection.'''
            book_title = input('Enter the title of the book you want to remove: ')

            for book in self.book_list:
                if book['title'] == book_title:
                    self.book_list.remove(book)
                    self.save_to_file()
                    print('The book has been removed from the collection.\n')
                    return
            print('The book was not found in the collection.')
    
    def search_book(self):
        '''Searches for a book in the collection.'''                
        search_type = input('Search by:\n1. Title\n2. Author\nEnter the number of your choice: ')
        search_text = input('Enter search term:').lower()
        found_books= [
            book
            for book in self.book_list
            if search_text in book['title'].lower() if search_type == '1' or
            search_text in book['author'].lower() if search_type == '2'
        ]                                          
        if found_books:
            for book in found_books:
                print(f'Title: {book["title"]}')
                print(f'Author: {book["author"]}')
                print(f'Publication Year: {book["publication_year"]}')
                print(f'Genre: {book["genre"]}')
                print(f'Reading Progress: {book["reading_progress"]}')
                print(f'Is Read: {book["is_read"]}\n')

        else:
            print('No books found.')

    def update_book(self):
        '''Updates the details of a book in the collection.'''
        book_title = input('Enter the title of the book you want to update: ')
        for book in self.book_list:
            if book['title'] == book_title:
                book['title'] = input(f'Enter the new title of the book ({book["title"]}): ') or book['title']
                book['author'] = input(f'Enter the new author of the book ({book["author"]}): ') or book['author']
                book['publication_year'] = input(f'Enter the new publication year of the book ({book["publication_year"]}): ') or book['publication_year']
                book['genre'] = input(f'Enter the new genre of the book ({book["genre"]}): ') or book['genre']
                book['is_read'] = input(f'Have you read this book? ({book["is_read"]}): ').strip().lower() == 'yes'
                book['reading_progress'] = int(input(f'Enter the reading progress of the book ({book["reading_progress"]}): '))
                self.save_to_file()
                print('The book details have been updated.\n')
                return
        print('The book was not found in the collection.')

    def view_all_books(self):
            '''Displays all the books in the collection.'''
            if self.book_list:
                for book in self.book_list:
                    print(f'Title: {book["title"]}')
                    print(f'Author: {book["author"]}')
                    print(f'Publication Year: {book["publication_year"]}')
                    print(f'Genre: {book["genre"]}')
                    print(f'Reading Progress: {book["reading_progress"]}')
                    print(f'Is Read: {book["is_read"]}\n')
            else:
                print('The book collection is empty.')

    def view_reading_progress(self):
        '''Displays the reading progress of each book in the collection.''' 
        if self.book_list:
            for book in self.book_list:
                print(f'Title: {book["title"]}')
                print(f'Reading Progress: {book["reading_progress"]} %\n')
        else:
            print('The book collection is empty.')

    def start_application(self):
        '''Starts the book collection application.'''
        print('Welcome to the Book 📕 Collection App!')
        while True:
            print('\nMenu:')
            print('1. Create a new book')
            print('2. Remove a book')
            print('3. Search for a book')
            print('4. Update a book details')
            print('5. View all books')
            print('6. View reading progress')
            print('7. Exit the application')
            user_choice = input('Please choose an option(1-7): ')
            if user_choice == '1':
                self.create_new_book()
            elif user_choice == '2':
                self.delete_book()
            elif user_choice == '3':
                self.search_book()
            elif user_choice == '4':
                self.update_book()
            elif user_choice == '5':
                self.view_all_books()
            elif user_choice == '6':
                self.view_reading_progress()
            elif user_choice == '7':
                self.save_to_file()
                print('Thank you for using the Book Collection App! Goodbye!')
                break
            else:
                print('Invalid option. Please try again.\n')

if __name__ == '__main__':     
    book_manager = BookCollection()
    book_manager.start_application()