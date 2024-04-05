from dataclasses import dataclass
from datetime import date, datetime
from uuid import UUID


@dataclass
class Location:
    location_id: UUID
    name: str


@dataclass
class ProductionBranch:
    production_branch_id: UUID
    name: str


@dataclass
class Company:
    company_id: UUID
    name: str
    phone_number: str
    production_branch: ProductionBranch
    company_location: Location


@dataclass
class VacancyCategory:
    vacancy_category_id: UUID
    name: str


@dataclass
class Vacancy:
    vacancy_id: UUID
    name: str
    salary: int
    vacancy_category: VacancyCategory
    company: Company
    additional_info: str = ""


@dataclass
class EmploymentStatus:
    employment_status_id: UUID
    name: str


@dataclass
class CandidateApplication:
    candidate_application_id: UUID
    first_name: str
    last_name: str
    phone_number: str
    email: str
    birth_date: date
    passport_code: str
    driver_license_code: str
    candidate_location: Location
    vacancy: Vacancy
    vacancy_category: VacancyCategory
    company: Company
    company_location: Location
    production_branch: ProductionBranch
    employment_status: EmploymentStatus
    created_at: datetime

    @property
    def candidate_location_id(self):
        return self.candidate_location.location_id

    @property
    def vacancy_id(self):
        return self.vacancy.vacancy_id

    @property
    def vacancy_category_id(self):
        return self.vacancy_category.vacancy_category_id

    @property
    def company_id(self):
        return self.company.company_id

    @property
    def company_location_id(self):
        return self.company_location.location_id

    @property
    def production_branch_id(self):
        return self.production_branch.production_branch_id

    @property
    def employment_status_id(self):
        return self.employment_status.employment_status_id