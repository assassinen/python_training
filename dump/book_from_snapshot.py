__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import re
import copy

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
    return (messageType == 'B' or messageType == 'X' or messageType == 'W' or messageType == 'd')


def applyAction(entry, dictName, depth, SecurityID):
    #print(entry)
    book_level = []
    for item in snapshot_items:
        book_level.append(entry[item])
    dictName[SecurityID][int(entry['MDEntryType'])].append(book_level)


def incremental_book_read(snapshot, dictName, r, depth):

    #print(snapshot)
    SecurityID = snapshot['SecurityID']

    for entry in snapshot['entries']:

        if SecurityID != '414301':
            continue

        if SecurityID not in changeSecurityID:
            changeSecurityID.append(SecurityID)

        if SecurityID not in dictName:
            dictName[SecurityID] = [[], []]
            applyAction(entry, dictName, depth, SecurityID)
        else:
            applyAction(entry, dictName, depth, SecurityID)

    if snapshot['LastFragment'] == '1' and len(changeSecurityID) > 0:
        for SecurityID in sorted(changeSecurityID):
            if SecurityID not in book_dict_back:
                book_dict_back[SecurityID] = [[], []]
            elif dictName[SecurityID] != book_dict_back[SecurityID]:
                print_level(snapshot['LastMsgSeqNumProcessed'], SecurityID, dictName, r)
                book_dict_back[SecurityID] = copy.deepcopy(dictName[SecurityID])
            dictName.clear()

        del changeSecurityID[:]

    return True


def print_level(MsgSeqNum, SecurityID, dictName, r):
    r.write(MsgSeqNum + '\n')
    for i in dictName[SecurityID][1]:
        r.write(str(i) + '\n')
    for i in dictName[SecurityID][0]:
        r.write(str(i) + '\n')


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
        #print (snapshot)

        if not snapshot:
            break    # finita la comedia

        if not is_order_book_message(snapshot):
            continue

        if int(snapshot['LastMsgSeqNumProcessed']) > 931:
            break

        if not incremental_book_read(snapshot, book_dict, r, depth):
            continue

    r.close()
    return True

# =================================================================================
diff_postfix = '_diff.txt'
snapshot_items = ['MDEntryPx', 'MDEntrySize', 'MDEntryTime']
# snapshot_items = ['MDEntryType',
#                  'ExchangeTradingSessionID',
#                  'MarketDepth',
#                  'MDEntryPx',
#                  #'MDEntryDate',
#                  'MDEntryTime',
#                  'MDEntrySize',
#                  'MDPriceLevel']
changeSecurityID = []
fastRoute = '/app/fusion/tools/fast_sensor/dumpM1-11-ptest_internet/Snapshot_A_239.192.70.4_40004.dump.txt'
book_dict = {}
book_dict_back = {}

if __name__ == '__main__':
    main()