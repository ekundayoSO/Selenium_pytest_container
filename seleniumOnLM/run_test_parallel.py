import pytest

from seleniumOnLM.AddProductsToCart import run_test_on_edge
from seleniumOnLM.DeleteProducts import run_test_on_chrome2
from seleniumOnLM.LoginTest import run_test_on_firefox
from seleniumOnLM.RegistrationTest import run_test_on_chrome

num_workers = 4

if __name__ == "__main__":
    run_test_on_chrome()
    run_test_on_firefox()
    run_test_on_edge()
    run_test_on_chrome2()

    pytest.main(['-n', str(num_workers), '--verbose', '--capture=no', 'seleniumOnLM'])
