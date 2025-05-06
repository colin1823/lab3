from bmi import calculate_bmi, classify_bmi
def test_normal_bmi():
    height =1.8 
    weight = 70
    expected_bmi = 21.604938271604937
    expected_classification = 0  # Normal weight
    bmi_value = calculate_bmi(height, weight)
    classification = classify_bmi(bmi_value)
    assert (expected_bmi == bmi_value) 
    assert (expected_classification == classification)

def test_underweight_bmi():
    height = 1.8
    weight = 50
    expected_bmi = 15.432098765432098
    expected_classification = -1  # Underweight
    bmi_value = calculate_bmi(height, weight)
    classification = classify_bmi(bmi_value)
    assert (expected_bmi == bmi_value) 
    assert (expected_classification == classification)

def test_overweight_bmi():  
    height = 1.8
    weight = 90
    expected_bmi = 27.777777777777775
    expected_classification = 1  # Overweight
    bmi_value = calculate_bmi(height, weight)
    classification = classify_bmi(bmi_value)
    assert (expected_bmi == bmi_value) 
    assert (expected_classification == classification)