# Database ORM API:

<p>
A python module to read all json files in a given folder and split the key-value pairs into model.attribute-value pairs and then push the model objects into a relational database.
</p>

### Functionality:

1. Parse through each '*.json' file and input the key-value pairs to the appropriate collumns in the appropriate tables.
2. Retrieve the data from the database tables and reconstruct the files with the original filenames.

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

