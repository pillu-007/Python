a = 5  # Binary: 0b101
b = 3  # Binary: 0b011

# Bitwise AND
result_and = a & b  # Binary: 0b001 (Decimal: 1)

# Bitwise OR
result_or = a | b   # Binary: 0b111 (Decimal: 7)

# Bitwise XOR
result_xor = a ^ b  # Binary: 0b110 (Decimal: 6)

# Bitwise NOT
result_not_a = ~a   # Binary: -0b110 (Decimal: -6)

# Left Shift
result_left_shift = a << 1  # Binary: 0b1010 (Decimal: 10)

# Right Shift
result_right_shift = a >> 1  # Binary: 0b10 (Decimal: 2)

print("Bitwise AND:", result_and)
print("Bitwise OR:", result_or)
print("Bitwise XOR:", result_xor)
print("Bitwise NOT (a):", result_not_a)
print("Left Shift:", result_left_shift)
print("Right Shift:", result_right_shift)


a = 5.0
b = 3.0

# Converting floating-point values to integers and then performing bitwise AND
result_and = int(a) & int(b)

print("Bitwise AND:", result_and)
