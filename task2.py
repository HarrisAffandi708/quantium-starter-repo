import pandas as pd

sheet1= pd.read_csv("data/daily_sales_data_0.csv")
sheet2= pd.read_csv("data/daily_sales_data_1.csv")
sheet3= pd.read_csv("data/daily_sales_data_2.csv")

#combine all three sheets into one
combined_sheet= pd.concat([sheet1, sheet2, sheet3], ignore_index=True)

combined_sheet= combined_sheet[combined_sheet["product"] == "pink morsel"].copy()
combined_sheet["price"] = combined_sheet["price"].replace("[$,]", "", regex=True).astype(float)
combined_sheet["Sales"] = combined_sheet["quantity"] * combined_sheet["price"]

final_sheet = combined_sheet[["Sales", "date", "region"]].copy()
final_sheet.columns = ["Sales", "Date", "Region"]

final_sheet.to_csv("pink_morsel_sales.csv", index=False)
