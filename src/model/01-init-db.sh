#!/bin/bash

psql -v ON_ERROR_STOP=1 --username "docker" --dbname "docker" <<-EOSQL
	CREATE DATABASE hello_world;
EOSQL

psql -v ON_ERROR_STOP=1 --username "docker" --dbname "hello_world" <<-EOSQL
	CREATE TABLE hello_world
	(
		id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
		message VARCHAR(50) NOT NULL
	)
EOSQL
