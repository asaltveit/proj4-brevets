"""
Nose tests for acp_times.py
"""
import arrow
import acp_times
import nose

def test_float_to_time_no_base():
	"""
	Float_to_time tests with no base (base = 0)
	"""
	assert acp_times.float_to_time(16.33, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm')) == '2017-01-01T16:20:00+00:00'
	assert acp_times.float_to_time(2.5, arrow.get('2017-01-04 08:00', 'YYYY-MM-DD HH:mm')) == '2017-01-04T10:30:00+00:00'

def test_float_to_time_base():
	"""
	Float_to_time tests with base = 40
	"""
	assert acp_times.float_to_time(16.33, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm'), 40) == '2017-01-03T08:20:00+00:00'
	assert acp_times.float_to_time(2.5, arrow.get('2017-01-01 00:00', 'YYYY-MM-DD HH:mm'), 40) == '2017-01-02T18:30:00+00:00'

def test_open_brev_200():
	"""
	Open_time tests using brevet distance of 200km
	"""
	assert acp_times.open_time(0, 200, '2017-01-01 00:00') == '2017-01-01T00:00:00+00:00'
	assert acp_times.open_time(150, 200, '2017-01-01 00:00') == '2017-01-01T04:25:00+00:00'
	assert acp_times.open_time(200, 200, '2017-01-01 00:00') == '2017-01-01T05:53:00+00:00'
	
def test_open_brev_1000():
	"""
	Open_time tests using brevet distance of 1000km
	"""
	assert acp_times.open_time(600, 1000, '2017-01-01 00:00') == '2017-01-01T18:48:00+00:00' 
	assert acp_times.open_time(725, 1000, '2017-01-01 00:00') == '2017-01-01T23:16:00+00:00' 
	assert acp_times.open_time(200, 1000, '2017-01-01 00:00') == '2017-01-01T05:53:00+00:00'

def test_open_brev_other():
	"""
	Open_time tests using brevet distances between 200km and 600km
	"""
	assert acp_times.open_time(300, 400, '2017-01-01 00:00') == '2017-01-01T09:00:00+00:00'
	assert acp_times.open_time(555, 600, '2017-01-01 00:00') == '2017-01-01T17:18:00+00:00'

def test_open_nonzero_start():
	"""
	Testing non-zero start times for open_time
	"""
	assert acp_times.open_time(0, 200, '2017-01-01 18:30') == '2017-01-01T18:30:00+00:00'
	assert acp_times.open_time(150, 200, '2017-01-01 02:00') == '2017-01-01T06:25:00+00:00'
	assert acp_times.open_time(725, 1000, '2017-01-01 20:00') == '2017-01-02T19:16:00+00:00'

def test_close_edges():
	"""
	Close_time edge case tests
	"""
	# first control
	assert acp_times.close_time(0, 400, '2017-01-01 00:00') == '2017-01-01T01:00:00+00:00'
	# Last control at 200km brevet distance
	assert acp_times.close_time(200, 200, '2017-01-01 00:00') == '2017-01-01T13:30:00+00:00'
	# Last control at 400km brevet distance
	assert acp_times.close_time(400, 400, '2017-01-01 00:00') == '2017-01-02T03:00:00+00:00'
	# Last control at 1000km brevet distance
	assert acp_times.close_time(1000, 1000, '2017-01-01 00:00') == '2017-01-04T03:00:00+00:00'
	# Another non-rule following case (off by 4 minutes)
	assert acp_times.close_time(249, 400, '2017-01-01 00:00') == '2017-01-01T16:36:00+00:00'

def test_close_normal():
	"""
	Non-edge cases for close_time 
	"""
	# 200km only as control time, not brevet time
	assert acp_times.close_time(200, 400, '2017-01-01 00:00') == '2017-01-01T13:20:00+00:00'
	# under 600km
	assert acp_times.close_time(555, 600, '2017-01-01 00:00') == '2017-01-02T13:00:00+00:00'
	# over 600km
	assert acp_times.close_time(725, 1000, '2017-01-01 00:00') == '2017-01-03T02:56:00+00:00'
	
