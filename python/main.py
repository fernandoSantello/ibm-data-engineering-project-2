from sqlalchemy import create_engine

from etl_modules.extract_data import extract
from etl_modules.transform_data import transform
from etl_modules.load_data import load_to_csv, load_to_db
from etl_modules.log_data import log_process
from etl_modules.query_data import run_query

save_csv_path = './files/Largest_banks_data.csv'
data_url = 'https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks'
rates_file_path = './files/exchange_rate.csv'
engine = create_engine('sqlite:///./files/Banks.db')
table_name = 'Largest_banks'

log_process('START PROCESS')
log_process('START EXTRACTION')
df = extract(url=data_url)
log_process('FINISHED EXTRACTION')
log_process('START TRANSFORMATION')
df = transform(df=df, rates_file_path=rates_file_path)
log_process('FINISHED TRANSFORMATION')
log_process('STARTED EXPORTING TO CSV')
load_to_csv(df=df, save_csv_path=save_csv_path)
log_process('FINISHED EXPORTING TO CSV')
log_process('STARTED EXPORTING TO BD')
load_to_db(table_name=table_name, df=df, con=engine)
log_process('FINISHED EXPORTING TO DB')
log_process('STARTED QUERY 1')
query_1 = run_query(engine=engine, statment='SELECT * FROM Largest_banks')
log_process('FINISHED QUERY 1')
log_process('STARTED QUERY 2')
query_2 = run_query(engine=engine, statment='SELECT AVG(MC_GBP_Billion) FROM Largest_banks')
log_process('FINISHED QUERY 2')
log_process('STARTED QUERY 3')
query_3 = run_query(engine=engine, statment='SELECT `Bank name` from Largest_banks LIMIT 5')
log_process('FINISHED QUERY 3')
