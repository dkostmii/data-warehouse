from random import seed

from faker import Faker
from pypika import Query

import tables.dv_star as tables
from contexts.dv_star import Context
from seeds.dv_star import seed_root

Faker.seed(123)
seed(123)

ctx = Context()
seed_root(context=ctx)

statements = [
    Query.into(tables.hub_candidate_application_table)
    .columns("candidate_application_id")
    .insert(*[(ca.candidate_application_id,) for ca in ctx.hub_candidate_applications]),
    Query.into(tables.sat_candidate_application_info_table)
    .columns(
        "candidate_application_id",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "birth_date",
        "passport_code",
        "driver_license_code",
        "candidate_location",
        "employment_status",
        "created_at",
    )
    .insert(
        *[
            (
                cai.candidate_application_id,
                cai.first_name,
                cai.last_name,
                cai.phone_number,
                cai.email,
                cai.birth_date,
                cai.passport_code,
                cai.driver_license_code,
                cai.candidate_location,
                cai.employment_status,
                cai.created_at,
            )
            for cai in ctx.sat_candidate_application_infos
        ]
    ),
    Query.into(tables.sat_vacancy_table)
    .columns("candidate_application_id", "name", "salary", "additional_info")
    .insert(
        *[
            (v.candidate_application_id, v.name, v.salary, v.additional_info)
            for v in ctx.sat_vacancies
        ]
    ),
    Query.into(tables.sat_vacancy_category_table)
    .columns("candidate_application_id", "name")
    .insert(
        *[(vc.candidate_application_id, vc.name) for vc in ctx.sat_vacancy_categories]
    ),
    Query.into(tables.sat_company_table)
    .columns("candidate_application_id", "name", "phone_number", "company_location")
    .insert(
        *[
            (c.candidate_application_id, c.name, c.phone_number, c.company_location)
            for c in ctx.sat_companies
        ]
    ),
    Query.into(tables.sat_producion_branch_table)
    .columns("candidate_application_id", "name")
    .insert(
        *[(pb.candidate_application_id, pb.name) for pb in ctx.sat_production_branches]
    ),
]
