import pytest

from seleniumOnVM.AddProductsToCart import run_test_on_chrome
from seleniumOnVM.DeleteProducts import run_test_on_firefox
from seleniumOnVM.LoginTest import run_test_on_edge
from seleniumOnVM.RegistrationTest import run_test_on_chrome2

num_workers = 4

if __name__ == "__main__":
    run_test_on_chrome()
    run_test_on_firefox()
    run_test_on_edge()
    run_test_on_chrome2()

    pytest.main(['-n', str(num_workers), '--verbose', '--capture=no', 'seleniumOnVM'])
