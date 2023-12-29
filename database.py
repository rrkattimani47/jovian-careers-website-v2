from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://wqgvegatku7sa7dxk55y:pscale_pw_bhlab9IBzXp3awoRxPGItJ9Lo770wtGXrQGJA6gkuKc@aws.connect.psdb.cloud/rashmicareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as connection:
  result = connection.execute(text("select * from jobs"))
  print(type(result))
  print(result.all())
  
