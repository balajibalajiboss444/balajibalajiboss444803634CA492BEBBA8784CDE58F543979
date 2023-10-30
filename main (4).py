# Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
def linear_search_product(products, target_product):
    # Write your code here
    # return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["apple", "banana", "orange", "banana", "apple", "banana"]
target_product = "banana"
indices = linear_search_product(products, target_product)
print(indices) # Output: [2, 4]
if indices == []:
    print("Product not found")
else:
    print("Product found at indices:", indices)