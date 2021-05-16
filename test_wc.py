import word_count

def test_normal_case():
	value = ("I am taking 15 credits this term")
	assert word_count.wCount(value) == 7

def test_bad_case():
	value = ("    ")
	assert word_count.wCount(value) == 0

def test_edge_case():
	value = ("1")
	assert word_count.wCount(value) == 1
