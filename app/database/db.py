from config import DATABASE, HOST, PASSWD, PORT, USER
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_engine():
    url = f"postgresql+psycopg2://{USER}:{PASSWD}@{HOST}:{PORT}/{DATABASE}"
    return create_engine(url)


engine = get_engine()

Session = scoped_session(sessionmaker())
Session.configure(bind=engine)
