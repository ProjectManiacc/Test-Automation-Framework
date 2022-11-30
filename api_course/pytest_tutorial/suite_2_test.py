import pytest

pytestmark = pytest.mark.fe


class TestCheckout(object):

    def test_checkout_as_guest(self):
        print("Checkout as guest")

    def test_checkout_with_existing_user(self):
        print("Checkout with existing user")