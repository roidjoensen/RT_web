
from qwe import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('mssql+pyodbc://TOR-PC\SQLEXPRESS/log?driver=ODBC+Driver+11+for+SQL+Server',echo=True )

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password")
session.add(user)

user = User("python", "python")
session.add(user)

user = User("jumpiness", "python")
session.add(user)

# commit the record the database
session.commit()

session.commit()