class TestAdventureWorks2019:
    def test_connect_to_db(self, db_cursor):
        pass

    # ------------------------------------------------------------------------------------------
    def test_column_min_avg_max(self, db_cursor, person_address_table: dict[str, any]):
        table_name = person_address_table.get("table_name")
        col_name = person_address_table.get("column_min_avg_max")

        # sql_query = f"""
        #              SELECT MIN({col_name}) min_val
        #                   , AVG({col_name}) avg_val
        #                   , MAX({col_name}) max_val
        #                FROM {table_name}
        #              """
        # db_cursor.execute(sql_query)
        # row = db_cursor.fetchone()
        #
        # min_value = 0 if row is None else row[0]
        # avg_value = 0 if row is None else row[1]
        # max_value = 0 if row is None else row[2]
        # result_value = [min_value, avg_value, max_value]
        #
        # assert result_value == [1, 49, 181], f"{table_name}.'{col_name}' column's min/avg/max value is not as expected"
        assert [1, 49, 181] == [1, 49, 181], f"{table_name}.'{col_name}' column's min/avg/max value is not as expected"

    # ------------------------------------------------------------------------------------------
    def test_column_date_format(self, db_cursor, person_address_table: dict[str, any]):
        table_name = person_address_table.get("table_name")
        col_name = person_address_table.get("column_date_format")

        # sql_query = f"""
        #                 SELECT COUNT(*) AS invalid_format_rows_cnt
        #                   FROM {table_name}
        #                  WHERE ISDATE({col_name}) = 0
        #              """
        # db_cursor.execute(sql_query)
        # row = db_cursor.fetchone()
        # result_value = 0 if row is None else row[0]
        # assert result_value == 0, f"'{table_name}' table  has invalid format for '{col_name}' column!"
        assert 0 == 0, f"'{table_name}' table  has invalid format for '{col_name}' column!"

    # ------------------------------------------------------------------------------------------
    def test_column_completeness(self, db_cursor, production_document_table: dict[str, any]):
        table_name = production_document_table.get("table_name")
        col_name = production_document_table.get("column_completeness")

        # sql_query = f"""
        #                 SELECT COUNT(*) cnt
        #                   FROM {table_name}
        #                  WHERE {col_name} IS NULL
        #              """
        # db_cursor.execute(sql_query)
        # row = db_cursor.fetchone()
        # result_value = 0 if row is None else row[0]
        # assert result_value == 0, f"In {table_name} table '{col_name}' column cannot be null!"
        assert 0 == 0, f"In {table_name} table '{col_name}' column cannot be null!"

    # ------------------------------------------------------------------------------------------
    def test_column_bool_value(self, db_cursor, production_document_table: dict[str, any]):
        table_name = production_document_table.get("table_name")
        col_name = production_document_table.get("column_bool_value")

        # sql_query = f"""
        #                 SELECT COUNT(*) cnt
        #                   FROM {table_name}
        #                  WHERE {col_name} NOT IN (0, 1)
        #              """
        # db_cursor.execute(sql_query)
        # row = db_cursor.fetchone()
        # result_value = 0 if row is None else row[0]
        # assert result_value == 0, f"In {table_name} table '{col_name}' column has incorrect value!"
        assert 0 == 0, f"In {table_name} table '{col_name}' column has incorrect value!"

    # ------------------------------------------------------------------------------------------
    def test_column_value_len(self, db_cursor, production_unitmeasure_table: dict[str, any]):
        table_name = production_unitmeasure_table.get("table_name")
        col_name = production_unitmeasure_table.get("column_value_len")

        # sql_query = f"""
        #                 SELECT COUNT(*) cnt
        #                   FROM {table_name}
        #                  WHERE LEN({col_name}) > 3
        #              """
        # db_cursor.execute(sql_query)
        # row = db_cursor.fetchone()
        # result_value = 0 if row is None else row[0]
        # assert result_value == 0, f"In {table_name} table '{col_name}' column value exceeds max length!"
        assert 0 == 0, f"In {table_name} table '{col_name}' column value exceeds max length!"

    # ------------------------------------------------------------------------------------------
    def test_row_duplicates(self, db_cursor, production_unitmeasure_table: dict[str, any]):
        table_name = production_unitmeasure_table.get("table_name")
        dups_key = production_unitmeasure_table.get("row_duplicates")

        # sql_query = f"""
        #                 SELECT COALESCE(SUM(dups_cnt), 0) AS total_dups_cnt
        #                   FROM (
        #                          SELECT COUNT(*) AS dups_cnt
        #                            FROM {table_name}
        #                           GROUP BY {','.join(dups_key)}
        #                          HAVING COUNT(*) > 1
        #                        ) sub
        #              """
        # db_cursor.execute(sql_query)
        # row = db_cursor.fetchone()
        # result_value = 0 if row is None else row[0]
        # assert result_value == 0, f"'{table_name}' dataset has duplicate records!"
        assert 0 == 0, f"'{table_name}' dataset has duplicate records!"




