import logging
import pytest

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class Test01Android:
    @pytest.mark.parametrize('os', ['android'])
    def test_01(self, request, os):
        logger.info(request.node.name)
        logger.info(os)

    @classmethod
    def setup_class(cls):
        logger.info(Test01Android.setup_class.__name__)

    @classmethod
    def teardown_class(cls):
        logger.info(Test01Android.teardown_class.__name__)

    def setup_method(self):
        logger.info(Test01Android.setup_method.__name__)

    def teardown_method(self):
        logger.info(Test01Android.teardown_method.__name__)