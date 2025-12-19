import requests
import logging

logger = logging.getLogger(__name__)

def get_next_race():
    """Получает информацию о следующей гонке"""
    try:
        response = requests.get("https://f1api.dev/api/v1/races/next")
        data = response.json()
        return data
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return None

def get_last_result():
    """Получает результаты последней гонки"""
    try:
        response = requests.get("https://f1api.dev/api/v1/races/last")
        data = response.json()
        return data
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return None