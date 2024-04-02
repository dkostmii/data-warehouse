from pypika import Column, CustomFunction, Query

from helpers.create_query import MultipleFKCreateQueryBuilder
import tables

gen_random_uuid = CustomFunction("gen_random_uuid")

statements = [
    Query.create_table(tables.production_branch_table.get_table_name())
    .columns(
        Column("production_branch_id", "UUID", default=gen_random_uuid()),
        Column("name", "VARCHAR(100)", nullable=False),
    )
    .primary_key("production_branch_id"),
    Query.create_table(tables.location_table.get_table_name())
    .columns(
        Column("location_id", "UUID", default=gen_random_uuid()),
        Column("name", "VARCHAR(100)", nullable=False),
    )
    .primary_key("location_id"),
    Query.create_table(tables.vacancy_category_table.get_table_name())
    .columns(
        Column("vacancy_category_id", "UUID", default=gen_random_uuid()),
        Column("name", "VARCHAR(100)", nullable=False),
    )
    .primary_key("vacancy_category_id"),
    Query.create_table(tables.phone_number_table.get_table_name())
    .columns(
        Column("phone_number_id", "UUID", default=gen_random_uuid()),
        Column("phone_number", "VARCHAR(22)", nullable=False),
    )
    .primary_key("phone_number_id"),
    MultipleFKCreateQueryBuilder(Query.create_table(tables.company_table.get_table_name()))
    .columns(
        Column("company_id", "UUID", default=gen_random_uuid()),
        Column("name", "VARCHAR(100)", nullable=False),
        Column("phone_number_id", "UUID", nullable=False),
        Column("location_id", "UUID", nullable=False),
        Column("production_branch_id", "UUID", nullable=False),
    )
    .primary_key("company_id")
    .foreign_key(["location_id"], tables.location_table, ["location_id"])
    .foreign_key(
        ["production_branch_id"], tables.production_branch_table, ["production_branch_id"]
    )
    .foreign_key(["phone_number_id"], tables.phone_number_table, ["phone_number_id"]),
    MultipleFKCreateQueryBuilder(Query.create_table(tables.vacancy_table.get_table_name()))
    .columns(
        Column("vacancy_id", "UUID", default=gen_random_uuid()),
        Column("name", "VARCHAR(100)", nullable=False),
        Column("company_id", "UUID", nullable=False),
        Column("salary", "NUMERIC(6,0)", nullable=False),
        Column("vacancy_category_id", "UUID", nullable=False),
        Column("additional_info", "VARCHAR(200)", default=""),
    )
    .primary_key("vacancy_id")
    .foreign_key(["company_id"], tables.company_table, ["company_id"])
    .foreign_key(["vacancy_category_id"], tables.vacancy_category_table, ["vacancy_category_id"]),
    MultipleFKCreateQueryBuilder(Query.create_table(tables.candidate_table.get_table_name()))
    .columns(
        Column("candidate_id", "UUID", default=gen_random_uuid()),
        Column("first_name", "VARCHAR(50)", nullable=False),
        Column("last_name", "VARCHAR(70)", nullable=False),
        Column("phone_number_id", "UUID", nullable=False),
        Column("email", "VARCHAR(80)", nullable=False),
        Column("birth_date", "DATE", nullable=False),
        Column("location_id", "UUID", nullable=False),
        Column("passport_code", "VARCHAR(9)", nullable=False),
        Column("driver_license_code", "VARCHAR(9)", nullable=False),
        Column("vacancy_id", "UUID", nullable=False),
        Column("employment_status", "VARCHAR(15)", nullable=False),
    )
    .primary_key("candidate_id")
    .foreign_key(["vacancy_id"], tables.vacancy_table, ["vacancy_id"])
    .foreign_key(["location_id"], tables.location_table, ["location_id"])
    .foreign_key(["phone_number_id"], tables.phone_number_table, ["phone_number_id"]),
]

statements = list(map(lambda stmt: str(stmt) + ";", statements))
