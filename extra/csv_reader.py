import pandas as pd
import csv

#File paths for input/output
input_csv_byzip = 'in_rent_data_byzip.csv'
output_csv_byzip = "rent_data.csv"

#read the input csv file
df = pd.read_csv(input_csv_byzip)

#selected columns to export
selected_columns_byzip = df[["Geographic ID for geographic unit","# Renter-occupied housing units, 2019","% Gross rent $1,000 or more, 2019","% Gross rent $2,000 or more, 2019","% Gross rent $3,000 or more, 2019"]]

#write selected to output csv file
selected_columns_byzip.to_csv(output_csv_byzip, index=False)

print(f"Exported selected columns to {output_csv_byzip}")


# #File paths for input/output
in_general_bycity = 'in_general_bycity.csv'
out_general_bycity = 'out_general_bycity.csv'

#read the input csv file
df = pd.read_csv(in_general_bycity)

#selected columns to export
selected_columns_byzip = df[['Name of geographic unit','# Total housing units, 2019','% Vacant housing units, 2019','Owner vacancy rate, 2019','Renter vacancy rate, 2019','% 1 unit, detached housing units, 2019','% Units built 2014 or later, 2019','% Occupied units lacking complete plumbing facilities, 2019','% Occupied units with no telephone service available, 2019']]

#write selected to output csv file
selected_columns_byzip.to_csv(out_general_bycity, index=False)

print(f"Exported selected columns to {output_csv_byzip}")
