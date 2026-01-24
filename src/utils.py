import re

units = {
    "temperature": ["c", "f", "k", "celsius", "fahrenheit"],
    "length": ["m", "km", "cm", "pulgadas", "inches"],
}

def get_tokens(text):
    pattern = r"([\d.0]+)\s+([a-zA-Z]+)\s+(to|a)\s+([a-zA-Z]+)"

    match = re.search(pattern, text)
    return match

def valid_src_dst(groups):
    print(f"match = {groups}")
    src = groups(1)
    dst = groups[3]
    valid = True

    print(f"src = {src} dst = {dst}")
    # for unit in units:
    #     if src and dst in units[unit]: 
    #         print(f"NOt Valid")

# analizador de lenguaje natural (un parser) sencillo.
# [VALOR] [UNIDAD_ORIGEN] [CONECTOR] [UNIDAD_DESTINO]
# asi voy:
# /[\d.0]+\s[a-zA-Z]+\sto\s[a-zA-Z]+
# [\d.0]+\s+[a-zA-Z]+\s+to\s+[a-zA-Z]+
def start_parser(text):
    print(f"in start_parser text = {text}")
    match = get_tokens(text)
    print(f"in start_parser match = {type(match.groups())}")

    valid_unit = valid_src_dst(match.groups())    

    # if not match or not valid_unit:
    #     return False

    
    # if match:
    #     src_to_dst = {
    #         "value": match.group(1),
    #         "source": match.group(2),
    #         "destination": match.group(4), 
    #     } 
        
    # return src_to_dst