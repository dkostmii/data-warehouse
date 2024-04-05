from os import makedirs, stat
from os.path import exists, join, dirname
from sys import argv
import pathlib

from queries.star.create import statements as star_create_statements
from queries.star.insert import statements as star_insert_statements
from queries.snowflake.create import statements as snowflake_create_statements
from queries.snowflake.insert import statements as snowflake_insert_statements
from queries.drop import statements as drop_statements

from helpers.statements import separate_statements

main_dir = pathlib.Path(__file__).parent.resolve()
queries_dir = join(main_dir, "queries")
out_dir = "generated"


def write_query_file(file_name: str, statements: list[str]):
    force = "-f" in argv
    makedirs(dirname(file_name), exist_ok=True)

    file_is_empty = (
        not exists(file_name) or stat(file_name).st_size == 0
    )

    if file_is_empty or force and not file_is_empty:
        with open(file_name, mode="w") as f:
            print(f"Writing queries to {file_name}...")
            statements = map(lambda s: s.strip(), statements)
            f.write("\n".join(statements))
    else:
        print(
            f"File {file_name} is not empty and -f flag is not provided. Skipping..."
        )


def copy_query_file(file_name: str, dest_file_name: str):
    with open(file_name, 'r') as f:
        statements = f.readlines()
        write_query_file(dest_file_name, statements)


def main():
    queries = [
        (join(out_dir, "star", "create.sql"), star_create_statements),
        (join(out_dir, "star", "insert.sql"), star_insert_statements),
        (join(out_dir, "star", "drop.sql"), drop_statements),
        (join(out_dir, "snowflake", "create.sql"), snowflake_create_statements),
        (join(out_dir, "snowflake", "insert.sql"), snowflake_insert_statements),
        (join(out_dir, "snowflake", "drop.sql"), drop_statements)
    ]

    sql_files = [
        (join(queries_dir, "star", "select.sql"), join(out_dir, "star", "select.sql")),
        (join(queries_dir, "snowflake", "select.sql"), join(out_dir, "snowflake", "select.sql"))
    ]

    for file_name, statements in queries:
        write_query_file(file_name, separate_statements(statements, ";"))

    for file_name, dest_file_name in sql_files:
        copy_query_file(file_name, dest_file_name)

    print("Done.")


if __name__ == "__main__":
    main()
