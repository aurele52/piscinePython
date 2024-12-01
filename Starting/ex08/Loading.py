import sys as sys
import math as math
import shutil
import time

def format_time(seconds):
    """
    Format the given time in seconds as MM:SS.

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted time in the format MM:SS.
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    columns, _ = shutil.get_terminal_size(fallback=(80, 24))
    i = 0
    total = len(lst)
    start_time = time.time()

    while i <= len(lst):
        start = "\r" + f"{int(i / len(lst) * 100):>3}" + "%|"
        elapsed_time = time.time() - start_time
        speed = float(i / elapsed_time)
        if (speed == 0) :
            speed = 1
        eta = (total - i) / speed

        elapsed_formatted = format_time(elapsed_time)
        eta_formatted = format_time(eta)
        end = "| " + str(i) + "/" + str(len(lst)) + " " +f"[{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"
        barLen = (columns - len(start) - len(end) + 1)
        # print()
        # print(len(start), barLen, len(end))
        # print("yes",float(barLen), float(barLen) / 2)
        # print(math.ceil(float(barLen) / 2), math.ceil(float(barLen) // 2))
        bar = "█" * (barLen - int(math.floor(float(barLen * (1 - (i / len(lst)))))))
        bar += "." * int(math.floor(float(barLen * (1 - (i / len(lst))))))
        toPrint = start + bar + end;
        print(toPrint, flush=False, end="")
        yield i - 1
        i += 1

