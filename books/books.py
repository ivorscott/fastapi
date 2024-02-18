from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    { 'title': "title one", 'author': 'Author one','category':'science'},
    { 'title': "title two", 'author': 'Author two','category':'science'},
    { 'title': "title three", 'author': 'Author three','category':'history'},
    { 'title': "title four", 'author': 'Author four','category':'math'},
    { 'title': "title five", 'author': 'Author five','category':'math'},
    { 'title': "title six", 'author': 'Author six','category':'math'},
]

@app.get("/books")
async def read_all_books():
    """
    Books for the public collection of the library.
    """
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title:str):
    """
    A specific book from the public collection of the library.
    """
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
@app.get("/books/")
async def filter_books_by_category(category: str):
    """
    Filter public book collection by category.
    """
    books = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books.append(book)
    return books

@app.get("/books/{book_author}/")
async def filter_books_by_author_and_category(book_author: str, category: str):
    """
    Filter public book collection by author and category.
    """
    books = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books.append(book)
    return books

@app.post('/books')
async def create_book(new_book=Body()):
    """
    Create a new book for the public collection.
    """
    BOOKS.append(new_book)