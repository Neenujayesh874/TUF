class LinearSearch:

    def solution(self,arr,element):

        i=0

        is_present=False

        while (i<len(arr)):

            if arr[i]==element:

                is_present=True

                break

            i+=1

        print(is_present)


lsearch_instance=LinearSearch()

lst=[15,14,19,23,12,26,18,21,27]

element=26

lsearch_instance.solution(lst,element)