import pathlib
from os import makedirs, stat
from os.path import dirname, exists, join
from sys import argv

from helpers.statements import separate_statements
from queries.dv_cif.create import statements as dv_cif_create_statements
from queries.dv_cif.drop import statements as dv_cif_drop_statements
from queries.dv_cif.insert import statements as dv_cif_insert_statements
from queries.dv_star.create import statements as dv_star_create_statements
from queries.dv_star.drop import statements as dv_star_drop_statements
from queries.dv_star.insert import statements as dv_star_insert_statements

main_dir = pathlib.Path(__file__).parent.resolve()
queries_dir = join(main_dir, "queries")
out_dir = "generated"


def write_query_file(file_name: str, statements: list[str]):
    force = "-f" in argv
    makedirs(dirname(file_name), exist_ok=True)

    file_is_empty = not exists(file_name) or stat(file_name).st_size == 0

    if file_is_empty or force and not file_is_empty:
        with open(file_name, mode="w") as f:
            print(f"Writing queries to {file_name}...")
            stripped_statements = map(lambda s: s.strip(), statements)
            f.write("\n".join(stripped_statements))
    else:
        print(f"File {file_name} is not empty and -f flag is not provided. Skipping...")


def copy_query_file(file_name: str, dest_file_name: str):
    with open(file_name, "r") as f:
        statements = f.readlines()
        write_query_file(dest_file_name, statements)


def main():
    queries = [
        (join(out_dir, "dv_cif", "create.sql"), dv_cif_create_statements),
        (join(out_dir, "dv_cif", "insert.sql"), dv_cif_insert_statements),
        (join(out_dir, "dv_cif", "drop.sql"), dv_cif_drop_statements),
        (join(out_dir, "dv_star", "create.sql"), dv_star_create_statements),
        (join(out_dir, "dv_star", "insert.sql"), dv_star_insert_statements),
        (join(out_dir, "dv_star", "drop.sql"), dv_star_drop_statements),
    ]

    sql_files = [
        (
            join(queries_dir, "dv_cif", "select.sql"),
            join(out_dir, "dv_cif", "select.sql"),
        ),
        (
            join(queries_dir, "dv_star", "select.sql"),
            join(out_dir, "dv_star", "select.sql"),
        ),
    ]

    for file_name, statements in queries:
        write_query_file(file_name, separate_statements(statements, ";"))

    for file_name, dest_file_name in sql_files:
        copy_query_file(file_name, dest_file_name)

    print("Done.")


if __name__ == "__main__":
    main()
