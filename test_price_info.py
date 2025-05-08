from price_info import total_cost_shopping, cost_of_fruits
test_price_list = {'apple': 1, 'orange': 2, 'watermelon': 1, 'pineapple': 2}
test_quantity_list = {'apple': 3, 'orange': 5, 'watermelon': 1, 'pineapple': 2}
    # Test the total cost of shopping
def test_total_cost_shopping():
    total_cost = 0
    expected_cost = 18
    for key in test_price_list.keys():
       
        if key in test_quantity_list:
            total_cost += test_price_list[key] * test_quantity_list[key]
    assert total_cost == expected_cost
def test_cost_of_fruits():
    expected_cost = 6
    cost = cost_of_fruits("apple" , 5)


    assert cost == expected_cost
            