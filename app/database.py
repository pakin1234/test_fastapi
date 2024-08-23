from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases

from api.models.model import metadata
from core.config import SQLALCHEMY_DATABASE_URL as SBU

# вынести отдельно в файл типо settings
SQLALCHEMY_DATABASE_URL = SBU
database = databases.Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

metadata.create_all(engine)



