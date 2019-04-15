from sys import argv
script, input_encoding, error = argv        #同 from sys import argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()                   #去掉字符前后的\n,\t等符号
    raw_bytes = next_lang.encode(encoding, errors=errors)            # 可选参数，设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
    cooked_string = raw_bytes.decode(encoding, errors=errors)        # https://www.cnblogs.com/wushuaishuai/p/7686290.html

    print("ENCODE", raw_bytes, "<===> DECODE", cooked_string)

languages = open("txt23.txt", encoding="utf-8")      #注意txt文件编码格式为utf-8

main(languages, input_encoding, error)


