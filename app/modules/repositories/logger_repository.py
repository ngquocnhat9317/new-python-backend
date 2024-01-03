from datetime import datetime, timedelta

from aiohttp import web
from database.models.logger_model import Logger
from database.schemas.logger_schema import LoggerSchema
from modules.repositories import BaseRepository

TIME_FORMAT = "%d/%m/%Y, %H:%M:%S"


class LoggerRepository(BaseRepository):
    def __init__(self, request: web.Request):
        super().__init__(request)
        self.model = Logger
        self.schema = LoggerSchema()
        self.schema.Meta.sqla_session = self.session

    def login_logger(self, ip: str):
        self.session.add(
            self.model(
                logger_ip=ip,
                create_at=datetime.now().strftime(TIME_FORMAT),
            )
        )

    async def check_logger(self, ip: str):
        logger: Logger = (
            await self.session.query(self.model)
            .filter(self.model.logger_ip == ip)
            .order_by(self.model.create_at.desc())
            .first()
        )
        if logger is None:
            return False

        return not self.__check_outdate_logger(create_at=logger.create_at)

    async def clear_log(self):
        session_query = await self.session.query(self.model)
        loggers: list[Logger] = list(
            session_query.order_by(self.model.create_at.desc()).all()
        )

        clear_loggers = [
            logger.id
            for idx, logger in enumerate(loggers)
            if idx >= 50 or self.__check_outdate_logger(create_at=logger.create_at)
        ]

        session_query.filter(self.model.id.in_(clear_loggers)).delete(
            synchronize_session=False
        )

    @classmethod
    def __check_outdate_logger(cls, create_at: str) -> bool:
        """
        Return true if
        """
        log_time = datetime.strptime(create_at, TIME_FORMAT)
        return datetime.now() > log_time + timedelta(hours=1)
