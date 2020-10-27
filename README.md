# dlink_upload_config


Скрипт для скачивания файлов конфигурации на tftp сервер.

Работает для моделей:
Dlink DES3010G/3018/3200/3526/1228/1210-28ME
Dlink DGS3120-24SC/DGS3420/

SNR SNR-S2995G-24FX
Eltex MES2324FB

Tp-Link JestStream Series (2500,2600)

Для работы вам потребуется Python3.5+

Запуск скрипта:

1)Склонируйте репозиторий
2)Установите и активируйте вирутальное окружение.
  python3.7 -m venv venv
  source venv/bin/activate
3)Установите зависимости pip intall -r requirements.txt
4)Создайте файл .env и укажите адрес вашего tftp сервера в переменной TFTP_SERVER
5)Откройте скрипт и отредактируйте список ip адресов в переменной sw_list
