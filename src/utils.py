import re

units = {
    "temperature": ["c", "f", "celsius", "fahrenheit"],
    "length": ["m", "km", "cm", "pulgadas", "inches"],
}

def get_tokens(text):
    pattern = r"([\d.0]+)\s+([a-zA-Z]+)\s+(to|a)\s+([a-zA-Z]+)"

    match = re.search(pattern, text)
    return match

def valid_token(token):
    print(f"token = {token}")
    for unit in units:
        if token.lower() in units[unit]: 
            return unit
    
    return False

# analizador de lenguaje natural (un parser) sencillo.
# [VALOR] [UNIDAD_ORIGEN] [CONECTOR] [UNIDAD_DESTINO]
# asi voy:
# /[\d.0]+\s[a-zA-Z]+\sto\s[a-zA-Z]+
# [\d.0]+\s+[a-zA-Z]+\s+to\s+[a-zA-Z]+
def start_parser(text):
    match = get_tokens(text)
    if not match:
        return False

    valid_src = valid_token(match.group(2))
    valid_dst = valid_token(match.group(4))
    
    if valid_src != valid_dst:
        return False


    # if not match or not valid_unit:
    #     return False

    
    # if match:
    #     src_to_dst = {
    #         "value": match.group(1),
    #         "source": match.group(2),
    #         "destination": match.group(4), 
    #     } 
        
    return True