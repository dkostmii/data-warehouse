from uuid import uuid4, UUID

def get_random_uuid() -> UUID:
    return uuid4()