from pypika import Query

import tables

statements = [
    Query.drop_table(tables.candidate_application_table),
    Query.drop_table(tables.employment_status_table),
    Query.drop_table(tables.company_table),
    Query.drop_table(tables.production_branch_table),
    Query.drop_table(tables.vacancy_table),
    Query.drop_table(tables.vacancy_category_table),
    Query.drop_table(tables.location_table),
]
