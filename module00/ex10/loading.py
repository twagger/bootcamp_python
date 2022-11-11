"""This module implements a loading bar on a list"""
import time


# Progress bar on a list
def ft_progress(lst):
    """Function to add a loading bar when iterating through a list"""
    try:
        i = 1
        progress_bar_size = 30
        start = time.time()
        lstlen = len(lst)
        for item in lst:
            percent = i * 100 / lstlen
            elapsed_time = time.time() - start
            curr_size = progress_bar_size * percent // 100
            progress_bar = ('=' * (int(curr_size) - 1)) + '>'
            eta = elapsed_time / (percent / 100)
            print(f'ETA : {eta:5.2f}s [{percent:3.0f}%][{progress_bar:30s}] '
                  f'{i}/{lstlen} | elapsed time {elapsed_time:.2f}s', end='\r')
            i += 1
            yield item
    except TypeError as exc:
        raise TypeError("This is not a list") from exc


# Test program
def main():
    """Test program"""
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)


main()
