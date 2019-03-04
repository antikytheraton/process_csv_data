from multiprocessing import Pool
import pandas as pd


xls = pd.ExcelFile('CPdescarga.xls')
sheet_names = xls.sheet_names[1:]


def convert_to_csv(sheet_name):
    return pd.read_excel(xls, sheet_name, index_col=None, converters={'d_codigo':str,'d_CP':str})

if __name__=='__main__':
    p = Pool()
    files = p.map(convert_to_csv, sheet_names)
    convined_csv = pd.concat(files)
    convined_csv.to_csv(f'csv_files/all.csv', encoding='utf-8', index=False, header=False)
    p.close()