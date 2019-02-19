# **************************************************************************** #
#                                                                              #
#                                                                              #
#    pharmacy-counting.py                                                      #
#                                                                              #
#    By: Chethana Krishna Murthy                                               #
#                                                                              #
#    Created: 2019/02/18 12:59:41                                              #
#    Updated: 2019/02/18 17:17:58 by ckrishna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import csv
import os

def input_check(fname):

    fileid = open(fname, 'r', encodings='utf-8')

    ids = []
    for line_num, line in enumerate(fileid):
        if line_num == 0:
            cline = line.split(",")
            if cline[0] != "id":
                raise Exception("column is not valid")
            if line_num > 0:
                cline = line.split(",")
                ids.append(cline[0])
            return len(ids) == len(set(ids))

def prescription_check(line_num, line):

    cline = line.split(",")

    pid = cline[0]
    last_name = cline[1]
    first_name = cline[2]
    drug_name = cline[3]
    drug_cost = cline[4].rstrip()

    try:
        if (len(cline) == 5 and
                isinstance(int(pid), (int)) and
                len(last_name) > 0 and
                not isinstance(last_name, (int, float, complex)) and
                len(first_name) > 0 and
                not isinstance(first_name, (int, float, complex)) and
                len(drug_name) > 0 and
                isinstance(int(drug_cost), (int))):
            return True
        else:
            print("bad data in line", (line_num))
            return False
        except ValueError:
            print("bad data in line", (line_num))
            return False

def zerofile_check(fpath)
    return (os.path.isfile(fpath) and os.path.getsize(fpath) > 0)

def duplicates(lst, item):
    return[i for i,x in  enumerate(lst) if x == item]
