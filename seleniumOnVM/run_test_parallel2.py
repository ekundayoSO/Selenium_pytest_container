import pytest

from seleniumOnVM.addProductsToCart import run_test_on_chrome
from seleniumOnVM.assertProductInCart import run_test_on_edge2
from seleniumOnVM.assertSubTotal import run_test_on_firefox2
from seleniumOnVM.deleteProducts import run_test_on_firefox
from seleniumOnVM.loginTest import run_test_on_edge
from seleniumOnVM.registrationTest import run_test_on_chrome2

num_workers = 6

if __name__ == "__main__":
    run_test_on_chrome2()
    run_test_on_edge()
    run_test_on_chrome()
    run_test_on_edge2()
    run_test_on_firefox2()
    run_test_on_firefox()

    pytest.main(['-n', str(num_workers), '--verbose', '--capture=no', 'seleniumOnVM'])
