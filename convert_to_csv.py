import pandas as pd

data_xls = pd.read_excel('CPdescarga.xls', 'Distrito_Federal', index_col=None, converters={'d_codigo':str,'d_CP':str})

print(data_xls)

data_xls.to_csv('zip_codes.csv', encoding='utf-8', index=False, header=False)

