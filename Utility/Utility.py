# -*- coding: utf-8 -*- 

def encode(text):
    return str(text)

def getWithOutBaseUrlEventNumber(baseUrl,fullUrl):
    return fullUrl[len(baseUrl):]

