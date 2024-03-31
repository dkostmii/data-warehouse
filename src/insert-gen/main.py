from create import statements
from os import makedirs, stat
from os.path import join, exists
from sys import argv

out_dir = "generated"

def main():
    force = '-f' in argv

    makedirs(out_dir, exist_ok=True)
    create_sql_file = join(out_dir, "create.sql")
    create_sql_is_empty = not exists(create_sql_file) or stat(create_sql_file).st_size == 0

    if create_sql_is_empty or force and not create_sql_is_empty:
        with open(create_sql_file, mode='w') as f:
            print(f"Writing to {create_sql_file}...")
            f.write("\n".join(statements))
    else:
        print(f"File {create_sql_file} is not empty and -f flag is not provided. Skipping...")

    print("Done.")

if __name__ == "__main__":
    main()
