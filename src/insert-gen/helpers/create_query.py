from typing import Any, List, Union

from pypika import Column, Table
from pypika.enums import ReferenceOption
from pypika.queries import CreateQueryBuilder
from pypika.utils import builder


class ForeignKey:
    """Represents a foreign key constraint."""

    def __init__(
        self,
        columns: List[Column],
        reference_table: Union[str, Table],
        reference_columns: List[Column],
        on_delete: ReferenceOption = None,
        on_update: ReferenceOption = None,
    ) -> None:
        self.columns = columns
        self.reference_table = reference_table
        self.reference_columns = reference_columns
        self.on_delete = on_delete
        self.on_update = on_update

    def get_sql(self, **kwargs: Any) -> str:
        foreign_key_sql = "FOREIGN KEY ({columns}) REFERENCES {table_name} ({reference_columns})".format(
            columns=",".join(column.get_name_sql(**kwargs) for column in self.columns),
            table_name=(
                self.reference_table.get_sql(**kwargs)
                if isinstance(self.reference_table, Table)
                else self.reference_table
            ),
            reference_columns=",".join(
                column.get_name_sql(**kwargs) for column in self.reference_columns
            ),
        )
        if self.on_delete:
            foreign_key_sql += " ON DELETE " + self.on_delete.value
        if self.on_update:
            foreign_key_sql += " ON UPDATE " + self.on_update.value
        return foreign_key_sql


class MultipleFKCreateQueryBuilder(CreateQueryBuilder):
    def __init__(self, original_query_builder: CreateQueryBuilder) -> None:
        self._create_table = original_query_builder._create_table
        self._temporary = original_query_builder._temporary
        self._unlogged = original_query_builder._unlogged
        self._as_select = original_query_builder._as_select
        self._columns = original_query_builder._columns
        self._period_fors = original_query_builder._period_fors
        self._with_system_versioning = original_query_builder._with_system_versioning
        self._primary_key = original_query_builder._primary_key
        self._uniques = original_query_builder._uniques
        self._if_not_exists = original_query_builder._if_not_exists
        self.dialect = original_query_builder.dialect
        self._foreign_keys = []

    def _foreign_key_clauses(self, **kwargs) -> str:
        return [foreign_key.get_sql(**kwargs) for foreign_key in self._foreign_keys]

    def _body_sql(self, **kwargs) -> str:
        clauses = self._column_clauses(**kwargs)
        clauses += self._period_for_clauses(**kwargs)
        clauses += self._unique_key_clauses(**kwargs)
        clauses += self._foreign_key_clauses(**kwargs)

        if self._primary_key:
            clauses.append(self._primary_key_clause(**kwargs))

        return ",".join(clauses)

    @builder
    def foreign_key(
        self,
        columns: List[Union[str, Column]],
        reference_table: Union[str, Table],
        reference_columns: List[Union[str, Column]],
        on_delete: ReferenceOption = None,
        on_update: ReferenceOption = None,
    ) -> "CreateQueryBuilder":
        """
        Adds a foreign key constraint.

        :param columns:
            Type:  List[Union[str, Column]]

            A list of foreign key columns.

        :param reference_table:
            Type: Union[str, Table]

            The parent table name.

        :param reference_columns:
            Type: List[Union[str, Column]]

            Parent key columns.

        :param on_delete:
            Type: ReferenceOption

            Delete action.

        :param on_update:
            Type: ReferenceOption

            Update option.

        :return:
            CreateQueryBuilder.
        """

        self._foreign_keys.append(
            ForeignKey(
                columns=self._prepare_columns_input(columns),
                reference_table=reference_table,
                reference_columns=self._prepare_columns_input(reference_columns),
                on_delete=on_delete,
                on_update=on_update,
            )
        )
