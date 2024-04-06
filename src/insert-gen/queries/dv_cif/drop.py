from pypika import Query

import tables.dv_cif as tables

statements = [
    Query.drop_table(tables.sat_vacancy_category_table),
    Query.drop_table(tables.sat_vacancy_info_table),
    Query.drop_table(tables.link_vacancy_table),
    Query.drop_table(tables.sat_candidate_contacts_table),
    Query.drop_table(tables.sat_candidate_info_table),
    Query.drop_table(tables.hub_candidate_table),
    Query.drop_table(tables.sat_company_info_table),
    Query.drop_table(tables.sat_production_branch_table),
    Query.drop_table(tables.hub_company_table),
]
