def rename(ko):
    a = ko.split(' ')
    return a[1] + ' ' + a[0]
print(rename('omas naohiko'))

def f(full_name):
    f_name,l_name = full_name.split(' ')
    return l_name + ' ' + f_name
print(f('yara yuuto'))

def fa(full_name):
    w = 'iha kazuki'.index(' ')
    return full_name[w+1:] + ' ' + full_name[:w]
print(fa('iha kazuki'))