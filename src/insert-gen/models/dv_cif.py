from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass
class HubCandidate:
    candidate_id: UUID


@dataclass
class SatCandidateInfo(HubCandidate):
    employment_status: str


@dataclass
class SatCandidateContacts(HubCandidate):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    birth_date: date
    passport_code: str
    driver_license_code: str
    location: str


@dataclass
class HubCompany:
    company_id: UUID


@dataclass
class SatCompanyInfo(HubCompany):
    name: str
    phone_number: str
    location: str


@dataclass
class SatProductionBranch(HubCompany):
    name: str


@dataclass
class LinkVacancyBase:
    vacancy_id: UUID


@dataclass
class LinkVacancy(LinkVacancyBase):
    company_id: UUID
    candidate_id: UUID


@dataclass
class SatVacancyInfo(LinkVacancyBase):
    name: str
    salary: int
    additional_info: str = ""


@dataclass
class SatVacancyCategory(LinkVacancyBase):
    name: str
