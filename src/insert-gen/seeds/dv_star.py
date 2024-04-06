from random import choice, randint, random
from types import SimpleNamespace
from typing import Any
from uuid import UUID

import yaml
from faker import Faker

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

import models.dv_star as models
from contexts.dv_star import Context
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

    vacancies_data: list[dict[str, Any]] = []
    with open("datasets/vacancies.yml") as f:
        vacancies_data = yaml.load(f.read(), Loader=Loader)

    while len(context.hub_candidate_applications) < CANDIDATE_COUNT:
        candidate = seed_candidate_application(
            vacancies_data=vacancies_data, context=context
        )
        context.hub_candidate_applications.append(candidate)


def seed_candidate_application(
    vacancies_data: list[dict[str, Any]], context: Context
) -> models.HubCandidateApplication:
    candidate_application_id = get_random_uuid()
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

    vacancy_data = choice(vacancies_data)
    vacancy = seed_vacancy(candidate_application_id=candidate_application_id, vacancy_data=vacancy_data, context=context)
    context.sat_vacancies.append(vacancy)

    employment_status = context.shared_generators["employment_status"].get()

    candidate_application_info = models.SatCandidateApplicationInfo(
        candidate_application_id=candidate_application_id,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email,
        birth_date=birth_date,
        passport_code=passport_code,
        driver_license_code=driver_license_code,
        candidate_location=location,
        employment_status=employment_status,
        created_at=fake.date_time_between(start_date="-6m"),
    )

    context.sat_candidate_application_infos.append(candidate_application_info)

    return models.HubCandidateApplication(
        candidate_application_id=candidate_application_id
    )


def seed_vacancy(
    candidate_application_id: UUID, vacancy_data: dict[str, Any], context: Context
) -> models.SatVacancy:
    vacancy_id = get_random_uuid()
    name = vacancy_data["name"]

    company = seed_company(
        candidate_application_id=candidate_application_id,
        company_data=vacancy_data["company"],
        context=context,
    )
    context.sat_companies.append(company)

    salary = randint(8_500, 120_000)

    vacancy_category_name = vacancy_data["vacancy_category"]

    additional_info = ""

    if random() < 0.33:
        additional_info = fake.text(max_nb_chars=200)

    vacancy_category = models.SatVacancyCategory(
        candidate_application_id=candidate_application_id, name=vacancy_category_name
    )

    context.sat_vacancy_categories.append(vacancy_category)

    return models.SatVacancy(
        candidate_application_id=candidate_application_id, name=name, salary=salary, additional_info=additional_info
    )


def seed_company(
    candidate_application_id: UUID, company_data: dict[str, Any], context: Context
) -> models.SatCompany:
    name = company_data["name"]

    phone_number = context.shared_unique_generators["phone_number"].get_unique()

    location = company_data["location"]
    production_branch_name = company_data["production_branch"]

    production_branch = models.SatProductionBranch(
        candidate_application_id=candidate_application_id, name=production_branch_name
    )

    context.sat_production_branches.append(production_branch)

    return models.SatCompany(
        candidate_application_id=candidate_application_id,
        name=name,
        phone_number=phone_number,
        company_location=location,
    )
