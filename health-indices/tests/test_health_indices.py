from health_indices import __version__
from health_indices import bmi


def test_version():
    assert __version__ == '0.0.1'


def test_bmi():
    results = bmi(54,1.70)
    assert results == 18.0
    
