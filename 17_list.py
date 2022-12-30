lt = [1, 2, 3, 4, 5, [6, 7, 8, [11, 12, 13, 14, 15]], 10]
print(lt[2])
# we need to print 8 but how we can do that??
print(lt[5][2]) 
                        # index start from 0 
# now we need 15??
print(lt[5][3][4])
# to print the list 
print(lt[0:])
print(lt[0::3])

# to print the list in reverse order
print(lt[-1::-1])