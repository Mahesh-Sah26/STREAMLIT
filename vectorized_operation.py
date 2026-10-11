import numpy as np
cost_prices=[100,150,200,250,300]
cp_arr=np.array(cost_prices)
print(cp_arr)
print(cp_arr.shape)
print(cp_arr.dtype)

sp_arr=cp_arr+0.13*cp_arr
print(sp_arr)

profit_arr=sp_arr-cp_arr
print(profit_arr)

def price_range(cp_arr):
    if cp_arr<150:
        return "low"
    elif 150<=cp_arr<=250:
        return "medium"
    else:
        return "high"
    
price_cat_ar=np.vectorize(price_range)(cp_arr)
# check_array=price_cat_ar(cp_arr)
print(price_cat_ar)
print(np.char.upper(price_cat_ar))
print(np.char.lower(price_cat_ar))
print(np.char.title(price_cat_ar))

rev_ar=profit_arr-2
print(rev_ar)

sp_ar_rounded=np.round(sp_arr,2)
print(sp_arr)
print(sp_ar_rounded)
