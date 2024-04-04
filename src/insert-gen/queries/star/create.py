from pypika import Column, CustomFunction, Query
from pypika.functions import Now as NOW

from helpers.create_query import MultipleFKCreateQueryBuilder
import tables

gen_random_uuid = CustomFunction("gen_random_uuid")


statements = [
    Query.create_table(tables.location_table)
        .columns(
            Column("location_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False)
        )
        .primary_key("location_id"),
    Query.create_table(tables.vacancy_table)
        .columns(
            Column("vacancy_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False),
            Column("salary", "NUMERIC(6,0)", nullable=False),
            Column("additional_info", "VARCHAR(200)", default="")
        )
        .primary_key("vacancy_id"),
    Query.create_table(tables.vacancy_category_table)
        .columns(
            Column("vacancy_category_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False)
        )
        .primary_key("vacancy_category_id"),
    Query.create_table(tables.company_table)
        .columns(
            Column("company_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False),
            Column("phone_number", "VARCHAR(22)", nullable=False)
        )
        .primary_key("company_id"),
    Query.create_table(tables.production_branch_table)
        .columns(
            Column("production_branch_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False)
        )
        .primary_key("production_branch_id"),
    Query.create_table(tables.employment_status_table)
        .columns(
            Column("employment_status_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False)
        )
        .primary_key("employment_status_id"),
    MultipleFKCreateQueryBuilder(Query.create_table(tables.candidate_application_table))
        .columns(
            Column("candidate_application_id", "UUID", default=gen_random_uuid()),
            Column("first_name", "VARCHAR(100)", nullable=False),
            Column("last_name", "VARCHAR(100)", nullable=False),
            Column("phone_number", "VARCHAR(22)", nullable=False),
            Column("email", "VARCHAR(80)", nullable=False),
            Column("birth_date", "DATE", nullable=False),
            Column("passport_code", "VARCHAR(9)", nullable=False),
            Column("driver_license_code", "VARCHAR(9)", nullable=False),
            Column("candidate_location_id", "UUID", nullable=False),
            Column("vacancy_id", "UUID", nullable=False),
            Column("vacancy_category_id", "UUID", nullable=False),
            Column("company_id", "UUID", nullable=False),
            Column("company_location_id", "UUID", nullable=False),
            Column("production_branch_id", "UUID", nullable=False),
            Column("employment_status_id", "UUID", nullable=False),
            Column("created_at", "TIME", default=NOW())
        )
        .primary_key("candidate_application_id")
        .foreign_key(["candidate_location_id"], tables.location_table, ["location_id"])
        .foreign_key(["vacancy_id"], tables.vacancy_table, ["vacancy_id"])
        .foreign_key(["vacancy_category_id"], tables.vacancy_category_table, ["vacancy_category_id"])
        .foreign_key(["company_id"], tables.company_table, ["company_id"])
        .foreign_key(["company_location_id"], tables.location_table, ["location_id"])
        .foreign_key(["production_branch_id"], tables.production_branch_table, ["production_branch_id"])
        .foreign_key(["employment_status_id"], tables.employment_status_table, ["employment_status_id"])
]