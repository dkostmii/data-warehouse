from pypika import Column, CustomFunction, Query

import tables.dv_cif as tables
from helpers.create_query import MultipleFKCreateQueryBuilder
from shared.dv.columns import load_date, record_source

gen_random_uuid = CustomFunction("gen_random_uuid")

statements = [
    Query.create_table(tables.hub_candidate_table)
    .columns(
        Column("candidate_id", "UUID", default=gen_random_uuid()),
        load_date,
        record_source,
    )
    .primary_key("candidate_id"),
    Query.create_table(tables.sat_candidate_info_table)
    .columns(
        Column("candidate_id", "UUID", nullable=False),
        Column("employment_status", "VARCHAR(100)", nullable=False),
        load_date,
        record_source,
    )
    .primary_key("candidate_id")
    .foreign_key(["candidate_id"], tables.hub_candidate_table, ["candidate_id"]),
    Query.create_table(tables.sat_candidate_contacts_table)
    .columns(
        Column("candidate_id", "UUID", nullable=False),
        Column("first_name", "VARCHAR(100)", nullable=False),
        Column("last_name", "VARCHAR(100)", nullable=False),
        Column("phone_number", "VARCHAR(22)", nullable=False),
        Column("email", "VARCHAR(80)", nullable=False),
        Column("birth_date", "DATE", nullable=False),
        Column("passport_code", "VARCHAR(9)", nullable=False),
        Column("driver_license_code", "VARCHAR(9)", nullable=False),
        Column("location", "VARCHAR(100)", nullable=False),
        load_date,
        record_source,
    )
    .primary_key("candidate_id")
    .foreign_key(["candidate_id"], tables.hub_candidate_table, ["candidate_id"]),
    Query.create_table(tables.hub_company_table)
    .columns(
        Column("company_id", "UUID", default=gen_random_uuid()),
        load_date,
        record_source,
    )
    .primary_key("company_id"),
    Query.create_table(tables.sat_company_info_table)
    .columns(
        Column("company_id", "UUID", nullable=False),
        Column("name", "VARCHAR(100)", nullable=False),
        Column("phone_number", "VARCHAR(22)", nullable=False),
        Column("location", "VARCHAR(100)", nullable=False),
        load_date,
        record_source,
    )
    .primary_key("company_id")
    .foreign_key(["company_id"], tables.hub_company_table, ["company_id"]),
    Query.create_table(tables.sat_production_branch_table)
    .columns(
        Column("company_id", "UUID", nullable=False),
        Column("name", "VARCHAR(100)", nullable=False),
        load_date,
        record_source,
    )
    .primary_key("company_id")
    .foreign_key(["company_id"], tables.hub_company_table, ["company_id"]),
    MultipleFKCreateQueryBuilder(Query.create_table(tables.link_vacancy_table))
    .columns(
        Column("vacancy_id", "UUID", default=gen_random_uuid()),
        Column("company_id", "UUID", nullable=False),
        Column("candidate_id", "UUID", nullable=False),
        load_date,
        record_source,
    )
    .primary_key("vacancy_id")
    .foreign_key(["company_id"], tables.hub_company_table, ["company_id"])
    .foreign_key(["candidate_id"], tables.hub_candidate_table, ["candidate_id"]),
    Query.create_table(tables.sat_vacancy_info_table)
    .columns(
        Column("vacancy_id", "UUID", nullable=False),
        Column("name", "VARCHAR(100)", nullable=False),
        Column("salary", "NUMERIC(6,0)", nullable=False),
        Column("additional_info", "VARCHAR(200)", default=""),
        load_date,
        record_source,
    )
    .primary_key("vacancy_id")
    .foreign_key(["vacancy_id"], tables.link_vacancy_table, ["vacancy_id"]),
    Query.create_table(tables.sat_vacancy_category_table)
    .columns(
        Column("vacancy_id", "UUID", nullable=False),
        Column("name", "VARCHAR(100)", nullable=False),
        load_date,
        record_source,
    )
    .primary_key("vacancy_id")
    .foreign_key(["vacancy_id"], tables.link_vacancy_table, ["vacancy_id"]),
]
