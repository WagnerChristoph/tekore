from typing import Optional, Sequence, TypeVar, Generic

from .serialise import Model

T = TypeVar('T', bound=Model)

class Paging(Model, Generic[T]):
    """Paging base."""

    href: str
    items: Sequence[T]
    limit: int
    next: Optional[str]


class OffsetPaging(Paging, Generic[T]):
    """
    Offset paging base.

    Paging that can be navigated both forward and back.
    """

    total: int
    offset: int
    previous: Optional[str]


class Cursor(Model):
    """Data cursor."""

    after: Optional[str]


class CursorPaging(Paging):
    """
    Cursor paging base.

    Paging that can be navigated only forward following the cursor.
    """

    cursors: Cursor
