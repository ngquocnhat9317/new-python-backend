from database.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE = "my-python-app-main-db-01b95e4f037436ea0"
HOST = "user-prod-us-east-2-1.cluster-cfi5vnucvv3w.us-east-2.rds.amazonaws.com"
USER = "my-python-app-main-db-01b95e4f037436ea0"
PASSWD = "u8JJ6RHC9Ej55XVpMMyF8BvGwyecgY"
PORT = "5432"


def get_engine():
    url = f"postgresql://{USER}:{PASSWD}@{HOST}:{PORT}/{DATABASE}"
    return create_engine(url)


engine = get_engine()

Session = scoped_session(sessionmaker())
Session.configure(bind=engine)
