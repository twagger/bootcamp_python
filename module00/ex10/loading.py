import time

# Progress bar on a list
def ft_progress(lst):
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
		print("ETA : {:5.2f}s [{:3.0f}%][{:30s}] {}/{} | elapsed time {:.2f}s".format(eta, percent, progress_bar, i, lstlen, elapsed_time), end='\r')
		i += 1
		yield item

# Test program
listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)