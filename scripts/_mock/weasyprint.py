"""Mock для weasyprint."""

import os
import sys
from unittest.mock import MagicMock

# делаем Mock только для CI на GitHub
if "GITHUB_ACTIONS" in os.environ:
    # создадим клас для мока
    class MockWeasyPrint:
        """Mock для WeasyPrint."""

        __name__ = "weasyprint"
        __version__ = "99.99.9"
        __file__ = "/mock/weasyprint/__init__.py"
        __path__ = ["/mock/weasyprint"]  # noqa: RUF012

        # доп. модули
        class HTML:
            __name__ = "weasyprint.HTML"

            def __call__(self, *args, **kwargs):
                return MagicMock()

            def write_pdf(self, *args, **kwargs):
                return b"mock pdf content"

        class css:
            __name__ = "weasyprint.css"

        class text:
            __name__ = "weasyprint.text"

        class fonts:
            __name__ = "weasyprint.fonts"

        class ffi:
            __name__ = "weasyprint.ffi"

    mock_instance = MockWeasyPrint()
    sys.modules["weasyprint"] = mock_instance

    # добавим др. модули
    sys.modules["weasyprint.HTML"] = mock_instance.HTML
    sys.modules["weasyprint.css"] = mock_instance.css
    sys.modules["weasyprint.text"] = mock_instance.text
    sys.modules["weasyprint.fonts"] = mock_instance.fonts