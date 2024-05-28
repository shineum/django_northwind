## Django Northwind

## Northwind Database
The Northwind database is a sample database that was originally created by Microsoft and used as the basis for their tutorials in a variety of database products for decades. The Northwind database contains the sales data for a fictitious company called “Northwind Traders,” which imports and exports specialty foods from around the world. The Northwind database is an excellent tutorial schema for a small-business ERP, with customers, orders, inventory, purchasing, suppliers, shipping, employees, and single-entry accounting. The Northwind database has since been ported to a variety of non-Microsoft databases, including PostgreSQL.

[Reference URL](https://docs.yugabyte.com/preview/sample-data/northwind/ 'yugabyte.com')


## How to use

### 1. Clone source code
```bash
git clone https://github.com/shineum/django_northwind.git
```

### 2. Create virtual env
```bash
cd django_northwind
python -m venv .venv
```

### 3. Activate virtual env
```bash
# for mac or linux
source ./.venv/bin/activate
# for windows
call .\venv\Scripts\activate.bat
```

### 4. Install modules
```bash
pip install -r requirements.txt
```

### 5. Database setup (optional)
For who wants to use postgres database only.
You can skip this step, then SQLite will be used.
```bash
cp sample.env .env
```
Change an environment file (.env) as your environment.


### 6. Migrate database
```bash
python manage.py migrate
```


### 7. Load data
```bash
python manage.py loaddata apps/northwind/fixtures/northwind.json
```


### 8. Create admin user
```bash
python manage.py createsuperuser
```


### 9. Run server
```bash
python manage.py runserver
```


### 10. Login to a website as an admin
```bash
http://localhost:8000/admin
```


## REST APIs

### 1. API base
```
http://localhost:8000/api/v1/
```

### 2. OpenAPI urls
```
http://localhost:8000/api/v1/swagger/
http://localhost:8000/api/v1/swagger.json/
http://localhost:8000/api/v1/redoc/
```


## References
https://github.com/samgca/django_northwind  
https://github.com/pthom/northwind_psql
