from random import choice, randint, random
from types import SimpleNamespace
from typing import Any

import yaml
from faker import Faker

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

import models.snowflake as models
from contexts.snowflake import Context
from generators.id import get_random_uuid
from generators.text import (
    EmailGenerator,
    PhoneNumberGenerator,
    get_driver_license_code,
    get_passport_code,
)
from helpers.unique_generator import UniqueGenerator

fake = Faker("uk_UA")
CANDIDATE_COUNT = 50


def seed_root(context: Context):
    context.shared_unique_generators["phone_number"] = UniqueGenerator(
        gen=PhoneNumberGenerator()
    )
    context.shared_unique_generators["email"] = UniqueGenerator(gen=EmailGenerator())
    context.shared_unique_generators["passport_code"] = UniqueGenerator(
        gen=SimpleNamespace(get=get_passport_code)
    )
    context.shared_unique_generators["driver_license_code"] = UniqueGenerator(
        gen=SimpleNamespace(get=get_driver_license_code)
    )

    with open("datasets/employment_status.txt") as f:
        employment_statuses: list[str] = f.readlines()
        for es_name in employment_statuses:
            context.employment_statuses.append(
                models.EmploymentStatus(
                    employment_status_id=get_random_uuid(),
                    name=es_name.strip()
                )
            )

    with open("datasets/locations.txt") as f:
        location_id = get_random_uuid()
        location_name = f.readline()
        context.locations.append(
            models.Location(location_id=location_id, name=location_name)
        )

    vacancies_data: list[dict[str, Any]] = []
    with open("datasets/vacancies.yml") as f:
        vacancies_data = yaml.load(f.read(), Loader=Loader)

    while len(context.candidate_applications) < CANDIDATE_COUNT:
        candidate = seed_candidate_application(vacancies_data=vacancies_data, context=context)
        context.candidate_applications.append(candidate)


def seed_candidate_application(vacancies_data: list[dict[str, Any]], context: Context) -> models.CandidateApplication:
    candidate_id = get_random_uuid()
    sex = "male" if random() < 0.5 else "female"
    first_name = fake.first_name_male() if sex == "male" else fake.first_name_female()
    last_name = fake.last_name_male() if sex == "male" else fake.last_name_female()

    phone_number = context.shared_unique_generators["phone_number"].get_unique()

    email = context.shared_unique_generators["email"].get_unique(
        first_name=first_name, last_name=last_name
    )
    birth_date = fake.date_between(start_date="-40y", end_date="-18y")

    location = choice(context.locations)

    passport_code_is_old_format = random() < 0.4
    passport_code = context.shared_unique_generators["passport_code"].get_unique(old_format=passport_code_is_old_format)
    driver_license_code = context.shared_unique_generators[
        "driver_license_code"
    ].get_unique()

    vacancy_data = choice(vacancies_data)

    vacancy: models.Vacancy | None = next(
        filter(lambda v: v.name == vacancy_data["name"], context.vacancies),
        None
    )

    if vacancy is None:
        vacancy = seed_vacancy(vacancy_data=vacancy_data, context=context)
        context.vacancies.append(vacancy)

    employment_status = choice(context.employment_statuses)

    return models.CandidateApplication(
        candidate_application_id=candidate_id,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email,
        birth_date=birth_date,
        passport_code=passport_code,
        driver_license_code=driver_license_code,
        candidate_location=location,
        vacancy=vacancy,
        company=vacancy.company,
        company_location=vacancy.company.company_location,
        employment_status=employment_status,
        created_at=fake.date_time_between(start_date='-6m')
    )


def seed_vacancy(vacancy_data: dict[str, Any], context: Context) -> models.Vacancy:
    vacancy_id = get_random_uuid()
    name = vacancy_data["name"]

    company: models.Company | None = next(
        filter(lambda c: c.name == vacancy_data["company"]["name"], context.companies),
        None,
    )

    if company is None:
        company = seed_company(company_data=vacancy_data["company"], context=context)
        context.companies.append(company)

    salary = randint(8_500, 120_000)

    vacancy_category_name = vacancy_data["vacancy_category"]
    vacancy_category: models.VacancyCategory | None = next(
        filter(lambda c: c.name == vacancy_category_name, context.vacancy_categories),
        None,
    )

    if vacancy_category is None:
        vacancy_category_id = get_random_uuid()
        vacancy_category = models.VacancyCategory(
            vacancy_category_id=vacancy_category_id, name=vacancy_category_name
        )
        context.vacancy_categories.append(vacancy_category)

    additional_info = ""

    if random() < 0.33:
        additional_info = fake.text(max_nb_chars=200)

    return models.Vacancy(
        vacancy_id=vacancy_id,
        name=name,
        salary=salary,
        additional_info=additional_info,
        company=company,
        vacancy_category=vacancy_category
    )


def seed_company(company_data: dict[str, Any], context: Context) -> models.Company:
    company_id = get_random_uuid()
    name = company_data["name"]

    phone_number = context.shared_unique_generators["phone_number"].get_unique()

    location_name = company_data["location"]
    location: models.Location | None = next(
        filter(lambda loc: loc.name == location_name, context.locations), None
    )

    if location is None:
        location_id = get_random_uuid()
        location = models.Location(location_id=location_id, name=location_name)
        context.locations.append(location)

    production_branch_name = company_data["production_branch"]
    production_branch: models.ProductionBranch | None = next(
        filter(
            lambda pb: pb.name == production_branch_name, context.production_branches
        ),
        None,
    )

    if production_branch is None:
        production_branch_id = get_random_uuid()
        production_branch = models.ProductionBranch(
            production_branch_id=production_branch_id, name=production_branch_name
        )
        context.production_branches.append(production_branch)

    return models.Company(
        company_id=company_id,
        name=name,
        phone_number=phone_number,
        production_branch=production_branch,
        company_location=location
    )