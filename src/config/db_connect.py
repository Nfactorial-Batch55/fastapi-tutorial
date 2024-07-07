from sqlmodel import create_engine
from migrations.env import get_url


engine = create_engine(get_url())
