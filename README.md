# transactions_test

## Problem
Al tener tantos datos e información de transacciones, llega un punto donde se pierde el manejo y control de la operación, visualización y monitoreo. Se necesita localizar ciertas combinaciones con los datos compartidos, para conocer mejor las operaciones y transacciones que se tienen. 

En el documento anexo en el apartado de base de datos, se encuentra un archivo en CSV que debe ser importado a una base de datos en el motor de su preferencia y considerando el siguiente modelado base, en este punto se puede proponer mejoras e información extra que se considere necesaria:

**Modelado Base**

- Transaction:
    - ID (en el formato que se considere más seguro)
    - ID de empresa
    - Price (el price actual no viene en la cantidad real... requiere una conversión...) o evaluación por ser costos reales
    - Fecha de transacción
    - Estatus de transacción
        - closed —> transaccion cobrada
        - reversed —> cobro realizado y regresado (para validar tarjeta)
        - pending —> pendiente de cobrar
    - Estatus de aprobación
        - false —> no se hizo un cobro
        - true —>  el cobro si fue aplicado a la tarjeta
    - Cobro Final  (Boolean)
        - Este punto es una combinación de "Estatus de transacción y estatus de aprobación"
            - Sólo se deben cobrar aquellas combinaciones que sean:
                - status_transaction = closed
                - status_approved = true

- ServicePriceCatalog:
    - id (uuid)
    - company_id (Foreign Key to Company)
    - base_price (decimal)

- Company:
    - Nombre
    - Status (activa/inactiva)
    - ID (en el formato que se considere más seguro)

- Account:
    - id (uuid)
    - clabe (string)
    - account_number (string)
    - company_id (Foreign Key to Company)
    - acount_type (Foreign Key to AccountType)

- AccountType:
    - id (uuid)
    - type_name (string)

- Address:
    - id (uuid)
    - company_id (Foreign Key to Company)
    - street (string)
    - number (string)
    - colony (string)
    - city (string)
    - state (string)
    - country_code_id (string)
    - zip_code (string)

- CountryCode:
    - id (uuid)
    - country_code (uuid)
    - country_name (uuid)

- CompanyUser:
    - id (uuid)
    - name (string)
    - last_name (string)
    - company_id (Foreign Key to Company)
    - user_type_id (Foreign Key to UserType)
    - contact_type_id (Foreign Key to ContactType)

- UserType:
    - id (uuid)
    - type_name (string)

- UserContactType:
    - id (uuid)
    - contact_type_name (string)
    - contact_type_value (string)

**Methods**  
    - set_real_price: On Model ServicePriceCatalog to set the real price on every each transaction.  
    - set_pk: On BaseModel to auto generate uuid value for id field. BaseModel extends over all models.  

### Diagrama Entidad-Relación
![Modelo Entidad Relacion](/data/plerk_test%20-%20DER.png)

## Setup project
  
### Requirements
- Python 3.9
- Django 3.2.12
- Django Rest Framework 3.13.1
- Pandas 1.4.2
- ipython 8.3.0
- DRF Spectacular 0.22.1
  

### Virtual environment
Create virtual environment  
`python3 -m venv <virtual_environment_name>`  
  
Activate virtual envionment  
`source <virtual_environment_name>/bin/activate`  
  
Clone repository  
`git clone git@github.com:mariomtzjr/transactions_test.git`  

### Install requirements  
Move into cloned repository  
`cd transactions_test/`  
`pip3 install -r requirements.txt`  

## Populate database
The project has a file (__/data/test_database.csv__) that contains information that is imported into an __SQLite engine__. Since the Django ORM will be used, it is necessary to have all the requirements listed above installed.

Since some of the records in our file contain null values, using the __pandas__ library, the information is processed and a final file called __test_database_built.csv__ (/data/test_database_built.csv) is created, whose information is what is currently in the database  (__db.sqlite3__), therefore, it is not necessary to import the information.

#### Steps to populate database
We need to be into transactions_test repository/directory:  
1. `python manage.py shell`: Open project's shell
2. `In [1] from scripts.seed import main`: Import main method to populate database 
3. `In [2] main()`: Will execute main method (database connection, db.sqlite3 database creation and populate database)

#### Run server
`python manage.py runserver`  


## API Doc
Out server is running over `http://localhost:8000/`, so the API doc is available over this URL: `http://localhost:8000/api/v1/schema/redoc/`

## Server on PythonAnyWhere
URL: `https://mariomartinez.pythonanywhere.com/`

## Django Admin Site
Current database contains a superuser to access to admin site, only you need to use the following credentials:  
**`username: mariomartinez`**  
**`password: test1234`**  

### Steps to create a new superuser
We need to be into transactions_test repository/directory: 
1. `python manage.py createsuperuser`  
2. `Set username or press enter to use default`  
3. `Enter a valid email`  
4. `Set password`
5. `Confirm password`
6. `Typing y confirm password`

