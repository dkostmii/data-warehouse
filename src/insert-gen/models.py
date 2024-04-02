from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class ProductionBranch:
    production_branch_id: UUID
    name: str


@dataclass
class Location:
    location_id: UUID
    name: str


@dataclass
class PhoneNumber:
    phone_number_id: UUID
    phone_number: str


@dataclass
class Company:
    company_id: UUID
    name: str
    phone_number: PhoneNumber
    location: Location
    production_branch: ProductionBranch

    @property
    def phone_number_id(self):
        return self.phone_number.phone_number_id

    @property
    def location_id(self):
        return self.location.location_id

    @property
    def production_branch_id(self):
        return self.production_branch.production_branch_id


@dataclass
class VacancyCategory:
    vacancy_category_id: UUID
    name: str


@dataclass
class Vacancy:
    vacancy_id: UUID
    name: str
    company: Company
    salary: float
    vacancy_category: VacancyCategory
    additional_info: str = ""

    @property
    def company_id(self):
        return self.company.company_id

    @property
    def vacancy_category_id(self):
        return self.vacancy_category.vacancy_category_id


@dataclass
class Candidate:
    candidate_id: UUID
    first_name: str
    last_name: str
    phone_number: PhoneNumber
    email: str
    birth_date: date
    location: Location
    passport_code: str
    driver_license_code: str
    vacancy: Vacancy
    employment_status: str

    @property
    def phone_number_id(self):
        return self.phone_number.phone_number_id

    @property
    def location_id(self):
        return self.location.location_id

    @property
    def vacancy_id(self):
        return self.vacancy.vacancy_id
