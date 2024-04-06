from random import choice, randint, random
from types import SimpleNamespace
from typing import Any

import yaml
from faker import Faker

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

import models.dv_cif as models
from contexts.dv_cif import Context
from generators.id import get_random_uuid
from generators.text import (EmailGenerator, EmploymentStatusGenerator,
                             LocationGenerator, PhoneNumberGenerator,
                             get_driver_license_code, get_passport_code)
from helpers.unique_generator import UniqueGenerator

fake = Faker("uk_UA")
CANDIDATE_COUNT = 50


def seed_root(context: Context):
    context.shared_unique_generators["phone_number"] = UniqueGenerator(
        gen=PhoneNumberGenerator()
    )
    context.shared_unique_generators["email"] = UniqueGenerator(gen=EmailGenerator())
    context.shared_generators["employment_status"] = EmploymentStatusGenerator()
    context.shared_generators["location"] = LocationGenerator()
    context.shared_unique_generators["passport_code"] = UniqueGenerator(
        gen=SimpleNamespace(get=get_passport_code)
    )
    context.shared_unique_generators["driver_license_code"] = UniqueGenerator(
        gen=SimpleNamespace(get=get_driver_license_code)
    )

    while len(context.hub_candidates) < CANDIDATE_COUNT:
        candidate = seed_candidate(context=context)
        context.hub_candidates.append(candidate)

    vacancies_data: list[dict[str, Any]] = []
    with open("datasets/vacancies.yml") as f:
        vacancies_data = yaml.load(f.read(), Loader=Loader)

    for vacancy_data in vacancies_data:
        vacancy = seed_vacancy(vacancy_data, context)
        context.link_vacancies.append(vacancy)


def seed_candidate(context: Context) -> models.HubCandidate:
    candidate_id = get_random_uuid()
    sex = "male" if random() < 0.5 else "female"
    first_name = fake.first_name_male() if sex == "male" else fake.first_name_female()
    last_name = fake.last_name_male() if sex == "male" else fake.last_name_female()

    phone_number = context.shared_unique_generators["phone_number"].get_unique()

    email = context.shared_unique_generators["email"].get_unique(
        first_name=first_name, last_name=last_name
    )
    birth_date = fake.date_between(start_date="-40y", end_date="-18y")

    location = context.shared_generators["location"].get()

    passport_code_is_old_format = random() < 0.4
    passport_code = context.shared_unique_generators["passport_code"].get_unique(
        old_format=passport_code_is_old_format
    )
    driver_license_code = context.shared_unique_generators[
        "driver_license_code"
    ].get_unique()

    employment_status = context.shared_generators["employment_status"].get()

    candidate_info = models.SatCandidateInfo(
        candidate_id=candidate_id, employment_status=employment_status
    )

    candidate_contacts = models.SatCandidateContacts(
        candidate_id=candidate_id,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email,
        birth_date=birth_date,
        location=location,
        passport_code=passport_code,
        driver_license_code=driver_license_code,
    )

    context.sat_candidate_infos.append(candidate_info)
    context.sat_candidate_contacts.append(candidate_contacts)

    return models.HubCandidate(candidate_id=candidate_id)


def seed_vacancy(vacancy_data: dict[str, Any], context: Context) -> models.LinkVacancy:
    vacancy_id = get_random_uuid()
    name = vacancy_data["name"]

    candidate_id = choice(context.hub_candidates).candidate_id

    company_info: models.SatCompanyInfo | None = next(
        filter(
            lambda ci: ci.name == vacancy_data["company"]["name"],
            context.sat_company_infos,
        ),
        None,
    )

    company: models.HubCompany | None = (
        next(
            filter(
                lambda c: c.company_id == company_info.company_id, context.hub_companies
            ),
            None,
        )
        if company_info is not None
        else None
    )

    if company is None:
        company = seed_company(vacancy_data["company"], context=context)
        context.hub_companies.append(company)

    salary = randint(8_500, 120_000)

    vacancy_category = vacancy_data["vacancy_category"]

    additional_info = ""

    if random() < 0.33:
        additional_info = fake.text(max_nb_chars=200)

    vacancy_info = models.SatVacancyInfo(
        vacancy_id=vacancy_id,
        name=name,
        salary=salary,
        additional_info=additional_info,
    )

    sat_vacancy_category = models.SatVacancyCategory(
        vacancy_id=vacancy_id, name=vacancy_category
    )

    context.sat_vacancy_infos.append(vacancy_info)
    context.sat_vacancy_categories.append(sat_vacancy_category)

    return models.LinkVacancy(
        vacancy_id=vacancy_id, company_id=company.company_id, candidate_id=candidate_id
    )


def seed_company(company_data: dict[str, Any], context: Context) -> models.HubCompany:
    company_id = get_random_uuid()
    name = company_data["name"]

    phone_number = context.shared_unique_generators["phone_number"].get_unique()

    location = company_data["location"]

    production_branch = company_data["production_branch"]

    company_info = models.SatCompanyInfo(
        company_id=company_id, name=name, phone_number=phone_number, location=location
    )

    sat_production_branch = models.SatProductionBranch(
        company_id=company_id, name=production_branch
    )

    context.sat_company_infos.append(company_info)
    context.sat_production_branches.append(sat_production_branch)

    return models.HubCompany(company_id=company_id)
