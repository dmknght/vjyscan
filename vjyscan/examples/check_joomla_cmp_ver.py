from vjyscan.cores.version_cmp import *

assert joomla_cmp("0.2.3", "0.2.3") == True, "OK"

assert joomla_cmp("2.3.7", "2.0.0<=2.5.7") == True, "OK"
assert joomla_cmp("2.3.5", "1.1.1<=1.1.3") == False, "OK"

assert joomla_cmp("2.0.0", "2.0.0=<=2.5.7") == True, "OK"
assert joomla_cmp("1.9.9", "2.0.0=<=2.5.7") == False, "OK"

assert joomla_cmp("2.1.0", "<=2.5.7") == True, "OK"
assert joomla_cmp("2.6.0", "<=2.5.7") == False, "OK"
