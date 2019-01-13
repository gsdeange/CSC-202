def perm_gen_lex(a): 
   """
   This function is designed to return all possible permutations of a string passed in.
   It takes in the input a and then loops through all possible permutations.
   It will return a list with all of the strings of the permutations. """

   #string will always intake in alphabetical order
   # raise exception if string has no length
   if(len(a) <= 1):
      return [a]
   else:
      #create the return list
      permlist = []
      # loop through the whole string
      for i in range(len(a)):
         #store the lead character
         lead = a[i]
         #loop through the characters left in the string
         for x in (perm_gen_lex(a.replace(a[i], ''))):
            #add possible permutations to the return list
            perm = lead+x
            permlist.append(perm)
   #return the list
   return permlist

   



 