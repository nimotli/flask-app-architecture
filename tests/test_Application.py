# import sys

# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from alembic.command import upgrade as alembic_upgrade
# from alembic.config import Config as AlembicConfig
# from tempfile import tempfile
# from src import create_app
# import os

# def pytest_configure(config):
#     sys._called_from_test = True


# def pytest_unconfigure(config):
#     del sys._called_from_test


# @pytest.fixture(scope='session')
# def flask_app(request):
#     app = create_app()
#     print('\n----- CREATE FLASK APPLICATION\n')

#     context = app.app_context()
#     context.push()
#     yield app
#     print('\n----- CREATE FLASK APPLICATION CONTEXT\n')

#     context.pop()
#     print('\n----- RELEASE FLASK APPLICATION CONTEXT\n')


# @pytest.fixture(scope='session')
# def flask_client(request, flask_app):
#     print('\n----- CREATE FLASK TEST CLIENT\n')
#     return flask_app.test_client()


# @pytest.fixture(scope='session')
# def db(request):
#     db_fd, src.app.config['DATABASE'] = tempfile.mkstemp()
#     src.app.config['TESTING'] = True
#     os.close(db_fd)
#     os.unlink(app.config['DATABASE'])

#     engine = create_engine(config['TEST_DB_URL'], echo=True)
#     session_factory = sessionmaker(bind=engine)
#     print('\n----- CREATE TEST DB CONNECTION POOL\n')

#     _db = {
#         'engine': engine,
#         'session_factory': session_factory,
#     }
#     alembic_config = AlembicConfig(config['ALEMBIC_INI'])
#     alembic_config.set_main_option('sqlalchemy.url', config['TEST_DB_URL'])
#     alembic_upgrade(alembic_config, 'head')
#     print('\n----- RUN ALEMBIC MIGRATION\n')
#     yield _db
#     print('\n----- CREATE TEST DB INSTANCE POOL\n')

#     engine.dispose()
#     print('\n----- RELEASE TEST DB CONNECTION POOL\n')


# @pytest.fixture(scope='function')
# def session(request, db):
#     session = db['session_factory']()
#     yield session
#     print('\n----- CREATE DB SESSION\n')

#     session.rollback()
#     session.close()
#     print('\n----- ROLLBACK DB SESSION\n')