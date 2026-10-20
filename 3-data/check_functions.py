def clean_currency(value:str) -> float:
    '''
    This function will take a string value and remove the dollar sign and commas
    and return a float value.
    '''
    return float(value.replace(',', '').replace('$', ''))

def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return 'normal'


if __name__ == '__main__':
    assert clean_currency('$1,234.56') == 1234.56

    print("All tests passed!!")
           
