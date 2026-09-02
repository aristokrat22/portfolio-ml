import re
import pandas as pd
def parse_address(address):
    parts = [p.strip() for p in address.split(",")]
    
    street = parts[0]
    house_number = None
    
    # ищем часть, которая похожа на номер дома (цифры, возможно с буквой/дробью типа "18/2", "5А")
    for p in parts[1:]:
        if re.match(r'^\d+[а-яА-Я]?(/\d+)?$', p):
            house_number = p
            break
    
    return pd.Series({"street": street, "house_number": house_number})


features = [
    'area_total', 
    'area_living', 
    'area_kitchen', 
    "rooms", 
    "year_built", 
    "has_balcony", 
    "is_first_floor", 
    "is_last_floor", 
    "bathroom_type", 
    "balcony_type", 
    "condition"]

cat_features = ["bathroom_type", "balcony_type", "condition"]