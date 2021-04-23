import argparse
import yaml, json
from fortigate_schema import get_schema


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", required=True,
                    help="The list of FortiGates that have been rendered "
                         "to {{role_path}}/files/tmp/fortigates -- as json")
args = parser.parse_args()
# convert the json back into a list of dictionaries
ztp_fortigates = json.loads(args.data)
# load the schema from ./fortigate_schema.py
schema = get_schema()
validated = schema.validate(ztp_fortigates)
is_valid = schema.is_valid(ztp_fortigates)
print(is_valid)

