from math import sqrt, pow, hypot
from pi_circumfirance import get_circumfirance

list_of_strings = ['1', '2', '3', '139', '228', 'one', 'two', 'three']


# Integrated functions
def test_intergrated_functions():
    assert list(filter(str.isdigit, list_of_strings)) == ['1', '2', '3', '139', '228']
    assert list(filter(str.isidentifier, list_of_strings)) == ['one', 'two', 'three']
    assert list(filter(lambda x: len(x) > 2, list_of_strings)) == ['139', '228', 'one', 'two', 'three']

    assert list(map(str.upper, list_of_strings)) == ['1', '2', '3', '139', '228', 'ONE', 'TWO', 'THREE']
    assert list(map(lambda x: 'point {}'.format(x), list_of_strings)) == ['point 1', 'point 2', 'point 3', 'point 139',
                                                                          'point 228', 'point one', 'point two',
                                                                          'point three']

    assert sorted(list_of_strings) == ['1', '139', '2', '228', '3', 'one', 'three', 'two']
    assert sorted(list_of_strings, reverse=True) == ['two', 'three', 'one', '3', '228', '2', '139', '1']


# Math functions
def test_math_functions():
    assert get_circumfirance(3) == 18.84955592153876
    assert get_circumfirance(6) == 37.69911184307752
    assert get_circumfirance(9) == 56.548667764616276
    assert get_circumfirance(12) == 75.39822368615503
    assert get_circumfirance(15) == 94.24777960769379

    assert sqrt(4) == 2
    assert sqrt(8) == 2.8284271247461903
    assert sqrt(16) == 4
    assert sqrt(32) == 5.656854249492381
    assert sqrt(64) == 8

    assert pow(2, 4) == 16
    assert pow(2, 6) == 64
    assert pow(2, 8) == 256
    assert pow(2, 10) == 1024
    assert pow(2, 12) == 4096

    assert hypot(1, 4) == 4.123105625617661
    assert hypot(2, 6) == 6.324555320336759
    assert hypot(3, 8) == 8.54400374531753
    assert hypot(4, 10) == 10.770329614269007
    assert hypot(5, 12) == 13
