__author__ = 'SELO77'


def to_numeral(number, numeral):
    """
    return list of elements of given numeral
    :param number: decimal number
    :param numeral: number of numeral
    :return: list of elements of given numeral.
    """
    result = []
    while True:
        if (number / numeral) < 1:
            result.append(number)
            break
        b = number % numeral
        number = int(number / numeral)
        result.append(b)
    return result.reverse()


def solution(n, t, m, t_order):
    """
    :param n: numeral
    :param t: number of answer
    :param m: number of gamer
    :param t_order: tube order
    :return: sequence of each answer for tube
    """
    result = ""
    current_index = 1
    current_decimal_number = 0

    while True:
        if t == len(result): break

        current_numeral_numbers = to_numeral(current_decimal_number, n)
        while current_numeral_numbers:
            current_numeral_number = current_numeral_numbers.pop()
            if current_index % m == t_order:
                result += str(current_numeral_number)
            current_index += 1

        current_decimal_number += 1

    return result


def test_solution():
    assert '04' == solution(10, 2, 4, 1)
    assert '01' == solution(2, 2, 2, 1)


if __name__ == '__main__':
    # print(to_numeral(8, 2))
    # print(to_numeral(1, 2))
    print('==')
    test_solution()