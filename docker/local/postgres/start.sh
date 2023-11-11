#!/bin/bash
set -e

# Create a new user if it does not exist

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
EOSQL


# Create a new database if it does not exist and grant privileges

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE $POSTGRES_DB;
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $DB_USER;
EOSQL


# Connect to the new database and enable the Citus extension
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -d $POSTGRES_DB <<-EOSQL
    CREATE EXTENSION IF NOT EXISTS citus;
EOSQL