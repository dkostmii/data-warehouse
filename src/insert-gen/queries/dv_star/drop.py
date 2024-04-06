from pypika import Query

import tables.dv_star as tables

statements = [
    Query.drop_table(tables.sat_candidate_application_info_table),
    Query.drop_table(tables.sat_company_table),
    Query.drop_table(tables.sat_producion_branch_table),
    Query.drop_table(tables.sat_vacancy_category_table),
    Query.drop_table(tables.sat_vacancy_table),
    Query.drop_table(tables.hub_candidate_application_table),
]
