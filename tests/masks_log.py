from logs.masks import apply_mask
import logging


def test_apply_mask_with_logging(caplog):
    with caplog.at_level(logging.INFO):
        result = apply_mask("123456789", "*****")
        assert result == "***"
        assert "Применение маски ***** к данным: 123456789" in caplog.text
        assert "Маскированные данные: ***" in caplog.text
