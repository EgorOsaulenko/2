from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from app.db.models.base import Base

class Dish(Base):
    __tablename__ = "dishes"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(250))
    price: Mapped[float] = mapped_column(Float)
