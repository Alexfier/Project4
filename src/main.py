def mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя только последние 4 цифры."""
    parts = account_number.split()

    # Проверяем, что часть с номером счета есть и что это все цифры
    if len(parts) > 1 and parts[-1].isdigit():
        # Длина счета 6 цифр
        if len(parts[-1]) == 6:
            return f"{parts[0]} **{parts[-1][-3:]}"  # Маскируем все кроме последних 3 цифр
        # Длина счета более 4 цифр
        elif len(parts[-1]) >= 4:
            return f"{parts[0]} **{parts[-1][-4:]}"  # Маскируем все кроме последних 4 цифр

    return account_number  # Возвращаем оригинал, если формат не соответствует

def mask_card(card_info):
    """Маскирует номер карты, оставляя название карты и последние 4 цифры."""
    # Проверяем, если в строке есть название карты (например, "Visa Gold")
    if " " in card_info and not card_info.replace(" ", "").isdigit():
        parts = card_info.rsplit(" ", 1)  # Разделяем название карты и номер
        if len(parts) != 2:
            return card_info  # Если формат некорректный, возвращаем как есть
        card_name = parts[0]  # Название карты
        card_number = parts[1]  # Номер карты
    else:
        card_name = ""  # Название карты отсутствует
        card_number = card_info.strip()  # Убираем лишние пробелы

    # Убираем пробелы из номера карты для обработки
    card_number_clean = card_number.replace(" ", "")

    # Проверяем, что номер карты состоит из цифр и имеет достаточную длину
    if not card_number_clean.isdigit() or len(card_number_clean) < 12:
        return card_info  # Если формат некорректный, возвращаем оригинал

    # Формируем маскированный номер карты
    masked_number = f"{card_number_clean[:4]} {card_number_clean[4:6]}** **** {card_number_clean[-4:]}"

    # Возвращаем название карты и маскированный номер
    if card_name:
        return f"{card_name} {masked_number}"
    return masked_number
