import hashlib

def encode_information_short(district_code, city_name, ward_number, distance, degree):
    # Combine the information into a string
    info_string = f"District Code: {district_code}, City Name: {city_name}, Ward Number: {ward_number}, Distance: {distance} km, Degree: {degree} degrees"
    
    # Hash the information using SHA-256
    hashed_info = hashlib.sha256(info_string.encode()).hexdigest()
    
    # Take the first 10 characters of the hash as the short code
    short_code = hashed_info[:10]
    
    return short_code

# Example usage:
district_code = 123
city_name = "Anytown"
ward_number = 5
distance = 2
degree = 45

short_code = encode_information_short(district_code, city_name, ward_number, distance, degree)
print(short_code)
