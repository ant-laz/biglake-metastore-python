# biglake-metastore-python

## What problem does this repo solve ? 

BigLake [Metastore](https://cloud.google.com/bigquery/docs/manage-open-source-metadata) 
can be used as a Catalogue when working with Apache Iceberg tables on BigQuery 
and Dataproc on Google Cloud.

However, the BigLake Rest [API](https://cloud.google.com/bigquery/docs/reference/biglake/rest)
**does not** have a nice python client library similar to the one that exists for the 
BigQuery [API](https://cloud.google.com/bigquery/docs/reference/libraries).

This is a problem as it introduces friction to teams looking to start using
BigLake [Metastore](https://cloud.google.com/bigquery/docs/manage-open-source-metadata)
as soon as possible in their Data Lakehouse projects.

## What solutions does this repo offer ? 

Example python code which shows how to use the generic google api client 
[library](https://github.com/googleapis/google-api-python-client) to interact with the
BigLake Rest [API](https://cloud.google.com/bigquery/docs/reference/biglake/rest).

This example code aims to offer ready usable code that covers basic operations with
BigLake [Metastore](https://cloud.google.com/bigquery/docs/manage-open-source-metadata).

## Using the code in this repo

This code has been tested with python 11. 

Create a Google Cloud project & setup `gcloud` so that it is the active project.

Create local authentication creditals for your user account

```
gcloud auth application-default login
```

Create the following environmental with the following names

```
export PROJECT_ID=$(gcloud config list core/project --format="value(core.project)")

export LOCATION="US"

export CATALOG_NAME="my_catalog"

export DATABASE_NAME="my_database"
```

You can use the library to execute api methods:

### Catalog - List all BigLake Metastore Catalogs in a given project & region

```
python blms_api.py catalog-list \
--project_id=${PROJECT_ID} \
--location=${LOCATION}
```

### Catalog - Creating a new BigLake Metastore Catalog in a project & region

```
python blms_api.py catalog-create \
--project_id=${PROJECT_ID} \
--location=${LOCATION} \
--catalog=${CATALOG_NAME}
```

### Database - List all Databases in a BigLake Metastore Catalog

```
python blms_api.py database-list \
--project_id=${PROJECT_ID} \
--location=${LOCATION} \
--catalog=${CATALOG_NAME}
```

### Database - Create a new Databse in a BigLake Metastore Catalog

```
python blms_api.py database-create \
--project_id=${PROJECT_ID} \
--location=${LOCATION} \
--catalog=${CATALOG_NAME} \
--database=${DATABASE_NAME}
```

### Table - List all Tables in a Database in a BigLake Metastore Catalog

```
python blms_api.py table-list \
--project_id=${PROJECT_ID} \
--location=${LOCATION} \
--catalog=${CATALOG_NAME} \
--database=${DATABASE_NAME}
```




