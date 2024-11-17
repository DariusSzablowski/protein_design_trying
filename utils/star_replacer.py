import random

def replace_random_positions(input_string, num_replacements=10):
    # Convert string to list because strings are immutable in Python
    str_list = list(input_string)
    length = len(input_string)

    # Check if there are enough positions to replace
    if num_replacements > length:
        raise ValueError("Number of replacements exceeds the length of the string.")

    # Choose 10 unique positions randomly
    positions = random.sample(range(length), num_replacements)

    # Replace characters at these positions with '*'
    for pos in positions:
        str_list[pos] = '*'

    # Join the list back into a string
    return ''.join(str_list)

# usage
top_1_string = "MTTPEQLKIHKEVVRAMDYLILMKHYYPEMTDEELKTPEMIEEMAKTAGNVDKKVFEILFEIYGTTENIIEAYYNGEMTPVVDKMVKLK"
top_2_string_efficiently_evolved = "MPEWERRSEEFVKMVEEKYGKEFGELVREILKEVAEREFPDGKMSHREFRNILYRMPFHLHHAAFKNPKYESLITKFDPDELKEMAEKIP"

result_1 = replace_random_positions(top_1_string)
result_2 = replace_random_positions(top_2_string_efficiently_evolved)

print("\n")
print("top_1_string with stars: ", result_1)
print("\n")
print("top_2_string_efficiently_evolved with stars: ", result_2)
