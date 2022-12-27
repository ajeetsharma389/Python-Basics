import openpyxl
loadxl = openpyxl.load_workbook("inventory.xlsx")
product_list = loadxl['Sheet1']
####### Ex:1 List each company with respective product count
## create a empty dictionary to store supplier name

def get_product_count_each_compant():
    supplier_name_list = {}
    print(product_list.max_row)

    for product_row in range(2,product_list.max_row):
        supplier_name = product_list.cell(product_row,4).value
        if supplier_name in supplier_name_list:
            supplier_name_list[supplier_name] = supplier_name_list.get(supplier_name) + 1
        else:
            print("adding new supplier")
            supplier_name_list[supplier_name] = 1        

    print(supplier_name_list)   

get_product_count_each_compant()
###### List products with inventory less than 10

