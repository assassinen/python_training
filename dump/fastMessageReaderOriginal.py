#!/usr/bin/python

import sys
import re

# ============================================================================  

class MessageReader:

    messageRegexp = r"s*(\w+)\[\d+\]=(.*?)(?=\s\w+\[\d+\]|$)";

    def __init__(self, fileName):
        self.fileName = fileName
        #self.file = open(fileName, encoding="utf8")
        self.file = open(fileName)

        self.carryover = "";

    def __del__(self):
        self.file.close()

    def getMessage(self):
        if (self.carryover != ""):
            line = self.carryover
            self.carryover = ""
        else:
            line = self.file.readline()

        while (line.startswith('ApplVerID') is not True):
            if not line: return {}
            line = self.file.readline()
        message = dict(re.findall(self.messageRegexp, line))
        message['entries'] = []

        line = self.file.readline();
        noEntries = re.sub(".*?NoMDEntries\[268\]\s*=\s*(\d+)[^\d]*", r'\1', line)
        if (noEntries == line):
            self.carryover = line;
            return message

        for i in range(int(noEntries)):
            line = self.file.readline().split(':')[1].strip()
            entry = dict(re.findall(self.messageRegexp, line))
            message["entries"].append(entry)

        return message

# ============================================================================
