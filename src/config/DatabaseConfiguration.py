
def init_db(app,env):
    datasource = env['datasource']
    dbtype=datasource.get('type')
    host=datasource.get('host')
    driver=datasource.get('driver')
    username=datasource.get('username')
    password=datasource.get('password')
    port=datasource.get('port')
    database=datasource.get('database')
    cnxUriTemplate = '{}:///{}'.format(dbtype,database) if dbtype=="sqlite" else '{}://{}:{}@{}:{}/{}'.format(dbtype,username,password,host,port,database)
    app.config['SQLALCHEMY_DATABASE_URI'] = cnxUriTemplate
    # engine = sa.create_engine(cnxString)
    print("-"*40)
    print("Initialized the {} database".format(dbtype))
    print("-"*40)
    return app

