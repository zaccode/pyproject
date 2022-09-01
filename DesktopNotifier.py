from plyer import notification
import time as tm

if __name__ == '__main__':
    while True:
        notification.notify(
            title="***Take Rest ***",
            message="RandomDavis i got the file in PycharmProjects\pythonProject\venv\Lib\site-packages when it was installed ",
            timeout=5)

        tm.sleep(10)
