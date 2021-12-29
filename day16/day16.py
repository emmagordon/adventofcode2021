import math

PUZZLE_INPUT = "puzzle_input.txt"

# Type IDs
SUM = 0
PRODUCT = 1
MINIMUM = 2
MAXIMUM = 3
LITERAL_VALUE = 4
GREATER_THAN = 5
LESS_THAN = 6
EQUAL_TO = 7

# Length Type IDs
TOTAL_LENGTH = 0
NUM_SUB_PACKETS = 1

# Operators
OPERATORS = {
    SUM: sum,
    PRODUCT: math.prod,
    MINIMUM: min,
    MAXIMUM: max,
    GREATER_THAN: lambda xs: int(xs[0] > xs[1]),
    LESS_THAN: lambda xs: int(xs[0] < xs[1]),
    EQUAL_TO: lambda xs: int(xs[0] == xs[1])
}


# def parse_part1(binary_packet, ptr=0, version_sum=0):
#     version = int(binary_packet[ptr:ptr+3], 2)
#     print(f"----\nversion={version}")
#     version_sum += version
#     ptr += 3
#
#     type_id = int(binary_packet[ptr:ptr+3], 2)
#     ptr += 3
#
#     if type_id == LITERAL_VALUE:
#         print("LITERAL VALUE")
#         bit_str = ""
#         while True:
#             continuation_bit = binary_packet[ptr]
#             bit_str += binary_packet[ptr + 1:ptr + 5]
#             ptr += 5
#             if continuation_bit == "0":
#                 break
#         literal_value = int(bit_str, 2)
#         print(f"literal_value={literal_value}")
#         return version_sum, ptr
#
#     print("OPERATOR")
#     length_type_id = int(binary_packet[ptr], 2)
#     ptr += 1
#
#     if length_type_id == TOTAL_LENGTH:
#         total_len = int(binary_packet[ptr:ptr+15], 2)
#         print(f"total_len={total_len}")
#         ptr += 15
#
#         start_pos = ptr
#         while ptr < (start_pos + total_len):
#             version_sum, ptr = parse_part1(binary_packet, ptr, version_sum)
#         return version_sum, ptr
#
#     elif length_type_id == NUM_SUB_PACKETS:
#         num_sub_packets = int(binary_packet[ptr:ptr+11], 2)
#         print(f"num_sub_packets={num_sub_packets}")
#         ptr += 11
#         for _ in range(num_sub_packets):
#             version_sum, ptr = parse_part1(binary_packet, ptr, version_sum)
#         return version_sum, ptr
#
#     else:
#         raise RuntimeError("oops...!")


def parse_part2(binary_packet, ptr=0):
    version = int(binary_packet[ptr:ptr+3], 2)
    print(f"----\nversion={version}")
    ptr += 3

    type_id = int(binary_packet[ptr:ptr+3], 2)
    ptr += 3

    if type_id == LITERAL_VALUE:
        print("LITERAL VALUE")
        bit_str = ""
        while True:
            continuation_bit = binary_packet[ptr]
            bit_str += binary_packet[ptr + 1:ptr + 5]
            ptr += 5
            if continuation_bit == "0":
                break
        literal_value = int(bit_str, 2)
        print(f"literal_value={literal_value}")
        return literal_value, ptr

    print(f"OPERATOR={type_id}")
    length_type_id = int(binary_packet[ptr], 2)
    ptr += 1

    values = []
    if length_type_id == TOTAL_LENGTH:
        total_len = int(binary_packet[ptr:ptr+15], 2)
        print(f"total_len={total_len}")
        ptr += 15

        start_pos = ptr
        while ptr < (start_pos + total_len):
            value, ptr = parse_part2(binary_packet, ptr)
            values.append(value)

    elif length_type_id == NUM_SUB_PACKETS:
        num_sub_packets = int(binary_packet[ptr:ptr+11], 2)
        print(f"num_sub_packets={num_sub_packets}")
        ptr += 11

        for _ in range(num_sub_packets):
            value, ptr = parse_part2(binary_packet, ptr)
            values.append(value)

    else:
        raise RuntimeError("oops...!")

    print(f"values={values}")
    operation_result = OPERATORS[type_id](values)
    print(f"operation_result={operation_result}")
    return operation_result, ptr


if __name__ == "__main__":
    with open(PUZZLE_INPUT, "r") as f:
        hex_packet = f.readline().rstrip()

    binary_str = f"{int(hex_packet, 16):0>{len(hex_packet)*4}b}"
    print(binary_str)
    # print(parse_part1(binary_str))
    print(parse_part2(binary_str))
