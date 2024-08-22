#    Copyright 2024 Google LLC

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from googleapiclient.discovery import build
from urllib.error import HTTPError
import click

########################################################################################
@click.group()
def cli():
    pass

########################################################################################
@cli.command()
@click.option(
    "--project_id",
    type=str,
    help="Google Cloud Project ID for listing BigLake Metastore catalogs",
    required=True,
)
@click.option(
    "--location",
    type=str,
    help="Google Cloud Location for listing BigLake Metastore catalogs",
    required=True,
)
def catalog_list(project_id: str,location: str):
    with build('biglake', 'v1') as service:
        try:
            parent_str = f"projects/{project_id}/locations/{location}"
            collection = service.projects().locations().catalogs()
            request = collection.list(parent=parent_str)
            response = request.execute()
            print(response)
        except HTTPError as e:
            print('Error response status code : {0}, reason : {1}'.format(
                e.status_code, 
                e.error_details)
                )

########################################################################################
@cli.command()
@click.option(
    "--project_id",
    type=str,
    help="Google Cloud Project ID for creating a BigLake Metastore catalog",
    required=True,
)
@click.option(
    "--location",
    type=str,
    help="Google Cloud Location for creating a BigLake Metastore catalog",
    required=True,
)
@click.option(
    "--catalog",
    type=str,
    help="Name to use when creating a BigLake Metastore catalog",
    required=True,
)
def catalog_create(project_id:str, location:str, catalog:str):
    with build('biglake', 'v1') as service:
        try:
            parent_str = f"projects/{project_id}/locations/{location}"
            collection = service.projects().locations().catalogs()
            request = collection.create(parent=parent_str, catalogId=catalog)
            response = request.execute()
            print(response)
        except HTTPError as e:
            print('Error response status code : {0}, reason : {1}'.format(
                e.status_code, 
                e.error_details)
                )

########################################################################################
@cli.command()
@click.option(
    "--project_id",
    type=str,
    help="Google Cloud Project ID for listing Databases in BigLake Metastore Catalog",
    required=True,
)
@click.option(
    "--location",
    type=str,
    help="Google Cloud Location for listing Databases in BigLake Metastore Catalog",
    required=True,
)
@click.option(
    "--catalog",
    type=str,
    help="Name of the BigLake Metastore Catalog whose Databases we want to list",
    required=True,
)
def database_list(project_id: str,location: str, catalog:str):
    with build('biglake', 'v1') as service:
        try:
            parent_str = f"projects/{project_id}/locations/{location}/catalogs/{catalog}"
            collection = service.projects().locations().catalogs().databases()
            request = collection.list(parent=parent_str)
            response = request.execute()
            print(response)
        except HTTPError as e:
            print('Error response status code : {0}, reason : {1}'.format(
                e.status_code, 
                e.error_details)
                )

########################################################################################
@cli.command()
@click.option(
    "--project_id",
    type=str,
    help="Google Cloud Project ID to create a Database in a BigLake Metastore Catalog",
    required=True,
)
@click.option(
    "--location",
    type=str,
    help="Google Cloud Location to create a Database in a BigLake Metastore Catalog",
    required=True,
)
@click.option(
    "--catalog",
    type=str,
    help="Name of the BigLake Metastore Catalog to create a Database in it",
    required=True,
)
@click.option(
    "--database",
    type=str,
    help="Name of the Database to create in the specified BigLake Metastore Catalog",
    required=True,
)
def database_create(project_id: str,location: str, catalog:str, database: str):
    with build('biglake', 'v1') as service:
        try:
            parent_str = f"projects/{project_id}/locations/{location}/catalogs/{catalog}"
            collection = service.projects().locations().catalogs().databases()
            request = collection.create(
                parent=parent_str, 
                databaseId=database,
                body={"type": "HIVE"}
                #Do I also need to specify a GCS location ? why ?
                #https://github.com/terraform-google-modules/terraform-docs-samples/blob/main/bigquery/biglake/biglake_metastore_create_table/main.tf#L66-L69
                )
            response = request.execute()
            print(response)
        except HTTPError as e:
            print('Error response status code : {0}, reason : {1}'.format(
                e.status_code, 
                e.error_details)
                )

########################################################################################
@cli.command()
@click.option(
    "--project_id",
    type=str,
    help="Google Cloud Project ID to list tables in DBs in BigLake Metastore Catalog",
    required=True,
)
@click.option(
    "--location",
    type=str,
    help="Google Cloud Location to list tables in DBs in BigLake Metastore Catalog",
    required=True,
)
@click.option(
    "--catalog",
    type=str,
    help="Catalog name to list tables in DBs in BigLake Metastore Catalog",
    required=True,
)
@click.option(
    "--database",
    type=str,
    help="Name of the Database whost tables we are to list out",
    required=True,
)
def table_list(project_id: str,location: str, catalog:str, database:str):
    with build('biglake', 'v1') as service:
        try:
            parent_str = f"projects/{project_id}/locations/{location}/catalogs/{catalog}/databases/{database}"
            collection = service.projects().locations().catalogs().databases().tables()
            request = collection.list(parent=parent_str)
            response = request.execute()
            print(response)
        except HTTPError as e:
            print('Error response status code : {0}, reason : {1}'.format(
                e.status_code, 
                e.error_details)
                )

########################################################################################
if __name__ == "__main__":
    cli()