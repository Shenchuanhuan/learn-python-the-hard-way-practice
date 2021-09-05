# close --- 关闭文件（带保存）
# read ---- 读取文件内容
# readline ---读取文件中的一行
# truncate --- 清空文件
# write(stuff) ---- 将stuff写入文件

# open params
# 'r'       open for reading (default)
#    'w'       open for writing, truncating the file first
#    'x'       create a new file and open it for writing
#    'a'       open for writing, appending to the end of the file if it exists
#    'b'       binary mode
#    't'       text mode (default)
#    '+'       open a disk file for updating (reading and writing)
#    'U'       universal newline mode (deprecated)

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C(^C)")
print("If you want that, hit RETURN")

input("?")

print("Opening the file...")
# 'w' -- truncating the file if it already exist
target = open(filename, 'w')

print("Truncating the file. Goodbye")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# # OPTIMIZE:
# target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally, we close it.")
target.close()
