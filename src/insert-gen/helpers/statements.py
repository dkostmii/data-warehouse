def separate_statements(statements: list[str], separator: str) -> str:
    return list(map(lambda stmt: str(stmt) + separator, statements))