#determining difference from the mean for validation of new DNA isolation kits
#if import val, then Call by val.validation(x, y)
#if run module, then validation(x, y)

def validation(x,y):
    mean = (x+y)/2
    diff = mean - y
    per = (abs(diff)/mean)*100
    return per


