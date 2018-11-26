# -*- coding: utf-8 -*-

'''###***定义各种符号: 字母、数字、界符、分隔符***###'''

Letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']      #字母
Numbers = ['1','2','3','4','5','6','7','8','9','0']     #数字
Delimiter = ['(',')','{','}','[',']',';']                   #界符
Operator = ['+','-','*','/','=','%','&','|','<>',':=','!=','==','>=','<=','<<','>>']                #运算符
Separator = [' ','\n','\r']
other = [':','>','<']
Separators = Separator + Delimiter + Operator  + other   #分隔符

'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''-----------------------------------------------'''

'''###***定义标识符***###'''

Identifier = ['WHILE','DO','BEGIN','END','NIL']

'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''-----------------------------------------------'''

'''###***清除注释***###'''
def Delete_comment(row):
    return row.split('//')[0]

'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''-----------------------------------------------'''

'''###***获取各个部分单词或符号***###'''
def get_word(row):
    word = ''
    answer = []
    for char in row:
        if char not in Separators:
            word += char
        else:
            if (word != ''):
                answer.append(word)  #可以对单词的判断？
                word = ''

            if char in  Delimiter + Operator  + other:
                answer.append(char)
    return answer

'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''-----------------------------------------------'''

'''###***转换进制***###'''
def binary_conversion(word):
    word = word.lower()   #处理大小写
    if(word[1]=='x'):     #16 进制转换
        word = word[2:]
        num = int(word,16)
        return num
    if(word[1]=='y'):    #24 进制转换
        word = word[2:]
        num = int(word,24)
        return str(num)
'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''-----------------------------------------------'''

'''###***获取各个部分单词或符号的属性***###'''
def get_attribute(answer):

    result = {}
    i = 0
    while i < len(answer):
        if answer[i] in Identifier:
            result[answer[i]+'_'+'%d'%i] = 'identifier'
            i +=1
            continue

        if answer[i] in Delimiter:
            result[answer[i]+'_'+'%d'%i] = 'delimiter'
            i +=1
            continue
        if answer[i] in other:
            if answer[i+1] in other+Operator:
                result[answer[i]+answer[i+1]+'_'+'%d'%i] = 'operator'
                i += 2
                continue
        if answer[i] in Operator:
            result[answer[i]+'_'+'%d'%i] = 'operator'
            i +=1
            continue

        flag = 1
        for x in answer[i]:
            if x not in Numbers:
                flag =0
        if flag == 1:
            result[answer[i]+'_'+'%d'%i] = 'num'
            i +=1
            continue

        if answer[i][0]== '0':
            result[binary_conversion(answer[i])+'_'+'%d'%i] = 'num'
            i +=1
            continue

        result[answer[i]+'_'+'%d'%i] = 'id'
        i +=1
    return result

'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''###***分析属性并输出***###'''
def asnalysis_attribute(object_dict):

    for key in object_dict:
        if(object_dict[key]=='num'):
            print('<num,'+key.split('_')[0]+'>')
        elif(object_dict[key]=='id'):
            print('<id,'+key.split('_')[0]+'>')
        elif(object_dict[key]=='operator'):
            print('<'+key.split('_')[0]+'>')
        elif(object_dict[key]=='delimiter'):
            print('<'+key.split('_')[0]+'>')
        elif(object_dict[key]=='identifier'):
            print('<'+key.split('_')[0]+'>')


'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''###***词法分析器主体函数***###'''
def lexical_analysis(row):
    
    row = Delete_comment(row)
    word_list = get_word(row)
    attribute_dict = get_attribute(word_list)
    asnalysis_attribute(attribute_dict)

'''-----------------------------------------------'''
'''-----------------------------------------------'''
'''-----------------------------------------------'''

# with open(Filenames,"r+") as file:
#     lines = file.read()
#     for i in lines:
#         for x in i :
#
#             if(x in CHR):
#                 print (x)


if __name__ == '__main__':
    row = 'WHILE (next<>NIL) DO BEGIN x:=6; Y:=xy+z END; // 这是一个注释'
    row = Delete_comment(row)
    lexical_analysis(row)
