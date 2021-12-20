# Database ORM API:

<p>
A python module to read all json files in a given folder and split the key-value pairs in model.attribute-value pairs and then push the model objects into a relational database.
</p>

### Usage:

```
1. Make env and .env file.
2. Edit 'REPROT_PATH' in main to the folder containing the Allure Reports.
3. Edit .env file as per format given below.

4. Run init.py to initialize the tables.
5. Run main as "__main__" as per requirements.
```


### Env file format:

```
DB_TYPE=""
PGHOST=""
PGPORT=""
PGDATABASE=""
PGUSER=""
PGPASSWORD=""
```