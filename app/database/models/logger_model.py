from database.models import Base
from database.models.user_model import User
from sqlalchemy.orm import Mapped, mapped_column


class Logger(Base):
    __tablename__ = "loggers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    logger_ip: Mapped[str] = mapped_column()
    create_at: Mapped[str] = mapped_column()
