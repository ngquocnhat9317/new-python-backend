import psycopg2

conn = psycopg2.connect(
    database="my-python-app-main-db-01b95e4f037436ea0",
    host="user-prod-us-east-2-1.cluster-cfi5vnucvv3w"
    ".us-east-2.rds.amazonaws.com",
    user="my-python-app-main-db-01b95e4f037436ea0",
    password="u8JJ6RHC9Ej55XVpMMyF8BvGwyecgY",
    port="5432",
)
