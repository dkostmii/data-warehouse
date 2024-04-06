import models.dv_cif as models
from helpers.unique_generator import Generator, UniqueGenerator


class Context:
    def __init__(self):
        self.shared_unique_generators: dict[str, UniqueGenerator] = {}
        self.shared_generators: dict[str, Generator] = {}
        self.link_vacancies: list[models.LinkVacancy] = []
        self.hub_candidates: list[models.HubCandidate] = []
        self.hub_companies: list[models.HubCompany] = []
        self.sat_candidate_infos: list[models.SatCandidateInfo] = []
        self.sat_candidate_contacts: list[models.SatCandidateContacts] = []
        self.sat_vacancy_infos: list[models.SatVacancyInfo] = []
        self.sat_vacancy_categories: list[models.SatVacancyCategory] = []
        self.sat_company_infos: list[models.SatCompanyInfo] = []
        self.sat_production_branches: list[models.SatProductionBranch] = []
