from random import seed

from faker import Faker
from pypika import Query

import tables
from contexts.snowflake import Context
from seeds.snowflake import seed_root

Faker.seed(123)
seed(123)

ctx = Context()
seed_root(context=ctx)

statements = [
    Query.into(tables.location_table)
    .columns("location_id", "name")
    .insert(*[(loc.location_id, loc.name) for loc in ctx.locations]),
    Query.into(tables.production_branch_table)
    .columns("production_branch_id", "name")
    .insert(*[(pb.production_branch_id, pb.name) for pb in ctx.production_branches]),
    Query.into(tables.company_table)
    .columns("company_id", "name", "phone_number", "production_branch_id")
    .insert(
        *[
            (c.company_id, c.name, c.phone_number, c.production_branch_id)
            for c in ctx.companies
        ]
    ),
    Query.into(tables.vacancy_category_table)
    .columns("vacancy_category_id", "name")
    .insert(*[(vc.vacancy_category_id, vc.name) for vc in ctx.vacancy_categories]),
    Query.into(tables.vacancy_table)
    .columns("vacancy_id", "name", "salary", "additional_info", "vacancy_category_id")
    .insert(
        *[
            (v.vacancy_id, v.name, v.salary, v.additional_info, v.vacancy_category_id)
            for v in ctx.vacancies
        ]
    ),
    Query.into(tables.employment_status_table)
    .columns("employment_status_id", "name")
    .insert(*[(es.employment_status_id, es.name) for es in ctx.employment_statuses]),
    Query.into(tables.candidate_application_table)
    .columns(
        "candidate_application_id",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "birth_date",
        "passport_code",
        "driver_license_code",
        "candidate_location_id",
        "vacancy_id",
        "company_id",
        "company_location_id",
        "employment_status_id",
        "created_at",
    )
    .insert(
        *[
            (
                ca.candidate_application_id,
                ca.first_name,
                ca.last_name,
                ca.phone_number,
                ca.email,
                ca.birth_date,
                ca.passport_code,
                ca.driver_license_code,
                ca.candidate_location_id,
                ca.vacancy_id,
                ca.company_id,
                ca.company_location_id,
                ca.employment_status_id,
                ca.created_at,
            )
            for ca in ctx.candidate_applications
        ]
    ),
]
