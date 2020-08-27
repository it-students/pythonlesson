import json
'''
a = open('sample.json')
b = json.load(a)

print(b["スコア一覧"])
'''

dic =  {
            "profile1": { 
                                "first" : "Tarou" , 
                                "last" : "Tanaka"
                            } ,                
             "profile2" : {
                                 "fisrt" : "Hanako" , 
                                 "last" : "Yamada"
                                 } 
             }
            
a = open('sample2.json' , 'w')
json.dump(dic, a , indent=4)