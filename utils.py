from datetime import timedelta

def time_diff (tdelta):

	# if more than a day
	if tdelta.total_seconds() > 86400:
		return '{} days'.format(abs(tdelta.total_seconds() / 86400))
	# if more than an hour
	elif tdelta.total_seconds() > 3600:
		return '{} hours'.format(abs(tdelta.total_seconds() / 3600))
	# if more than a minute
	elif tdelta.total_seconds() > 60:
		return '{} minutes'.format(abs(tdelta.total_seconds() / 60))
	# or just return seconds
	else:
		return '{} seconds'.format(abs(tdelta.total_seconds()))