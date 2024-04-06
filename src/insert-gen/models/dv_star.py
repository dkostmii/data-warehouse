from dataclasses import dataclass
from datetime import date, datetime
from uuid import UUID


@dataclass
class HubCandidateApplication:
    candidate_application_id: UUID


@dataclass
class SatCandidateApplicationInfo(HubCandidateApplication):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    birth_date: date
    passport_code: str
    driver_license_code: str
    candidate_location: str
    employment_status: str
    created_at: datetime


@dataclass
class SatVacancy(HubCandidateApplication):
    name: str
    salary: int
    additional_info: str = ""


@dataclass
class SatVacancyCategory(HubCandidateApplication):
    name: str


@dataclass
class SatCompany(HubCandidateApplication):
    name: str
    phone_number: str
    company_location: str


@dataclass
class SatProductionBranch(HubCandidateApplication):
    name: str
