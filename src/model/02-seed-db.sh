#!/bin/bash

psql -v ON_ERROR_STOP=1 --username "docker" --dbname "hello_world" <<-EOSQL
	INSERT INTO hello_world (message)
	VALUES ('Hello, World!'), ('Привіт, Світе!');
EOSQL
