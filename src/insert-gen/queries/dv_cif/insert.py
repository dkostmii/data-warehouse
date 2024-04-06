from random import seed

from faker import Faker
from pypika import Query

import tables.dv_cif as tables
from contexts.dv_cif import Context
from seeds.dv_cif import seed_root

Faker.seed(123)
seed(123)

ctx = Context()
seed_root(context=ctx)

statements = [
    Query.into(tables.hub_candidate_table)
    .columns("candidate_id")
    .insert(*[(c.candidate_id,) for c in ctx.hub_candidates]),
    Query.into(tables.sat_candidate_info_table)
    .columns("candidate_id", "employment_status")
    .insert(
        *[(ci.candidate_id, ci.employment_status) for ci in ctx.sat_candidate_infos]
    ),
    Query.into(tables.sat_candidate_contacts_table)
    .columns(
        "candidate_id",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "birth_date",
        "passport_code",
        "driver_license_code",
        "location",
    )
    .insert(
        *[
            (
                c.candidate_id,
                c.first_name,
                c.last_name,
                c.phone_number,
                c.email,
                c.birth_date,
                c.passport_code,
                c.driver_license_code,
                c.location,
            )
            for c in ctx.sat_candidate_contacts
        ]
    ),
    Query.into(tables.hub_company_table)
    .columns("company_id")
    .insert(*[(c.company_id,) for c in ctx.hub_companies]),
    Query.into(tables.sat_company_info_table)
    .columns("company_id", "name", "phone_number", "location")
    .insert(
        *[
            (ci.company_id, ci.name, ci.phone_number, ci.location)
            for ci in ctx.sat_company_infos
        ]
    ),
    Query.into(tables.sat_production_branch_table)
    .columns("company_id", "name")
    .insert(*[(pb.company_id, pb.name) for pb in ctx.sat_production_branches]),
    Query.into(tables.link_vacancy_table)
    .columns("vacancy_id", "company_id", "candidate_id")
    .insert(
        *[(v.vacancy_id, v.company_id, v.candidate_id) for v in ctx.link_vacancies]
    ),
    Query.into(tables.sat_vacancy_info_table)
    .columns("vacancy_id", "name", "salary", "additional_info")
    .insert(
        *[
            (vi.vacancy_id, vi.name, vi.salary, vi.additional_info)
            for vi in ctx.sat_vacancy_infos
        ]
    ),
    Query.into(tables.sat_vacancy_category_table)
    .columns("vacancy_id", "name")
    .insert(*[(vc.vacancy_id, vc.name) for vc in ctx.sat_vacancy_categories]),
]
