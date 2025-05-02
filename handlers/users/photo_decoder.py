# import os
# import cv2
# from pathlib import Path
# from aiogram import types
# import logging
#
# from keyboards.default.defold_keys import main_menu
# from loader import dp
#
# # Настройка пути для загрузок
# DOWNLOAD_PATH = Path("downloads/categories/photos","rb")
# DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)
#
# # Настройка логгирования
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
#
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def photo_handler(message: types.Message):
#     try:
#         # Генерация имени файла
#         existing_files = list(DOWNLOAD_PATH.glob("file_*.jpg"))
#         next_index = len(existing_files) + 1
#         filename = f"file_{next_index}.jpg"
#         file_path = DOWNLOAD_PATH / filename
#
#         # Сохранение фото
#         await message.photo[-1].download(destination_file=file_path)
#         await message.answer("Фото получено, начинаю обработку...")
#
#         # Проверка что файл сохранен
#         if not file_path.exists():
#             await message.reply("Ошибка: не удалось сохранить изображение")
#             return
#
#         # Чтение и обработка изображения
#         image = cv2.imread(str(file_path))
#         if image is None:
#             await message.reply("Не удалось прочитать изображение")
#             return
#
#         # Попытка распознавания QR-кода
#         detector = cv2.QRCodeDetector()
#         data, _, _ = detector.detectAndDecode(image)
#
#         if data:
#             await message.reply(f"Найден QR-код: {data}", reply_markup=main_menu)
#         else:
#             # Дополнительная попытка с обработкой изображения
#             gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#             _, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
#             data, _, _ = detector.detectAndDecode(threshold)
#
#             if data:
#                 await message.reply(f"QR-код (после обработки): {data}", reply_markup=main_menu)
#             else:
#                 await message.reply("QR-код не обнаружен. Пожалуйста, отправьте четкое изображение QR-кода.")
#
#     except Exception as e:
#         logger.error(f"Ошибка при обработке фото: {str(e)}", exc_info=True)
#         await message.reply("Произошла ошибка при обработке изображения. Пожалуйста, попробуйте еще раз.")
#
# import os
# import cv2
# from pathlib import Path
# from aiogram import types
# from keyboards.default.defold_keys import main_menu
# from loader import dp
#
# # Папка для сохранения изображений
# DOWNLOAD_PATH = Path("downloads/categories/photos")
# DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)
#
#
# def decode_qr_data(raw_bytes):
#     """Попытка декодировать байты с учетом кодировок."""
#     try:
#         # Пробуем UTF-8
#         decoded_text = raw_bytes.decode('utf-8', errors='strict')
#     except UnicodeDecodeError:
#         # Если ошибка, пробуем Windows-1251
#         decoded_text = raw_bytes.decode('windows-1251', errors='replace')
#     return decoded_text
#
#
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def photo_handler(message: types.Message):
#     try:
#         # Сохраняем фото
#         existing_files = list(DOWNLOAD_PATH.glob("file_*.jpg"))
#         next_index = len(existing_files) + 1
#         filename = f"file_{next_index}.jpg"
#         file_path = DOWNLOAD_PATH / filename
#         await message.photo[-1].download(destination_file=file_path)
#         await message.answer("Фото получено, начинаю обработку...")
#
#         # Читаем изображение
#         image = cv2.imread(str(file_path))
#         if image is None:
#             await message.reply("Не удалось прочитать изображение")
#             return
#
#         # Детектор QR-кодов
#         detector = cv2.QRCodeDetector()
#         data, _, _ = detector.detectAndDecode(image)
#
#         # Если не удалось распознать QR-код, пробуем улучшить изображение
#         if not data:
#             gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#             _, threshold = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
#             data, _, _ = detector.detectAndDecode(threshold)
#
#         if data:
#             try:
#                 # Преобразуем строку в байты (как они были в QR)
#                 raw_bytes = data.encode('latin1')
#
#                 # Декодируем данные с попыткой разных кодировок
#                 decoded_text = decode_qr_data(raw_bytes)
#
#                 await message.reply(
#                     f"QR-код (кодировка: UTF-8 или Windows-1251):\n<code>{decoded_text}</code>",
#                     parse_mode="HTML",
#                     reply_markup=main_menu
#                 )
#             except Exception as e:
#                 await message.reply(f"Ошибка при чтении данных QR-кода: {e}")
#         else:
#             await message.reply("QR-код не найден. Попробуйте отправить более четкое изображение.")
#
#     except Exception as e:
#         await message.reply(f"Произошла ошибка при обработке изображения:\n{e}")
import os
import cv2
from pathlib import Path
from aiogram import types
import numpy as np
import re

from keyboards.default.defold_keys import main_menu
from loader import dp

# Создаем папку для загрузок
dow_path = Path("downloads/categories/photoes")
dow_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(message: types.Message):
    folder_path = 'downloads/categories/photoes'

    # Находим следующий номер файла более безопасным способом
    files = [f for f in os.listdir(folder_path) if f.startswith('file_') and f.endswith('.jpg')]
    next_index = 1
    if files:
        # Используем регулярное выражение для извлечения числа из имени файла
        # Это более безопасно, так как учитывает только файлы с правильным форматом
        indices = []
        for file in files:
            match = re.search(r'file_(\d+)\.jpg', file)
            if match:
                indices.append(int(match.group(1)))

        if indices:
            next_index = max(indices) + 1

    # Сохраняем фото
    filename = f"file_{next_index}.jpg"
    file_path = os.path.join(folder_path, filename)
    await message.photo[-1].download(destination_file=file_path)

    await message.answer("Обработка картинки...")

    try:
        # Чтение изображения
        image = cv2.imread(file_path)

        # Пытаемся использовать встроенный в OpenCV детектор QR-кодов
        detector = cv2.QRCodeDetector()

        # Проверяем только, есть ли QR-код на изображении
        retval, points = detector.detect(image)

        if retval:
            # QR-код обнаружен, но нужно аккуратно декодировать данные
            try:
                # Вызываем detectAndDecode через исключение - мы знаем что он может сломаться,
                # но иногда он работает, и мы хотим попробовать
                data, _, _ = detector.detectAndDecode(image)

                # Если всё получилось - отлично!
                if data:
                    await message.reply(
                        text=f"✅ <b>QR-код готов!</b>\n\n"
                             f"📋 <b>Содержимое:</b>\n<code>{data}</code>\n\n"
                             f"🔍 <i>Отсканируйте код или скопируйте текст</i>\n"
                             f"▬▬▬▬▬▬▬▬▬▬▬\n"
                             f"🤖 Создано: <code>@QRcode_webr1_bot</code>",
                        parse_mode="HTML",
                        reply_markup=main_menu
                    )
                else:
                    # Данные не были извлечены напрямую. Используем резервный подход.
                    await message.reply("QR-код найден, но содержимое не удалось декодировать. "
                                        "Попробуйте более чёткое изображение.", reply_markup=main_menu)

            except UnicodeDecodeError:
                # Если возникла ошибка кодировки, используем низкоуровневый подход
                # Извлекаем QR-код из изображения
                x, y, w, h = cv2.boundingRect(points)
                qr_region = image[y:y + h, x:x + w]

                # Сохраняем вырезанный QR-код с новым именем, не конфликтующим с основными файлами
                region_path = os.path.join(folder_path, f"region_{next_index}.jpg")
                cv2.imwrite(region_path, qr_region)

                # Экспериментальный подход - попытаемся восстановить данные вручную
                # Преобразуем изображение в бинарное для лучшего контраста
                gray = cv2.cvtColor(qr_region, cv2.COLOR_BGR2GRAY)
                _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

                # Предлагаем пользователю использовать другой декодер
                await message.reply(
                    "QR-код содержит данные в нестандартной кодировке. "
                    "Пожалуйста, используйте один из онлайн-декодеров QR-кодов, например "
                    "https://zxing.org/w/decode.jspx для декодирования.",
                    reply_markup=main_menu
                )

                # Отправляем вырезанный QR-код пользователю
                with open(region_path, 'rb') as file:
                    await message.answer_photo(
                        file,
                        caption="Вот обнаруженный QR-код. Используйте онлайн-декодер для его чтения."
                    )
        else:
            await message.reply("QR-code не найден, пожалуйста, отправьте понятный QR-код.", reply_markup=main_menu)

    except Exception as e:
        # В случае любой другой ошибки
        import traceback
        error_details = traceback.format_exc()
        await message.reply(f"Ошибка при обработке: {str(e)}\n\nПодробности:\n{error_details[:800]}",
                            reply_markup=main_menu)