#!/usr/bin/python3
def multiple_returns(sentence):
    first = None
    if len(sentence):
        first = sentence[0]
    return (len(sentence), first)
