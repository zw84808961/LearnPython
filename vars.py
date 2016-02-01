# coding=utf-8
#变量赋值

counter = 100
miles = 1000.0
name = "Hugh"

print(counter)
print(miles)
print(name)

#多个变量赋值
a = b = c = 1
print("{0},{1},{2}".format(a,b,c))

a, b, c = 1,2, "Hugh"
print("{0},{1},{2}".format(a,b,c))

#Python数字
var1 = 1
var2 = 10

#使用del删除一些对象引用
#del var2
print(var1)
print(var2)

#Python字符串
'''
python的字串列表有2种取值顺序:
从左到右索引默认0开始的，最大范围是字符串长度少1
从右到左索引默认-1开始的，最大范围是字符串开头
'''
s = 'ilovepython'
print(s[1:5]) #变量[头下标:尾下标] 其中下标是从0开始算起，可以是正数或负数，下标可以为空表示取到头或尾。

str = 'Hello World!'

print str
print str[0]
print str[7]
print str[2:7]
print str[2:]
print str*2
print str + "TEST"

#Python列表
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表

#python元组
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple # 输出完整元组
print tuple[0] # 输出元组的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print tuple + tinytuple # 打印组合的元组

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000 # 元组中是非法应用
list[2] = 1000 # 列表中是合法应用

#Python元字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one'] # 输出键为'one' 的值
print dict[2] # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值
