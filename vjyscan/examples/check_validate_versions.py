from vjyscan.cores.version_cmp import __validate_versions

assert __validate_versions(("1.1.1", "1.2.1")) == ("1.1.1", "1.2.1"), "Wrong line 3"
assert __validate_versions(("1.0.1", "1.2", "1.3.4.5")) == ("1.0.1.0", "1.2.0.0", "1.3.4.5"), "wrong line 4"
assert __validate_versions(("0.1", "2.1.3")) == ("0.1.0", "2.1.3"), "Wrong ('0.1', '2.1.3')"
assert __validate_versions(("0.1", "2.1.3")) != ("0.1", "2.1.3"), "Wrong ('0.1', '2.1.3')"
assert __validate_versions(("0.1.2", "2.1")) == ("0.1.2", "2.1.0"), "Wrong ('0.1.2', '2.1')"
assert __validate_versions(("0.1.2", "2.1")) != ("0.1.2", "2.1"), "Wrong ('0.1.2', '2.1')"
