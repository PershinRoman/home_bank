from logs.logging_config import loggers

# Получаем логер для модуля masks
logger = loggers["masks"]


def apply_mask(data: str, mask: str) -> str:
    """
    Применяет маску к данным.

    :param data: Дата для маскировки.
    :param mask: Маска, которая будет применена.
    :return: Маскированные данные.
    """
    try:
        logger.info(f"Применение маски {mask} к данным: {data}")
        # Пример маскировки (может быть заменен на вашу логику)
        masked_data = f"{mask[:3]}***{mask[-3:]}"
        logger.info(f"Маскированные данные: {masked_data}")
        return masked_data
    except Exception as e:
        logger.error(f"Ошибка применения маски: {e}")
        return ""
