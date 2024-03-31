from pypika import Query, Column, CustomFunction
from helpers.create_query import MultipleFKCreateQueryBuilder

gen_random_uuid = CustomFunction("gen_random_uuid")

statements = [
    Query
        .create_table("Production_Branch")
        .columns(
            Column("production_branch_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False)
        )
        .primary_key("production_branch_id"),
    Query
        .create_table("Location")
        .columns(
            Column("location_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False)
        )
        .primary_key("location_id"),
    Query
        .create_table("Vacancy_Category")
        .columns(
            Column("vacancy_category_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False)
        )
        .primary_key("vacancy_category_id"),
    Query
        .create_table("Phone_number")
        .columns(
            Column("phone_number_id", "UUID", default=gen_random_uuid()),
            Column("phone_number", "VARCHAR(22)", nullable=False)
        )
        .primary_key("phone_number_id"),
    MultipleFKCreateQueryBuilder(Query.create_table("Company"))
        .columns(
            Column("company_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False),
            Column("phone_number_id", "UUID", nullable=False),
            Column("location_id", "INT", nullable=False),
            Column("production_branch_id", "INT", nullable=False),
        )
        .primary_key("company_id")
        .foreign_key(["location_id"], "Location", ["location_id"])
        .foreign_key(["production_branch_id"], "Production_Branch", ["production_branch_id"])
        .foreign_key(["phone_number_id"], "Phone_number", ["phone_number_id"]),
    MultipleFKCreateQueryBuilder(Query.create_table("Vacancy"))
        .columns(
            Column("vacancy_id", "UUID", default=gen_random_uuid()),
            Column("name", "VARCHAR(100)", nullable=False),
            Column("company_id", "UUID", nullable=False),
            Column("salary", "NUMERIC(6,0)", nullable=False),
            Column("vacancy_category_id", "UUID", nullable=False),
            Column("additional_info", "VARCHAR(200)", default="")
        )
        .primary_key("vacancy_id")
        .foreign_key(["company_id"], "Company", ["company_id"])
        .foreign_key(["vacancy_category_id"], "Vacancy_Category", ["vacancy_category_id"]),
    MultipleFKCreateQueryBuilder(Query.create_table("Candidate"))
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
            Column("vacancy_id", "UUID", nullable=False)
        )
        .primary_key("candidate_id")
        .foreign_key(["vacancy_id"], "Vacancy", ["vacancy_id"])
        .foreign_key(["location_id"], "Location", ["location_id"])
        .foreign_key(["phone_number_id"], "Phone_number", ["phone_number_id"])
]

statements = list(map(str, statements))