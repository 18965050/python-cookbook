# search.py
'''
Hypothetical command line tool for searching a collection of
files for one or more text patterns.
'''
import argparse
parser = argparse.ArgumentParser(description='Search some files')   #命令描述

parser.add_argument(dest='filenames',metavar='filename', nargs='*') #参数存放在dest中, metavar 参数被用来生成帮助信息

parser.add_argument('-p', '--pat',metavar='pattern', required=True,
                    dest='patterns', action='append',               # action='append'用于将多个值合并
                    help='text pattern to search for')

parser.add_argument('-v', dest='verbose', action='store_true',      # action='store_true' 用于存放Boolean值
                    help='verbose mode')

parser.add_argument('-o', dest='outfile', action='store',           # action='store' 用于存放字符串
                    help='output file')

parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='slow',        # choices表示只能取设置的值. default表示默认值
                    help='search speed')

args = parser.parse_args()

# Output the collected arguments
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)
