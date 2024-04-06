from pypika import Column
from pypika.functions import Now as NOW

load_date = Column("load_date", "TIMESTAMP", default=NOW())
record_source = Column("record_source", "VARCHAR(50)", default="A record source")
