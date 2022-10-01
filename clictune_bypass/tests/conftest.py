from urllib.request import Request

from vcr import VCR
from vcr_unittest import VCRTestCase


def custom_headers_check(new_request: Request, cassette_request: Request):
    headers1 = {k: v for k, v in new_request.headers.items() if k != "User-Agent"}
    headers2 = {k: v for k, v in cassette_request.headers.items() if k != "User-Agent"}
    assert headers1 == headers2, f"{headers1} != {headers2}"


class ClictuneBypassTest(VCRTestCase):
    record_mode = "once"

    def _get_vcr(self, **kwargs) -> VCR:
        vcr = super()._get_vcr(**kwargs)
        vcr.register_matcher("headers", custom_headers_check)
        vcr.match_on = vcr.matchers.keys()
        vcr.record_mode = self.record_mode
        return vcr

    def _get_cassette_name(self) -> str:
        return f"{self.__class__.__name__}.{self._testMethodName}.yaml"
