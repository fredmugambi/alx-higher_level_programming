#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    if sentence:
        return len(sentence), sentence[0]
    else:
        return None, None
