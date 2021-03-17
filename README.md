# Flask Application Structure (DONT USE YET ONGOING WORK)

It's an easy to understand layered Flask architecture for application backends, inspired by Jhipster

### Features
  - Layered: Web->Service->Repository Architecture
  - Multiple database sources(not yet) and types
  - Migration
  - ORM
  - JWT authentication
  - Testing
  - Multiple Profiles for multiple environment

### Installation

- Clone this repo
- Create a python virtual environment (Optional)
- Activate the virtual environment (Optional)
- Run : pip install -r requirements.tx

(write the installation steps for all OS)
### Setup
(write the setup steps for all OS)

### Migration : 
- Create the entity in ./src/domain/
- Add it to the import list in the create-app function in src/__init__.py
- Run : flask db init -d resources/migration/main
- Run : flask db migrate -d resources\migration\main -m "migration name"
- Run : flask db upgrade

### ORM
The app user SQLALCHEMY

### Authentication
The app support simple JWT authentication with more strategies to be implemented later.
- You can find and update the User model in src/domain/User.py
- You can find and update the Authentication logic in src/config/AuthenticationProvider.py authenticate
- You can find and update the identity logic in src/config/AuthenticationProvider.py identity (for getting the currently authenticated user)
- You can find and update the register logic in src/service/AuthenticationService.py register
- The api for signup is host:port/auth/register POST with a json body containing email,username and a password
- The api for signin is host:port/api/authenticate POST with a json body containing username and password
#### JWT
- Requires a valid database connection and to already launch a migration
- /register to create a new user
- /api/authenticate [POST] to get jwt token
- Send username and password
- Pass the recieved token as a header "Authorization":"JWT your_generated_token"

### Database Configuration
- Change the datasource values in the profiles (resources/profile)
- You can find and update the database configuration logic in src/config/DatabaseConfiguration

### Models
(Write the steps for adding a new model)

### Profiles
The app comes with 3 profiles for development, production and test envirenment, each profile contains some configs (currently data source and authentication config will add more later) you can find and edit the profiles in resources/profile/**.json .
#### Adding A Profile
  - Create a json file for you profile in resources/profile/ with the same datasource and auth data as the other profiles.
  - Add a condition case for a keyword that you'd like to associate to you newly created profile in src/config/Configure configure_app function.

### Testing
The app comes preconfigured with a testing profile that gets used when the tests are run, it also uses pytest.
- You can find the profile for the test env in resources/profile/application-test.json 
- Run : python -m pytest to run the tests (after activating the virtual env) 
- There are already some unit & integration tests for the current functionnality
- You can add your tests to tests/
- There are already some fixtures (for creating a user object and for initializing the test client and creating a tests database and migrating you tables to it)
- You can add your fixtures to tests/conftest.py
### Routing

### Monitoring
  - You can access the monitoring dashboard using this url host:ip/dashboard
  - You can authenticate using the credentials in the config files in resources/config/monitoring/
  - For a detailed documentation from the package's developers [Documentation](https://flask-monitoringdashboard.readthedocs.io/en/latest/index.html)