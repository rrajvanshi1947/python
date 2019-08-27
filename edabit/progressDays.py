def progress_days(runs):
	progressDays = 0
	for i in range(len(runs)):
		if i == len(runs) - 1:
			break
		if runs[i] < runs[i+1]:
			progressDays += 1
	return progressDays

print(progress_days([1,3,2,4]))