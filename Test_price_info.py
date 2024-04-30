import price_info as p

def test_total_cost_shopping():
    assert(p.total_cost_shopping() == 46.75)

def test_cost_of_fruits():
    input_q = 6
    fruit = "apple"
    assert(p.cost_of_fruits(fruit, input_q) == 7.2)
