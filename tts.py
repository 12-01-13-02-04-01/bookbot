import threading
import time
from pathlib import Path

import soundfile as sf  # pyright: ignore[reportMissingImports]
from kokoro_onnx import Kokoro

kokoro = Kokoro("data/kokoro-v1.0.onnx", "data/voices-v1.0.bin")


def heartbeat(stop_event, interval=10):
    while not stop_event.is_set():
        print(f"[{time.strftime('%H:%M:%S')}]--running...")
        time.sleep(interval)


stop_signal = threading.Event()

timer_thread = threading.Thread(target=heartbeat, args=(stop_signal, 10))
timer_thread.daemon = True  # Thread dies if main process exits
timer_thread.start()


def make_file(content: str, title: str):
    size = 10000
    chunks = [content[i : i + size] for i in range(0, len(content), size)]

    i = 0

    try:
        print("Generating file...")
        for chunk in chunks:
            i += 1

            if i > 2:
                break

            Path(f"output/{title}[{i}].wav").touch(exist_ok=True)
            print(f"proccessing chunk {i}")
            samples, sample_rate = kokoro.create(
                chunks[i - 1], voice="af_sarah", speed=1.0, lang="en-us"
            )

            sf.write(f"output/{title}[{i}].wav", samples, sample_rate)
    finally:
        stop_signal.set()
        timer_thread.join()
        print("Task complete.")
