from random import choice, randint, random

from translitua import translitua

alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"


def get_random_letters(length: int = 1, alphabet: str = alphabet) -> str:
    if length < 1:
        raise Exception("Expected length to be at least 1.")

    result = ""

    while len(result) < length:
        result += choice(alphabet)

    return result


class EmailGenerator:
    _email_providers: list[str]

    def __init__(self):
        with open("datasets/email_providers.txt") as f:
            self._email_providers = f.readlines()

    def get(self, first_name: str, last_name: str) -> str:
        first_name = translitua(first_name.lower())
        last_name = translitua(last_name.lower())
        separator = choice([".", "_", "__"])
        appendix = ""
        email_provider = choice(self._email_providers).strip()

        if random() < 0.5:
            appendix = str(randint(0, 99)).zfill(2)

        return f"{first_name[:1]}{separator}{last_name}{appendix}@{email_provider}"


class PhoneNumberGenerator:
    _phone_prefixes: list[str]

    def __init__(self):
        with open("datasets/phone_prefixes.csv") as f:
            lines = f.readlines()
            table_rows = lines[1:]
            self._phone_prefixes = ["".join(row.strip().split(",")) for row in table_rows]

    def get(self) -> str:
        phone_prefix = choice(self._phone_prefixes)
        phone_number_rest = str(randint(0, 999_99_99)).zfill(7)

        return f"{phone_prefix}{phone_number_rest}"


class LocationGenerator:
    _locations: list[str]

    def __init__(self):
        with open("datasets/locations.txt") as f:
            self._locations = f.readlines()

    def get(self) -> str:
        return choice(self._locations).strip()


class EmploymentStatusGenerator:
    _employment_statuses: list[str]

    def __init__(self):
        with open("datasets/employment_status.txt") as f:
            self._employment_statuses = f.readlines()

    def get(self) -> str:
        return choice(self._employment_statuses).strip()


def get_passport_code(old_format: bool = False) -> str:
    if old_format:
        code = get_random_letters(length=2).upper()
        id = str(randint(0, 999_999)).zfill(6)

        return f"{code}{id}"

    return str(randint(0, 999_999_999)).zfill(9)


def get_driver_license_code() -> str:
    code = get_random_letters(length=3).upper()
    id = str(randint(0, 999_999)).zfill(6)

    return f"{code}{id}"
