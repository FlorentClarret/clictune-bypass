import requests

from clictune_bypass import get_url
from clictune_bypass.tests.conftest import ClictuneBypassTest


class TestGetUrl(ClictuneBypassTest):
    def test_link_found(self) -> None:
        self.assertEqual(
            "https://www.google.com/", get_url("https://www.mylink1.biz/bypass")
        )

    def test_link_invalid(self) -> None:
        with self.assertRaises(requests.exceptions.HTTPError) as error:
            self.assertEqual(
                "https://www.google.com/", get_url("https://www.mylink1.biz/bypass")
            )

        assert error.exception.response.status_code == 404

    def test_link_missing(self) -> None:
        self.assertIsNone(get_url("https://www.mylink1.biz/bypass"))
