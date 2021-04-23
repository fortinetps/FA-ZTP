import yaml, json
from fortigate_schema import get_schema

with open('./test/TEST_FGT1.yml', 'r') as f:
    test_fgt1 = yaml.safe_load(f.read())

with open('./test/TEST_FGT2.yml', 'r') as f:
    test_fgt2 = yaml.safe_load(f.read())

schema = get_schema()
validated = schema.validate(test_fgt1)
is_valid = schema.is_valid(test_fgt1)
if is_valid:
    print("TEST-FGT1 OK!")
else:
    print("TEST-FGT1 FAIL!")

validated = schema.validate(test_fgt2)
is_valid = schema.is_valid(test_fgt2)
if is_valid:
    print("TEST-FGT2 OK!")
else:
    print("TEST-FGT2 FAIL!")

