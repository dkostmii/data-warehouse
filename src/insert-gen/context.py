import models
from helpers.unique_generator import Generator, UniqueGenerator


class Context:
    def __init__(self):
        self.shared_unique_generators: dict[str, UniqueGenerator] = {}
        self.shared_generators: dict[str, Generator] = {}
        self.production_branches: list[models.ProductionBranch] = []
        self.locations: list[models.Location] = []
        self.phone_numbers: list[models.PhoneNumber] = []
        self.companies: list[models.Company] = []
        self.vacancy_categories: list[models.VacancyCategory] = []
        self.vacancies: list[models.Vacancy] = []
        self.candidates: list[models.Candidate] = []
