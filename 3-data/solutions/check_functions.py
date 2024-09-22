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
    
    return ''


def detect_tipper(tip_pct:float, tip_pct_75th_pctile:float, tip_pct_25th_pctile:float) -> str:
    if tip_pct > tip_pct_75th_pctile:
        return 'heavy tipper'
    if tip_pct < tip_pct_25th_pctile:
        return 'light tipper'
    
    return ''



if __name__=='__main__':
    # tests
    assert clean_currency('$1,000.00') == 1000.00
    assert clean_currency('$1,000') == 1000.00
    assert clean_currency('1,000') == 1000.00
    assert clean_currency('$1000') == 1000.00

    assert detect_whale(10, 100, 5, 50) == 'whale'
    assert detect_whale(10, 100, 5, 100) == 'big eater'
    assert detect_whale(5, 100, 5, 50) == 'big spender'

    assert detect_tipper(0.24, 0.75, 0.25) == 'light tipper'
    assert detect_tipper(0.76, 0.75, 0.25) == 'heavy tipper'
    assert detect_tipper(0.50, 0.75, 0.25) == ''