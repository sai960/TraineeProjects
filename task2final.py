def Email(list):
    dic={}
    for i in list:
        list1=i.split('@')
        domain=list1[1]
        ename=list1[0]
        if(domain in dic):
            dic[domain].append(ename)
        else:
            dic[domain]=[]
            dic[domain].append(ename)
    return dic
    dic={}
    lst=data.keys()
    for i in list:
        dic[i]=len( TotalEmployees(data,i))    
    return dic
list=['sunil@dhruvsoft.co.in','venky@dhruvsoft.in','sai@dhruvsoft.com','roshini@google.com','ajay@google.com']
data=Email(list)
i=0
for domain in data:
    print("The number of employees in the domain -",domain)
    for emp in data[domain]:
        i+=1
    print(i)
    i=0
print(data)
