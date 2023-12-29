from datetime import datetime, timedelta
from database.models.logger_model import Logger
from database.schemas.logger_schema import LoggerSchema
from modules.repositories import BaseRepository
from sqlalchemy import delete

TIME_FORMAT = "%d/%m/%Y, %H:%M:%S"

class LoggerRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = Logger
        self.schema = LoggerSchema()

        self.session_query = self.get_session_query()

    def login_logger(self, ip: str):
        self.session.add(
            self.model(
                logger_ip=ip,
                create_at=datetime.now().strftime(TIME_FORMAT),
            )
        )

    def check_logger(self, ip: str):
        logger: Logger = (
            self.session_query.filter(self.model.logger_ip == ip)
            .order_by(self.model.create_at.desc())
            .first()
        )
        if logger is None:
            return False

        return not self.__check_outdate_logger(create_at=logger.create_at)

    def clear_log(self):
        loggers: list[Logger] = list(
            self.session_query
            .order_by(self.model.create_at.desc())
            .all()
        )

        clear_loggers = [
            logger.id
            for idx, logger in enumerate(loggers)
            if idx >= 50 or self.__check_outdate_logger(create_at=logger.create_at)
        ]

        self.session_query.filter(self.model.id.in_(clear_loggers)).delete(synchronize_session=False)

    @classmethod
    def __check_outdate_logger(cls, create_at: str) -> bool:
        """
        Return true if
        """
        log_time = datetime.strptime(create_at, TIME_FORMAT)
        return datetime.now() > log_time + timedelta(hours=1)

