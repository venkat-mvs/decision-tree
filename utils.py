"""
Some utils developed specially for descison_tree

#made by venkat
 
"""




import math
# from data import *

def distinct(index,body):# output : {"type":"numeric"/"discrete","point"/"outcomes":[.,.,..]}
    distinct_ = {"type":"dicrete"}
    if type(body[0][index]) not in [type(1),type(1.0)]:
        distinct_["outcomes"]=[]
        for i in body:
            if i[index] not in distinct_["outcomes"]:
                distinct_["outcomes"]+= [i[index]]
    else:
        distinct_["type"] = "numeric"
        distinct_["point"] = []
        # numeric values are not still implemented


    return distinct_

def tuples_at_i(index,ls_distinct,body):#output : {"for_each_outcome":"tuples that consist outcome"}
    dic = {}
    for i in ls_distinct:
        dic[i]=[]
        for j in body:
            if j[index] == i:
                dic[i] += [j]
    return dic

def info(t_head,t_body):# based on entropy
    sum = 0
    b_len = len(t_body)
    if b_len == 0:
        return 0
    class_i = t_head.index("class")
    dic = {}
    for i,j in enumerate(t_head):
        dic[j] = distinct(i,t_body)
    tups = tuples_at_i(class_i, dic[t_head[class_i]]["outcomes"], t_body)
    for i in tups:
        temp = float(len(tups[i]))/float(b_len)
        if temp!=0:
            sum += -1*temp*math.log(temp,2)
    return sum
# print "info(D) =",info(tuples_head,tuples_body)


def info_a(att,t_head,t_body):# entropy of an attribute
    sum = 0
    b_len = len(t_body)
    if b_len == 0:
        return 0
    att_i = t_head.index(att)
    dic = {}
    for i,j in enumerate(t_head):
        dic[j] = distinct(i,t_body)
    tups = tuples_at_i(att_i,dic[t_head[att_i]]["outcomes"],t_body)
    for i in tups:
        info_d = info(t_head,tups[i])
        temp = float(len(tups[i]))/float(b_len)
        sum += temp*info_d
    return sum
#print info_a("credit_rating",tuples_head,tuples_body)

def select_dist(index,t_head,t_body):# split the tuples that are related to outcome
    #output : head_list_without_attribute_on_index,
    # {"for each outcome of attribute of given index":[tuples asscoiated with outcome]}
    new_t_body = {}
    outcomes = distinct(index,t_body)
    outcomes = outcomes["outcomes"]
    for outcome in outcomes:
        new_t_body[outcome] = []
        for i in t_body:
            if outcome==i[index]:
                temp = []
                for j,k in enumerate(i):
                    if j != index:
                        temp+=[k]
                new_t_body[outcome].append(temp)
    t_head.remove(t_head[index])

    return t_head[:],new_t_body
# print(select_dist(tuples_head.index("age"),tuples_head,tuples_body))

def _dismissquotes(line_list):
	return [i.strip('"') for i in line_list]
def load_data(file_name,headless=False,with_quote=True,sep=","):
	tuple_head,tuple_body = [],[]
	try:
		open_file = open(file_name)
	except:
		raise ValueError("No File Found")
	else:
		if not headless:
			tuple_head += open_file.readline().strip().split(sep)
			if with_quote:
				tuple_head[:] = _dismissquotes(tuple_head)
		if with_quote:
			for line in open_file.readlines():
				tuple_body += [_dismissquotes(line.strip().split(sep))]
		else:
			for line in open_file.readlines():
				if line.strip() == "":	
					continue	
				tuple_body += [line.strip().split(sep)]
		return tuple(tuple_head),tuple_body
def load_data_with_meta(file_name,meta,headless=False,with_quote=True,sep=","):
	tuple_head,tuple_body = load_data(file_name,headless,with_quote,sep)# load data 
	for attrib in meta:
		if meta[attrib] == "numeric":
			index = tuple_head.index(attrib)
			row = 0
			while row!=len(tuple_body):
				if '.' in tuple_body[row][index]:
					tuple_body[row][index] = float(tuple_body[row][index])
				else:
					tuple_body[row][index] = int(tuple_body[row][index])
				row += 1
	return tuple_head,tuple_body

#made by venkat 
