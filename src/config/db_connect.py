from sqlmodel import create_engine


def get_url():
    user = 'nfactorial_user'
    password = 'qwerty123'
    server = 'localhost'
    port = '5432'
    db = 'nfactorial'
    return f"postgresql+psycopg://{user}:{password}@{server}:{port}/{db}"


engine = create_engine(get_url())
