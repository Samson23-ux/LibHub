from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import JSONResponse


from app.routers.v1.admin import admin_router_v1
from app.routers.v1.authors import author_router_v1
from app.routers.v1.books import book_router_v1
from app.routers.v1.borrow_history import borrow_history_router_v1
from app.routers.v1.penalties import penalty_router_v1
from app.routers.v1.users import users_router_v1


from app.core.config import settings

from app.errors import (
    create_exception_handler,
    AuthenticationError,
    AuthorizationError,
    AuthorExistError,
    AuthorNotFoundError,
    AuthorsNotFoundError,
    BookExistError,
    BookNotFoundError,
    BooksNotFoundError,
    BorrowHistoryExistError,
    BorrowHistoriesNotFoundError,
    BorrowHistoryNotFoundError,
    EmailError,
    PasswordError,
    PenaltyExistError,
    PenaltiesNotFoundError,
    PenaltyNotFoundError,
    StaffExistError,
    StaffNotFoundError,
    UserExistError,
    UserNotFound,
    UsersNotFoundError,
)

app = FastAPI(title=settings.API_TITLE, description=settings.DESCRIPTION)


@app.get("/")
async def home():
    return """Welcome to LibHub API v1.0.
    A Library Management System where
    users can borrow book issued by a librarian,
    admin can manage and view statistics for
    available and borrowed books.
"""


error_time: datetime = datetime.timestamp()

app.include_router(author_router_v1, prefix=settings.API_VERSION_1, tags=["AuthorsV1"])
app.include_router(book_router_v1, prefix=settings.API_VERSION_1, tags=["BooksV1"])
app.include_router(
    borrow_history_router_v1, prefix=settings.API_VERSION_1, tags=["Borrow HistoryV1"]
)
app.include_router(
    penalty_router_v1, prefix=settings.API_VERSION_1, tags=["PenaltiesV1"]
)
app.include_router(admin_router_v1, prefix=settings.API_VERSION_1, tags=["Admin"])
app.include_router(users_router_v1, prefix=settings.API_VERSION_1, tags=["Users"])


@app.exception_handler(500)
async def internal_server_error(request, exc):
    return JSONResponse(
        status_code=500,
        content={"error_code": "Server error", "message": "Oops! Something went wrong"},
    )


app.add_exception_handler(
    exc_class_or_status_code=AuthenticationError,
    handler=create_exception_handler(
        status_code=401,
        initial_detail={
            "error_code": "Not Authenticated",
            "message": "User should sign up or sign in to accesss resource",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=AuthorizationError,
    handler=create_exception_handler(
        status_code=403,
        initial_detail={
            "error_code": "Not Authorized",
            "message": "User does not have access to the resource",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=EmailError,
    handler=create_exception_handler(
        status_code=400,
        initial_detail={
            "error_code": "Invalid email",
            "message": "Check the provided email to confirm its validity",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=PasswordError,
    handler=create_exception_handler(
        status_code=400,
        initial_detail={
            "error_code": "Invalid password",
            "message": "Check the provided password to confirm its validity",
            "timestamp": error_time,
        },
    ),
)


app.add_exception_handler(
    exc_class_or_status_code=UserExistError,
    handler=create_exception_handler(
        status_code=400,
        initial_detail={
            "error_code": "User Exist",
            "message": "User provided an existing email",
            "resolution": """Check the provided email to
                            confirm if does not exist already""",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=UsersNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Users not found",
            "message": "No users at the moment. Check back later!",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=UserNotFound,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "User not found",
            "message": "User not found with the provided id",
            "resolution": "Confirm that the sent id matches the user id",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=AuthorExistError,
    handler=create_exception_handler(
        status_code=400,
        initial_detail={
            "error_code": "Author already exist",
            "message": "Author name already exist",
            "resolution": "Check the provided name to confirm if it does not already exist",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=AuthorsNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Authors not found",
            "message": "No authors at the moment. Check back later!",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=AuthorNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Author not found",
            "message": "Author not found with the provided id",
            "resolution": "Confirm that the provided id matches the author id",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=BookExistError,
    handler=create_exception_handler(
        status_code=400,
        initial_detail={
            "error_code": "Book already exist",
            "message": "Book name already exist",
            "resolution": "Check the provided name to confirm if it does not already exist",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=BooksNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Books not found",
            "message": "No books at the moment. Check back later!",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=BookNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Book not found",
            "message": "Book not found with the provided id",
            "resolution": "Confirm that the provided id matches the book's id",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=StaffExistError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Staff already exist",
            "message": "A staff with the provided name already exist",
            "resolution": "Check the provided name to confirm if it does not already exist",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=StaffNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Staff not found",
            "message": "No staff at the moment or staff not found with the provided id",
            "resolution": "Confirm that the provided id matches the staff id",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=BorrowHistoryExistError,
    handler=create_exception_handler(
        status_code=400,
        initial_detail={
            "error_code": "Borrow history already exist",
            "message": "Borrow history created already",
            "resolution": """Check the provided borrow details
                            to confirm if it does not already exist""",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=BorrowHistoriesNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Borrow histories not found",
            "message": "No borrow histories at the moment",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=BorrowHistoryNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Borrow history not found",
            "message": "Borrow history not found with the provided id",
            "resolution": "Confirm that the provided id matches the record's id",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=PenaltyExistError,
    handler=create_exception_handler(
        status_code=400,
        initial_detail={
            "error_code": "Penalty already exist",
            "message": "A penalty for the borrow history already exist",
            "resolution": """Check the provided penalty for the borrow
                            history to confirm if it does not already exist""",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=PenaltiesNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Penalties not found",
            "message": "No penalties at the moment. Check back later!",
            "timestamp": error_time,
        },
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=PenaltyNotFoundError,
    handler=create_exception_handler(
        status_code=404,
        initial_detail={
            "error_code": "Penalty not found",
            "message": "Penalty not found with the provided id",
            "resolution": "Confirm that the provided id matches the penalty's id",
            "timestamp": error_time,
        },
    ),
)
