'''
    Program purpose: Sales data flower shop
    Programmer: NURSYAZANA BINTI MOHAMAD NOH EZAM
    Date: 8 Mac 2024
'''

def calculate_total_units_sold(units_sold):
#Calculate the total number of units sold for all cosmetic products.
    return sum(units_sold)
def find_highest_sales_product(product_names, units_sold):
#Determine the cosmetic product with the highest sales.
    highest_sales_index = units_sold.index(max(units_sold))
    return product_names[highest_sales_index]
def find_above_average_products(product_names, customer_reviews):
#Identify cosmetic products with average customer reviews above 3.
    above_average_products = [product_names[i] for i in range(len(customer_reviews)) if customer_reviews[i] > 3]
    return above_average_products
def find_average_customer_reviews(customer_reviews):
#Calculate the average customer review score for all flowers based on the provided flower sales data.
    average_score = sum(customer_reviews) / len(customer_reviews)
    return average_score

# Sample lists of flower product names, units sold, and customer reviews
product_names = ["Tulip", "Sunflower", "Lily", "Roses", "Hibiscus", "Daisy", "Dahlia", "Lavender", "Violet",
                 "Jasmine", "Orchid", "Blossom", "Azalea", "Iris", "Snowdrop", "Dandelion", "Poppy", "Marigold",
                 "Levy", "Iris"]
units_sold = [200, 100, 300, 155, 200, 500, 450, 250, 250, 150, 100, 350, 300, 110, 450, 300, 300,
              100, 150, 200]
customer_reviews = [5, 5, 3.5, 4, 4, 2.5, 3, 3, 3, 4, 4.5, 2.5, 2, 2, 3, 2, 1.5, 4.5, 5, 2]

# Calculate total units sold
total_units_sold = calculate_total_units_sold(units_sold)
# Find product with highest sales
highest_sales_product = find_highest_sales_product(product_names, units_sold)
# Find products with above-average customer reviews
above_average_products = find_above_average_products(product_names, customer_reviews)
#Find the products with average score
average_score = find_average_customer_reviews(customer_reviews)

# Display the output
print("The Total number of units sold for all flowers:", total_units_sold)
print("The highest sales of flower:", highest_sales_product)
print("Flower customer review above 3:", above_average_products)
print("Average Customer Review Score:", average_score)




