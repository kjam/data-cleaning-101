@ed.has_dtypes(final_types)
@ed.none_missing()
def calculate_store_sales(sales):
    sales['store_total'] = sales.groupby('store_id').transform(sum)['sale_amount']
    sales['associate_total'] = sales.groupby('associate').transform(sum)['sale_amount']
    sales['city_total'] = sales.groupby('city').transform(sum)['sale_amount']
    sales['store_total'] = pd.to_numeric(sales['store_total'])
    sales['city_total'] = pd.to_numeric(sales['city_total'])
    sales['associate_total'] = pd.to_numeric(sales['associate_total'])
    return sales
