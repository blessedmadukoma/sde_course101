import polars as pl
from cuallee import Check, CheckLevel

# Read CSV file into Polars DataFrame
df = pl.read_csv("./data/sample_data.csv")

# Question: Check for Nulls on column Id and that Customer_ID column is unique

check = Check()
check.is_complete("Customer_ID")

# Validate
print(check.validate(df))
