#dilution of high volume oncoscan (>180ng/uL) and cytoscan (>560 ng/uL) DNA isolates
#x must be in nanograms/uL
#import dils, dils.oshigh(quant)

def oshigh(x):
    if x > 180 and x < 400:
        dil = (x * 3)/50
        buffer = round(dil - 3)
        return '{} uL of buffer and {} uL of sample'.format(buffer, 3)
    else:
        dil2 = (x * 2)/50
        buffer2 = round(dil2 - 2)
        return '{} uL of buffer and {} uL of sample'.format(buffer2, 2)

def cshigh(x):
    if x > 560:
        csdil = (x * 2)/80
        buffercs = round(csdil - 2)
        return '{} uL of buffer and {} uL of sample'.format(buffercs, 2)
            
