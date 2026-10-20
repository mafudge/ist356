def clean_currency(value: str) -> float:
    '''
    This function takes a value as str and remove the $ and , and 
    converts to a float value. It returns the float value.
    '''
    value = value.replace(',', '')
    value = value.replace('$', '')
    float_value = float(value)
    return float_value


def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    '''
    This function takes in the items per person and 
    price per person for a check, along with the 75th percentile values for each.
    It returns a string indicating the type of customer.
    '''
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return 'normie'

if __name__ == '__main__':
    # test clean_currency function
    assert clean_currency('$1,234.56') == 1234.56
    print("\nAll tests passed!")


