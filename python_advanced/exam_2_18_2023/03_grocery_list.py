def shop_from_grocery_list(budget, grocery_list, *products_info):
    products = []
    
    for product in products_info:
        name, price = product
        
        if name in grocery_list and price <= budget:
            budget -= price
            products.append(name)
            grocery_list.remove(name)

        if not grocery_list:
            break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    
    return f"You did not buy all the products. Missing products: {', '.join(map(str, grocery_list))}."
