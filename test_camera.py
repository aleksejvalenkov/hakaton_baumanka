# Подключаем необходимые библиотеки
from picamera2 import Picamera2, Preview
from time import sleep

# Создаём объект для работы с камерой
camera = Picamera2()

# Настраиваем окно предпросмотра
preview_config = camera.create_preview_configuration()
camera.configure(preview_config)

# Запускаем окно предпросмотра сигнала с камеры на экране поверх всех окон
camera.start_preview(Preview.QTGL)

# Включаем камеру
camera.start()

# Ставим паузу на 10 секунд
sleep(10)

# Выключаем камеру
camera.stop()

# Выключаем окно предпросмотра
camera.stop_preview()