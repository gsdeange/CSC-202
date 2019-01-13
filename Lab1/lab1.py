def max_list_iter(tlist):  # must use iteration not recursion
   """ finds the max of a list of numbers and returns it, not the index"""
   if(len(tlist) < 1):
      raise ValueError
   elif(len(tlist) == 1):
      return tlist[0]
   else:
      max = tlist[0]
      for i in range(len(tlist)-1):
         if(tlist[i] < tlist[i+1]):
            max = tlist[i+1]
      return max

def reverse_rec(tempstr):   #must use recursion
   """ recursively reverses the characters in a string"""
   if((len(tempstr)) <= 1):
      return tempstr
   else:
      return reverse_rec(tempstr[1:]) + tempstr[0]


def bin_search(target, low, high, list_val, index=0):  #must use recursion
   """ searches for target in list_val[low..high] and returns index if found"""

   if(len(list_val) < 1):
      raise ValueError
   elif(list_val[low:high][0] == target):
      return index
   else:
      return bin_search(target, low+1, high, list_val, index+1) 

def reverse(tlist):
   length = len(tlist)
   if(length <= 1):
      return tlist
   return reverse(tlist[1:]) + tlist[0]
   
   
print(reverse('abcd'))