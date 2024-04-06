from pypika import Column, CustomFunction, Query
from pypika.functions import Now as NOW

import tables.dv_star as tables
from shared.dv.columns import load_date, record_source

gen_random_uuid = CustomFunction("gen_random_uuid")

statements = [
    Query.create_table(tables.hub_candidate_application_table)
    .columns(
        Column("candidate_application_id", "UUID", nullable=False),
        load_date,
        record_source,
    )
    .primary_key("candidate_application_id"),
    Query.create_table(tables.sat_candidate_application_info_table)
    .columns(
        Column("candidate_application_id", "UUID", nullable=False),
        Column("first_name", "VARCHAR(100)", nullable=False),
        Column("last_name", "VARCHAR(100)", nullable=False),
        Column("phone_number", "VARCHAR(22)", nullable=False),
        Column("email", "VARCHAR(80)", nullable=False),
        Column("birth_date", "DATE", nullable=False),
        Column("passport_code", "VARCHAR(9)", nullable=False),
        Column("driver_license_code", "VARCHAR(9)", nullable=False),
        Column("candidate_location", "VARCHAR(100)", nullable=False),
        Column("employment_status", "VARCHAR(100)", nullable=False),
        Column("created_at", "TIMESTAMP", default=NOW()),
        load_date,
        record_source,
    )
    .primary_key("candidate_application_id")
    .foreign_key(
        ["candidate_application_id"],
        tables.hub_candidate_application_table,
        ["candidate_application_id"],
    ),
    Query.create_table(tables.sat_vacancy_table)
    .columns(
        Column("candidate_application_id", "UUID", nullable=False),
        Column("name", "VARCHAR(100)", nullable=False),
        Column("salary", "NUMERIC(6,0)", nullable=False),
        Column("additional_info", "VARCHAR(200)", default=""),
        load_date,
        record_source,
    )
    .primary_key("candidate_application_id")
    .foreign_key(
        ["candidate_application_id"],
        tables.hub_candidate_application_table,
        ["candidate_application_id"],
    ),
    Query.create_table(tables.sat_vacancy_category_table)
    .columns(
        Column("candidate_application_id", "UUID", nullable=False),
        Column("name", "VARCHAR(100)", nullable=False),
    )
    .primary_key("candidate_application_id")
    .foreign_key(
        ["candidate_application_id"],
        tables.hub_candidate_application_table,
        ["candidate_application_id"],
    ),
    Query.create_table(tables.sat_company_table)
    .columns(
        Column("candidate_application_id", "UUID", nullable=False),
        Column("name", "VARCHAR(100)", nullable=False),
        Column("phone_number", "VARCHAR(22)", nullable=False),
        Column("company_location", "VARCHAR(100)", nullable=False),
        load_date,
        record_source,
    )
    .primary_key("candidate_application_id")
    .foreign_key(
        ["candidate_application_id"],
        tables.hub_candidate_application_table,
        ["candidate_application_id"],
    ),
    Query.create_table(tables.sat_producion_branch_table)
    .columns(
        Column("candidate_application_id", "UUID", nullable=False),
        Column("name", "VARCHAR(100)", nullable=False),
    )
    .primary_key("candidate_application_id")
    .foreign_key(
        ["candidate_application_id"],
        tables.hub_candidate_application_table,
        ["candidate_application_id"],
    ),
]
