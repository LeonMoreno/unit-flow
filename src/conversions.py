# celsius_to_fahrenheit(n)
# bits_to_bytes(n)
def start_conversion(to_convert):
    # TOdo -- Saber si es Temp, Long, Bytes, AnyWay
    print(f"IN convertion {to_convert}")
    return celsius_to_fahrenheit(to_convert)

def celsius_to_fahrenheit(to_convert):
# Formula °F = (°C × 9/5) + 32
    celsius = to_convert[0]
    return (int(celsius) * 9/5) + 32    
