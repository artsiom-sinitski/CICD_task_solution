import pytest
import pyodbc


@pytest.fixture(scope='module')
def db_session(variables):
    server = variables.get("server")
    db_name = variables.get("db_name")
    db_user = variables.get("db_user")
    db_pwd = variables.get("db_pwd")
    db_session = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                                "SERVER=" + server + ";DATABASE=" + db_name +
                                ";UID=" + db_user + ";PWD=" + db_pwd)
    print(f"\n*** Connected to '{db_name}' database! ***")
    yield db_session
    print(f"\n*** Disconnected from '{db_name}' database! ***")
    db_session.close()


@pytest.fixture
def db_cursor(db_session):
    cursor = db_session.cursor()
    yield cursor


@pytest.fixture
def person_address_table() -> dict[str, any]:
    person_address_table = {
                             "table_name": "[Person].[Address]",
                             "column_min_avg_max": "StateProvinceID",
                             "column_date_format": "ModifiedDate"
                           }
    return person_address_table


@pytest.fixture
def production_document_table() -> dict[str, any]:
    production_document_table = {
                                 "table_name": "[Production].[Document]",
                                 "column_bool_value": "FolderFlag",
                                 "column_completeness": "DocumentNode"
                                 }
    return production_document_table


@pytest.fixture
def production_unitmeasure_table() -> dict[str, any]:
    production_unitmeasure_table = {
                                     "table_name": "[Production].[UnitMeasure]",
                                     "column_value_len": "UnitMeasureCode",
                                     "row_duplicates": ["UnitMeasureCode", "Name"]
                                   }
    return production_unitmeasure_table
