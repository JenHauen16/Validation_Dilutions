These are simple scripts for diluting high concentrations of DNA and calculating the % difference from the mean to validate new DNA isolation kits. The dilutions of DNA are from >180 ng/uL to 50 ng\uL with the oshigh function and >560 ng\uL to 80 ng\uL with the cshigh function. The isolation kit validation script finds the difference from the mean between the old kit DNA quantification and the new kit DNA quantification. In my lab, we use a 25% cut-off.

Directions for diluting DNA concentration script:

1) Open Python Shell
2) Type import dils
3) Type dils.oshigh(quant > 180 nq/uL) or dils.cshigh(quant > 560 ng/uL)

Directions for isolation validation "% difference from the mean" calculation script:

1) Open Python Shell
2) Type import val
3) Type val.validation(old quant, new quant)