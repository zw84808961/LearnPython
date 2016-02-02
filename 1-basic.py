# coding=utf-8
#多行语句

total = 'item_one' + ' '\
		'item_two' + ' '\
		'item_three'
print(total)
#语句中包含[], {} 或 () 括号就不需要使用多行连接符	
days = ['Monday','Tuesday','Wednesday',
		'Thursday','Friday']


# Python 接收单引号(' )，双引号(" )，三引号(''' """) 来表示字符串
word = 'word'
sentence = "这是一个句子"
paragraph = """这是一个段落
第二行"""

print(word)
print(sentence)
print(paragraph)


#python注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
#等待用户输入
aaa = raw_input("\n\nPress the enter key to exit.")
print aaa


#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'foo'; sys.stdout.write(x + '\n')
