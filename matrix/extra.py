def all_3_digit_numbers(base, digits):
    return {(x * base**2 + y * base + z) for x in digits for y in digits for z in digits}

