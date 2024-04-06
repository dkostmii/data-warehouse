import models.dv_star as models
from helpers.unique_generator import Generator, UniqueGenerator


class Context:
    def __init__(self):
        self.shared_unique_generators: dict[str, UniqueGenerator] = {}
        self.shared_generators: dict[str, Generator] = {}
        self.hub_candidate_applications: list[models.HubCandidateApplication] = []
        self.sat_candidate_application_infos: list[
            models.SatCandidateApplicationInfo
        ] = []
        self.sat_vacancies: list[models.SatVacancy] = []
        self.sat_vacancy_categories: list[models.SatVacancyCategory] = []
        self.sat_companies: list[models.SatCompany] = []
        self.sat_production_branches: list[models.SatProductionBranch] = []
