import sys
import os
import json
import glob
import sqlite3


def readFile(paramFile):
    file = open(paramFile, 'rb')
    arrayOfByte = file.read()
    # print(arrayOfByte)
    return readString(arrayOfByte)


def readString(arrayOfByte):
    i = 0
    byteArray = []
    while (i < len(arrayOfByte)):
        if (len(arrayOfByte) > i + 1):
            j = ((int('0xFF', 16) & arrayOfByte[(
                i + 1)]) >> 5 | (int('0xFF', 16) & arrayOfByte[(i + 1)]) << 3)
            byteArray.append(j)
            byteArray.append(((int('0xFF', 16) & arrayOfByte[i]) >> 5 | (
                int('0xFF', 16) & arrayOfByte[i]) << 3))
        else:
            byteArray.append(((int('0xFF', 16) & arrayOfByte[i]) >> 5 | (
                int('0xFF', 16) & arrayOfByte[i]) << 3))
        i += 2
    return ''.join([chr(x & 0xFF) for x in byteArray])


connection = sqlite3.connect("bible.db")
cursor = connection.cursor()


def scrap_data(scrap_path, bible_id):
    for filename in glob.iglob(scrap_path + '**/*.yves', recursive=True):
        f = filename.replace(scrap_path, "").split("/")

        book_id = f[0]

        chapter = -1
        try:
            chapter = int(f[1].replace(".yves", ""))
        except ValueError:
            chapter = 0

        text = readFile(filename)

        cursor.execute(
            "INSERT INTO bible (bible_id, book_id, chapter, text) values(?,?,?,?)",
            (bible_id, book_id, chapter, text))
        connection.commit()


def create_db():
    cursor.execute(
        "CREATE VIRTUAL TABLE bible USING fts5(bible_id, book_id, chapter, text)")
    # "CREATE TABLE bible (bible_id INTEGER KEY, book_id TEXT, chapter INTEGER, text TEXT)")
    connection.commit()

# connection = sqlite3.connect("bible.db")
# # print(connection.total_changes)
# cursor = connection.cursor()


# rows = cursor.execute("SELECT * FROM bible").fetchall()
# print(rows)


scrap_data('/Users/tzrootm1mi/Downloads/344-4/', 344)
# scrap_data('/Users/tzrootm1mi/Desktop/3313-1/', 3313)
# scrap_data('/Users/tzrootm1mi/Desktop/3312-1/', 3312)
# create_db()
connection.close()
