# easy-wordlist

Helps with making English-Chinese Quizlet flashcards

## 内容列表 CONTENT

- [背景 BACKGROUND](#背景 BACKGROUND)
- [安装 INSTALL](#安装 INSTALL)
- [使用 USE](#使用 USE)


## 背景 BACKGROUND

Quizlet 建立学习集一个个查词改格式真的很麻烦。刚好在网上找到了txt版本的英汉词典(lexicon.txt)，就用上了。

It is time consuming to build Quizlet wordlists by looking every word up and then put them into the right format. I found an open-sourse English-Chinese dictionary online(lexicon.txt) so I made this program that facilitates this progress.

## 安装 INSTALL

这个项目使用 [python 3](https://www.python.org)。

This program uses [python 3](https://www.python.org).

## 使用 USE

在一个名叫wordlist.txt的文档里写上所有的词（英文），一个一行。运行程序后，调整了格式加上释义的词会导出到一个叫做quizletlist.txt的文档里。可以直接复制粘贴导入Quizlet学习集。目前只支持英语（只有英语字典）且不支持查询变型后的词。部分词有多种拼写方法的只有一种是可以查出来的。

Write all the words (in English, only one word in each line) in a document. Name the document `wordlist.txt`, place it in the folder the program is in. After running the program, the formatted words with their translations will be exported to a document named `quizletlist.txt`. You can copy and paste them directly into Quizlet when creating a list. Currently only English is supported and the program does not support conjugated words. Some of the words have multiple spellings and only one of them works.
