import os
import threading
import time
from multiprocessing import Process
from threading import Thread

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"Processing file from {path} " f"in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    for i in range(200_000_000):
        pass


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(
        f"Downloading image from {image_url}"
        f"in thread "
        f"{threading.current_thread().name}"
    )
    time.sleep(2)
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


def proces():
    list_file = ["rockyou.txt", "rockyou_2.txt", "rockyou3.txt"]
    process = [
        Process(
            target=encrypt_file,
            args=(path_to,),
        )
        for path_to in list_file
    ]
    for proces in process:
        proces.start()
    for proces in process:
        proces.join()


def thread():
    threads_1 = Thread(
        target=download_image,
        args=("https://picsum.photos/1000/1000",),
    )
    threads_2 = Thread(
        target=download_image,
        args=("https://picsum.photos/1000/1000",),
    )
    threads_1.start()
    threads_2.start()
    threads_1.join()
    threads_2.join()


def main():
    total_start = time.perf_counter()

    start_proces = time.perf_counter()
    proces()
    finish_proces = time.perf_counter() - start_proces

    start_thread = time.perf_counter()
    thread()
    finish_thread = time.perf_counter() - start_thread

    total_finish = time.perf_counter() - total_start
    return finish_proces, finish_thread, total_finish


if __name__ == "__main__":
    try:
        finish_proces, finish_thread, total_finish = main()
        print(
            f"Time taken for CPU-bound task: {finish_proces},"
            f"I/O-bound task: {finish_thread},"
            f"Total: {total_finish} seconds"
        )

    except Exception as e:
        print(f"Error occurred: {e}")
