from src.config.ApplicationProperties import getEnv
import flask_monitoringdashboard as dashboard


def configure_app(app,profile):
    if profile == "dev":
        app.config['DEBUG']=True
        env = getEnv("dev")
    elif profile == "prod":
        app.config['DEBUG']=False
        env = getEnv("prod")
    elif profile == "test":
        app.config['TESTING']=True
        env = getEnv("test")
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = env['jwt_secret']
    app.config['JWT_AUTH_URL_RULE'] = env['auth_url']
    return app,env

def configure_monitoring(env):
    dashboard.config.init_from(file=env['monitoring_path'])
    return dashboard
