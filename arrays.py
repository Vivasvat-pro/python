import array as arr
array_num = arr.array('i',[1,3,5,3,7,9,3])
print("original array:"+str(array_num))
print("number of occurences of number 3 in the siad array:"+str(array_num.count(3)))
array_num.reverse()
print("the reverse order od irmes:")
print(str(array_num))