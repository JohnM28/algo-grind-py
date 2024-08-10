def product_except_self(arr: list) -> list:
    # Replace this placeholder return statement with your code
    left_product = 0
    right_product = len(arr) - 1
    result = [1] * len(arr)

    while left_product <= right_product:
        result[left_product] = result[left_product] * arr[right_product]
        result[right_product] = result[right_product] * arr[left_product]
        left_product += 1
        right_product -= 1
    return result

arr = [-1, 2, 3, 5, 0]

print(product_except_self(arr))