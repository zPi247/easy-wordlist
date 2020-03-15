import time

# 覆盖原文档
with open('quizletlist.txt', 'wt') as f_1:
    f_1.write("----- EASY QUIZLET WORD LIST -----\n")
    f_1.write("-" * 5 + time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) + "-" * 5 + "\n\n")

# find all words in wordlist.txt
list_ori = []
file_ori = open('wordlist.txt')
try:
    for i in file_ori:
        if "\n" in i:
            i = i[0:len(i)-1]
        list_ori.append(i)
finally:
    file_ori.close()

# look up
list_aft = []
list_non = []
for i_2 in list_ori:
    file_dict = open('lexicon.txt')
    try:
        found = 0
        for i_3 in file_dict:
            if i_2 in i_3:
                if i_3.find("|") != -1 and i_3.find("|") < i_3.find("["):
                    pure_word_index = i_3.find("|")
                else:
                    pure_word_index = i_3.find("[")
                pure_word = i_3[0:pure_word_index]
                if pure_word == i_2:
                    found = 1
                    meaning_index = i_3.find("]")
                    meaning = i_3[meaning_index+1:len(i_3)]
                    list_aft.append(pure_word+"\t"+meaning)
        if found == 0:
            list_non.append(i_2)
    finally:
        file_dict.close()

# write in
with open('quizletlist.txt', 'a') as f_2:
    for i_4 in list_aft:
        f_2.writelines(i_4)
    if len(list_non) > 0:
        f_2.writelines("\n❗❗❗️无法找到这些词：️\n")
        for i_5 in list_non:
            f_2.writelines(i_5+"\n")

print("\n\n---------- DONE ----------\n\n")
