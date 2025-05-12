from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pokemon.db', echo=True)
SessionLocal =sessionmaker(autoflush= False, autocommit=False, bind=engine)
print('Conexão bem sucedida')

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


