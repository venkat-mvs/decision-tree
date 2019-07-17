"""
Domain : Descison Tree (or) ID3 algorithm
Completed Date : 22/2/19
made by venkat

Known bugs :
*) no support for numerical data

"""



from utils import info,info_a,distinct,select_dist,load_data_with_meta
from data import *
import pprint

def Gain(att,t_head,t_body):# finding information gain for given attribute
    c = round(info(t_head,t_body),3)
    a = round(info_a(att,t_head,t_body),3)
    return c-a

def best(t_head,t_body):# best attribute according to information gain
    dic = {}
    for i in range(len(t_head)-1):
        dic[t_head[i]] = round(Gain(t_head[i],t_head,t_body),3)
    return max(dic.items(),key=lambda x:x[1])[0]

def genrate_tree(t_head,t_body,maj="yes"):
    n = {}
    ds = distinct(t_head.index("class"),t_body)
    if len(ds["outcomes"]) == 1:
        return ds["outcomes"][0]
    if len(t_head)==0:
        return maj
    split_point = best(t_head,t_body)
    new_t_head,div = select_dist(t_head.index(split_point),t_head,t_body)
    n[split_point] = {}
    for i in div:
        if len(i) == 0:
            return maj
        n[split_point][i] = genrate_tree(new_t_head[:],div[i],maj)
    return n
def tree(file_name,meta,maj):
    for data_type in meta.values():
        if data_type == "numeric":
            raise ValueError("ID3 Algorithm does'nt allow numeric")
    tuples_head,tuples_body = load_data_with_meta(file_name,meta)
    return genrate_tree(list(tuples_head),tuples_body,maj) 
def predict(tree,data_tuple):
    '''
    tree={}
    data_tuple=((head),[body,])
    '''
    
    pass
if __name__ == "__main__":
    pprint.pprint(tree(buys_computer_file,buys_computer_meta,"yes"))
#made by venkat 
