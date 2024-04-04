from os import makedirs, stat
from os.path import exists, join, dirname
from sys import argv

from queries.star.create import statements as star_create_statements
from queries.snowflake.create import statements as snowflake_create_statements
from queries.drop import statements as drop_statements

from helpers.statements import separate_statements

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
            f.write("\n".join(statements))
    else:
        print(
            f"File {file_name} is not empty and -f flag is not provided. Skipping..."
        )


def main():
    queries = [
        (join(out_dir, "star", "create.sql"), star_create_statements),
        (join(out_dir, "star", "drop.sql"), drop_statements),
        (join(out_dir, "snowflake", "create.sql"), snowflake_create_statements),
        (join(out_dir, "snowflake", "drop.sql"), drop_statements)
    ]

    for file_name, statements in queries:
        write_query_file(file_name, separate_statements(statements, ";"))

    print("Done.")


if __name__ == "__main__":
    main()
