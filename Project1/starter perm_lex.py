def perm_gen_lex(a): 
   #string will always intake in alphabetical order
   # raise exception if string has no length
   if(len(a) <= 1):
      return a
   else:
      permlist = []
      for i in range(len(a)):
         combo = a[i] + perm_gen_lex(a[i+1])
         permlist.append(combo)
   return permlist

   



 