def merge(a, left, mid, right):
    copy_list = []
    i, j = left, mid + 1
    ind = left
    while ind < right+1:
        if i > mid:
            copy_list.append(int(a[j]))
            j +=1
        elif j > right:
            copy_list.append(int(a[i]))
            i +=1
        elif a[j] < a[i]:
            copy_list.append(int(a[j]))
            j +=1
        else:
            copy_list.append(int(a[i]))
            i +=1
        ind +=1
    ind=0
    for x in (xrange(left,right+1)):
        a[x] = copy_list[ind]
        ind += 1

def merge_sort(alist):
   comparisons = 0
   factor = 2
   temp_mid = 0
   while 1:
      comparisons +=1
      index = 0
      left = 0
      right = len(alist) - (len(alist) % factor) - 1
      mid = (factor / 2) - 1

      while index < right:
         comparisons +=1
         temp_left = index
         temp_right = temp_left + factor -1
         mid2 = (temp_right +temp_left) / 2
         merge (alist, temp_left, mid2, temp_right)
         index = (index + factor)
      if len(alist) % factor and temp_mid !=0:
         comparisons +=1
         merge(alist, right +1, temp_mid, len(alist)-1)
         mid = right
      factor = factor * 2
      temp_mid = right
       
      if factor > len(alist) :
         comparisons +=1
         mid = right
         right = len(alist)-1
         merge(alist, 0, mid, right)
         break

   return comparisons
