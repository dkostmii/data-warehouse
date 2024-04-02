from random import seed

from faker import Faker
from pypika import Query

from context import Context
from seed import seed_root
import tables


Faker.seed(123)
seed(123)

ctx = Context()
seed_root(context=ctx)

statements = [
    Query.into(tables.production_branch_table)
    .columns("production_branch_id", "name")
    .insert(*[(pd.production_branch_id, pd.name) for pd in ctx.production_branches]),
    Query.into(tables.location_table)
    .columns("location_id", "name")
    .insert(*[(loc.location_id, loc.name) for loc in ctx.locations]),
    Query.into(tables.phone_number_table)
    .columns("phone_number_id", "phone_number")
    .insert(*[(pn.phone_number_id, pn.phone_number) for pn in ctx.phone_numbers]),
    Query.into(tables.company_table)
    .columns(
        "company_id", "name", "phone_number_id", "location_id", "production_branch_id"
    )
    .insert(
        *[
            (
                c.company_id,
                c.name,
                c.phone_number_id,
                c.location_id,
                c.production_branch_id,
            )
            for c in ctx.companies
        ]
    ),
    Query.into(tables.vacancy_category_table)
    .columns("vacancy_category_id", "name")
    .insert(*[(vc.vacancy_category_id, vc.name) for vc in ctx.vacancy_categories]),
    Query.into(tables.vacancy_table)
    .columns(
        "vacancy_id",
        "name",
        "company_id",
        "salary",
        "vacancy_category_id",
        "additional_info",
    )
    .insert(
        *[
            (
                v.vacancy_id,
                v.name,
                v.company_id,
                v.salary,
                v.vacancy_category_id,
                v.additional_info,
            )
            for v in ctx.vacancies
        ]
    ),
    Query.into(tables.candidate_table)
    .columns(
        "candidate_id",
        "first_name",
        "last_name",
        "phone_number_id",
        "email",
        "birth_date",
        "location_id",
        "passport_code",
        "driver_license_code",
        "vacancy_id",
        "employment_status",
    )
    .insert(
        *[
            (
                c.candidate_id,
                c.first_name,
                c.last_name,
                c.phone_number_id,
                c.email,
                c.birth_date,
                c.location_id,
                c.passport_code,
                c.driver_license_code,
                c.vacancy_id,
                c.employment_status,
            )
            for c in ctx.candidates
        ]
    ),
]

statements = list(map(lambda stmt: str(stmt) + ";", statements))
