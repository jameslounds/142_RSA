def modular_exponentiate(x, y, n):
    """
    An algorithm that computes the value c: x^y === c (mod n)
    We first get the binary representation of the exponent.
    For each bit of this, we calculate the value of x to the bit's place value.
    Since we're going in powers of 2, we are squaring each time
    If the current bit is a 1, we multiply our total by the current square.
    """
    binary_representation = "{0:b}".format(y)
    running_total = 1
    current_square = x

    for bit in binary_representation[::-1]:
        if bit == "1":
            running_total = (running_total * current_square) % n
        current_square = (current_square ** 2) % n

    return running_total
