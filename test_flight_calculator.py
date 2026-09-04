# test_flight_calculator.py

import pytest
from flight_calculator import calculate_flight_time

def test_calculate_flight_time_typical_payload():
    # Test with a positive weight
    assert calculate_flight_time(1000) == 180 - (0.1 * 1000)

def test_calculate_flight_time_zero_payload():
    # Test with zero payload
    assert calculate_flight_time(0) == 180

def test_calculate_flight_time_negative_weight():
    # Test with a negative weight, expecting a ValueError
    with pytest.raises(ValueError, match="Payload weight cannot be negative."):
        calculate_flight_time(-100)

def test_calculate_flight_time_result_zero():
    # Test where the formula would produce a negative result, expecting 0
    assert calculate_flight_time(2000) == 0

def test_calculate_flight_time_boundary_case():
    # Test with a weight that results in exactly 0 flight time
    assert calculate_flight_time(1800) == 0

