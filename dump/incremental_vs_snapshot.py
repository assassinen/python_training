__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#апдейт

import os
import sys

sys.path.append(os.path.join(sys.path[0], '../lib'))
from fastMessageReaderOriginal import MessageReader



def is_order_book_message(message):
    messageType = message['MessageType']
    return (messageType == 'X' or messageType == 'W')


def is_reset_MsgSeqNum(message):
    #print(message)
    messageType = message['MessageType']
    return messageType == '4'


def applyAction(entry, dictName, depth, SecurityID):
    book_level = []
    for item in snapshot_items:
        book_level.append(entry[item])
    dictName[SecurityID][int(entry['MDEntryType'])].append(book_level)


def set_snapshot_book(book_dict, entries):
    depth = 5
    SecurityID = entries['SecurityID']

    for entry in entries['entries']:

        MDEntryType = entry['MDEntryType']

        if SecurityID != '406936':
            continue

        if MDEntryType == 'J':
            book_dict[SecurityID] = [[], []]
        elif SecurityID not in book_dict:
            book_dict[SecurityID] = [[], []]
            applyAction(entry, book_dict, depth, SecurityID)
        else:
            applyAction(entry, book_dict, depth, SecurityID)


def reading_data_from_snapshot(dataset):
    book_dict = {}
    while True:
        data = dataset.getMessage()
        if not data:
            break
        if is_reset_MsgSeqNum(data) and len(book_dict) > 0:
            if i[0] < 3:
                i[0] += 1
                return book_dict
        elif not is_order_book_message(data):
            continue
        else:
            set_snapshot_book(book_dict, data)


def main():
    dataset_from_snapshot = MessageReader(to_snapshot_file_path)
    dataset_from_incremental = MessageReader(to_snapshot_file_path)
    while True:
        snapshot = reading_data_from_snapshot(dataset_from_snapshot)
        #incremental = reading_data_from_file(dataset_from_incremental)

        #if not snapshot or not incremental:
        if not snapshot:
            break

        print(snapshot)

    return True

if __name__ == '__main__':
    to_incremental_file_path = './Inc_test.txt'
    to_snapshot_file_path = './Snap_test.txt'
    i = [0]
    snapshot_items = ['MDEntryPx', 'MDEntrySize', 'MDEntryTime']

    main()