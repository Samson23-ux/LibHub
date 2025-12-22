from fastapi.responses import JSONResponse
from fastapi import Request
from typing import Any, Callable

class LibraryException(Exception):
    '''Base Exception for all Errors'''
    pass

class ServerError(LibraryException):
    '''Internal Server Error'''
    pass

class AuthenticationError(LibraryException):
    '''User provided an invalid token'''
    pass

class AuthorizationError(LibraryException):
    '''User not authorized'''
    pass

class EmailError(LibraryException):
    '''User provided an invalid email'''
    pass

class PasswordError(LibraryException):
    '''User provided an invalid password'''
    pass

class UserExistError(LibraryException):
    '''User provided an exsisting email'''
    pass

class UsersNotFoundError(LibraryException):
    '''No Users found currently'''
    pass

class UserNotFound(LibraryException):
    '''User not found with the provided id'''
    pass

class AuthorExistError(LibraryException):
    '''An existing author was provided'''
    pass

class AuthorsNotFoundError(LibraryException):
    '''No authors found currently'''
    pass

class AuthorNotFoundError(LibraryException):
    '''A wrong id was provided to get an author'''
    pass

class BookExistError(LibraryException):
    '''An existing book was provided'''
    pass

class BooksNotFoundError(LibraryException):
    '''No books found currently'''
    pass

class BookNotFoundError(LibraryException):
    '''A wrong id was provided to get a book'''
    pass

class StaffExistError(LibraryException):
    '''An existing staff name was provided'''
    pass

class StaffNotFoundError(LibraryException):
    '''No staff at the moment or a wrong id was provided'''
    pass

class BorrowHistoryExistError(LibraryException):
    '''An existing borrow history was provided'''
    pass

class BorrowHistoriesNotFoundError(LibraryException):
    '''No borrow histories found currently'''
    pass

class BorrowHistoryNotFoundError(LibraryException):
    '''A wrong id was provided to get a borrow history'''
    pass

class PenaltyExistError(LibraryException):
    '''An existing penalty was issued to the same borrow history'''
    pass

class PenaltiesNotFoundError(LibraryException):
    '''No penalties found currently'''
    pass

class PenaltyNotFoundError(LibraryException):
    '''A wrong id was provided to get a penalty'''
    pass

def create_exception_handler(status_code: int, initial_detail: Any) -> Callable[[Request, Exception], JSONResponse]:
    async def exception_handler(request: Request, exc: LibraryException):
        return JSONResponse(
            status_code=status_code,
            content=initial_detail
        )
    return exception_handler
