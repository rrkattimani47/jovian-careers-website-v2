from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://kgu4rnfpn72r2d6nwqfk:pscale_pw_PaJ4SmO30U0OayWMI4uaQxb2LsI2myMcu5VnvpwOaGb@aws.connect.psdb.cloud/rashmicareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

