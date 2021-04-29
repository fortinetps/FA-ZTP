import argparse
import yaml, json
from fortigate_schema import get_schema


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", required=True,
                    help="The list of FortiGates paths that have been rendered "
                         "to {{role_path}}/files/tmp/fortigates -- as json")
args = parser.parse_args()
# convert the json back into a list of dictionaries
fgt_paths = json.loads(args.data)
# print(fgt_paths)
ztp_fortigates = []
# get all the fgt files' yaml data
for path in fgt_paths:
    with open(path, "r") as tmp_fgt_file:
        fgt_data_list = yaml.load(tmp_fgt_file, Loader=yaml.FullLoader)
        # we write these tmp files as a dictionary inside a list, for ease of merging in ansible.
        # but we need to strip that dictionary from the list before we put it in yet another list
        # so let's just get index 0 (there should only be 1 fortigate per file anyways)
        ztp_fortigates.append(fgt_data_list[0])
    tmp_fgt_file.close()
# print(ztp_fortigates)

# load the schema from ./fortigate_schema.py
schema = get_schema()
validated = schema.validate(ztp_fortigates)
is_valid = schema.is_valid(ztp_fortigates)
print(is_valid)

