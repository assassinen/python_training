__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import re
sys.path.append(os.path.join(sys.path[0], '../lib'))
from fastMessageReaderOriginal import MessageReader



def print_missing_sequence(start_seq_num, end_seq_num):
    for i in range(start_seq_num+1, end_seq_num):
        print(i)


def is_correct_sequence(message, last_seq_num, seq_num_type):
    seq_num = int(message[seq_num_type])
    if seq_num_type not in last_seq_num:
        last_seq_num[seq_num_type] = seq_num
    if last_seq_num[seq_num_type] + 1 == seq_num:
        last_seq_num[seq_num_type] = seq_num
    else:
        print_missing_sequence(last_seq_num[seq_num_type], seq_num)
        last_seq_num[seq_num_type] = seq_num

def is_sequence_to_list(message, last_seq_num, seq_num_type):
    seq_num = int(message[seq_num_type])
    if seq_num_type not in last_seq_num:
        last_seq_num[seq_num_type] = []
    last_seq_num[seq_num_type].append(seq_num)

def is_order_book_message(message):
    messageType = message['MessageType']
    return (messageType == 'B' or messageType == 'X' or messageType == 'd')


def applyAction(entry, dictName, depth):
    MDPriceLevel = entry['MDPriceLevel']
    MDUpdateAction = int(entry['MDUpdateAction'])
    MDEntryPx = entry['MDEntryPx']
    MDEntrySize = entry['MDEntrySize']
    MDEntryType = int(entry['MDEntryType'])
    MDEntryTime = entry['MDEntryTime']
    Revision = entry['Revision']

    if MDUpdateAction == 0:
        dictName[entry['SecurityID']][MDEntryType].insert(int(MDPriceLevel) - 1, [MDEntryPx, MDEntrySize, MDEntryTime])
        dictName[entry['SecurityID']][MDEntryType] = dictName[entry['SecurityID']][MDEntryType][0:depth]
    if MDUpdateAction == 1:
        dictName[entry['SecurityID']][MDEntryType][int(MDPriceLevel) - 1] = [MDEntryPx, MDEntrySize, MDEntryTime]
    if MDUpdateAction == 2:
        dictName[entry['SecurityID']][MDEntryType].pop(int(MDPriceLevel) - 1)


changeSecurityID = []

def incremental_book_read(snapshot, dictName, r, depth):
    ignoreField = ['MsgSeqNum', 'RptSeq', 'Revision', 'MDEntryDate', 'MDEntryTime']

    for entry in snapshot['entries']:

        MDEntryType = entry['MDEntryType']
        SecurityID = entry['SecurityID']

        if SecurityID != '414301':
            continue

        if SecurityID not in changeSecurityID:
            changeSecurityID.append(SecurityID)

        if MDEntryType == 'J':
            dictName[SecurityID] = [[], []]
        elif SecurityID not in dictName:
            dictName[SecurityID] = [[], []]
            applyAction(entry, dictName, depth)
        else:
            applyAction(entry, dictName, depth)

    if snapshot['LastFragment'] == '1' and len(changeSecurityID) > 0:
        r.write(snapshot['MsgSeqNum'] + '\n')
        for SecurityID in sorted(changeSecurityID):
            for i in dictName[SecurityID][1]:
                r.write(str(i) + '\n')
            for i in dictName[SecurityID][0]:
                r.write(str(i) + '\n')
            #r.write("%s: %s\n" % (SecurityID, dictName[SecurityID][0]))
            #r.write("%s: %s\n" % (SecurityID, dictName[SecurityID][1]))

        del changeSecurityID[:]

    return True

# =================================================================================

def main():
    pattern = r"(-BOOK-)(\d+)(_)"
    #depth = int(re.findall(pattern, fastRoute))
    depth = 5
    fastRouteOut = fastRoute[0:-4] + diff_postfix
    r = open(fastRouteOut, 'w')

    snapshots = MessageReader(fastRoute)

    while True:
        snapshot = snapshots.getMessage()

        if not snapshot:
            break    # finita la comedia

        if not is_order_book_message(snapshot):
            continue

        if int(snapshot['MsgSeqNum']) > 937850:
            break

        if not incremental_book_read(snapshot, bookDict, r, depth):
            continue

    r.close()
    return True

# =================================================================================

diff_postfix = '_diff.txt'
fastRoute = '/app/fusion/tools/fast_sensor/dumpM1-11-ptest_internet/Incremental_A_239.192.70.3_40003.dump.txt'
#fastRoute = '/app/fusion/tools/fast_sensor/dumpM1-11-ptest_internet/20170207/Incremental_A_239.192.70.3_40003.txt'
#fastRoute = '/app/fusion/tools/fast_sensor/dumpM1-11-ptest_internet/FUT-BOOK-5_F_5/Incremental_B_239.195.137.3_43003.dump.txt'
#fastRoute = '/app/fusion/tools/fast_sensor/dumpM1-11-ptest_internet/FUT-BOOK-5_F_5/Snapshot_B_239.195.137.4_43004.dump.txt'


bookDict = {}

if __name__ == '__main__':
    main()