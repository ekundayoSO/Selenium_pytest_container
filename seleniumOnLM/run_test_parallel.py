import pytest

from seleniumOnLM.addProductsToCart import run_test_on_edge
from seleniumOnLM.assertProductInCart import run_test_on_edge2
from seleniumOnLM.assertSubTotal import run_test_on_firefox2
from seleniumOnLM.deleteProducts import run_test_on_chrome2
from seleniumOnLM.loginTest import run_test_on_firefox
from seleniumOnLM.registrationTest import run_test_on_chrome

num_workers = 6

if __name__ == "__main__":
    run_test_on_chrome()
    run_test_on_firefox()
    run_test_on_edge()
    run_test_on_edge2()
    run_test_on_firefox2()
    run_test_on_chrome2()

    pytest.main(['-n', str(num_workers), '--verbose', '--capture=no', 'seleniumOnLM'])
