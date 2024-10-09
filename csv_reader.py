import pandas as pd

#File paths for input/output
input_csv = 'in_rent_data_byzip.csv'
output_csv = "rent_data.csv"

#read the input csv file
df = pd.read_csv(input_csv)

#selected columns to export
selected_columns = df[["Geographic ID for geographic unit","# Renter-occupied housing units, 2019","% Gross rent $1,000 or more, 2019","% Gross rent $2,000 or more, 2019","% Gross rent $3,000 or more, 2019"]]

#write selected to output csv file
selected_columns.to_csv(output_csv, index=False)

print(f"Exported selected columns to {output_csv}")