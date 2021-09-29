from vjyscan.cores.version_cmp import *

assert joomla_cmp("0.2.3", "0.2.3") == True, "OK"
assert joomla_cmp("2.3.7", "2.0.0<=2.5.7") == True, "OK"
assert joomla_cmp("2.3.5", "1.1.1<=1.1.3") == False, "OK"
