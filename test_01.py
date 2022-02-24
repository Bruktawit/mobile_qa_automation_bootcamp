import logging
import pytest


class Test01Android:
    @pytest.mark.parametrize('os', ['android'])
    def test_01(self, request, os):
        logging.info(request.node.name)
        logging.info(os)

    @classmethod
    def setup_class(cls):
        logging.info(Test01Android.setup_class.__name__)

    @classmethod
    def teardown_class(cls):
        logging.info(Test01Android.teardown_class.__name__)

    def setup_method(self):
        logging.info(Test01Android.setup_method.__name__)

    def teardown_method(self):
        logging.info(Test01Android.teardown_method.__name__)