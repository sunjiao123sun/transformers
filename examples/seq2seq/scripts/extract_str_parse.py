# the scripts to extract the sentences from the parse

import re
def convert_parse_to_str(string):
    new_list = []
    for ele in string.split(" "):
        if ")" in ele:
            new_list.append(str(re.sub('\).*','',ele)))
    new_str = " ".join(ele for ele in new_list)
    return new_str

input_data = "../result_paranmt/bart-base-set2.txt"
output_data = open("../result_paranmt/bart-base-set2-extract.txt", "w+")

for line in open(input_data, "r").readlines():
    line = line.strip()
    output_data.write(convert_parse_to_str(line))
    output_data.write("\n")

