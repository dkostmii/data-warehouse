import models.snowflake as models
from helpers.unique_generator import Generator, UniqueGenerator


class Context:
    def __init__(self):
        self.shared_unique_generators: dict[str, UniqueGenerator] = {}
        self.shared_generators: dict[str, Generator] = {}
        self.candidate_applications: list[models.CandidateApplication] = []
        self.locations: list[models.Location] = []
        self.vacancies: list[models.Vacancy] = []
        self.vacancy_categories: list[models.VacancyCategory] = []
        self.companies: list[models.Company] = []
        self.production_branches: list[models.ProductionBranch] = []
        self.employment_statuses: list[models.EmploymentStatus] = []
