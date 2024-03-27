import pandas as pd

df = pd.read_csv("../01.dataset/ProductPriceIndex.csv")
df

df.farmprice = df.farmprice.str.replace("$","")
df.farmprice

unique_product_name = df["productname"].unique().tolist()
unique_product_name

def dichotomous_variable_multiple(product_name, fruit_name):
    if product_name == fruit_name:
        return 1
    else:
        return 0 

for product_name in unique_product_name:
    df[product_name] = df["productname"].apply(dichotomous_variable_multiple, args=(product_name,))

for product_name in unique_product_name:
    print(product_name)

df["farmprice"] = df["farmprice"].replace("","0")

df["farmprice_Numeric"] = df["farmprice"].str.replace("$","")
df

df["farmprice_Numeric"] = df["farmprice_Numeric"].replace("","0")


df["farmprice_Numeric"] = df["farmprice_Numeric"].astype(float)
df["farmprice_Numeric"]

farmprice_mean_by_date = df.groupby('date').agg({"farmprice_Numeric":"mean"}).reset_index()
farmprice_mean_by_date

farmprice_mean_by_productname = df.groupby('productname').agg({"farmprice_Numeric":"mean"}).reset_index()
farmprice_mean_by_productname

farmprice_mean_by_date_and_productname = df.groupby(["productname","date"]).agg({"farmprice_Numeric":"mean"}).reset_index()
farmprice_mean_by_date_and_productname

writer = pd.ExcelWriter(f"../03.output_folder/mean_distribution.xlsx", engine='xlsxwriter')
writer

farmprice_mean_by_productname.to_excel(writer, sheet_name='farmprice_mean_by_productname',startrow = 1,index=False)

sheet1 = writer.sheets['farmprice_mean_by_productname']
sheet1.set_column('A:Z',20)
sheet1.write("A1:C1","This is the mean of the farmprice by productname.")

farmprice_mean_by_date.to_excel(writer, sheet_name='farmprice_mean_by_date',startrow = 1,index=False)

writer.close()