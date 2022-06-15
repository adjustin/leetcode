class Solution:
    def numberToWords(self, num: int) -> str:
        dict1 = {0: "", 1:"One", 2: "Two", 3: "Three", 4: "Four", 
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        dict2 ={10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
        dict3 ={ 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 
                  7: "Seventy", 8: "Eighty", 9: "Ninety"}

        result=''
        if(num==0):
            result='Zero'
            return result
        
        billion=num//(10**9)
        num=num%(10**9)
        million=(num)//(10**6)
        num=num%(10**6)
        thousand=num//(10**3)
        rest=num%(10**3)
        
        
        def split(num):
            result=''
            while(num>=0):

                if(num//100>0):
                    result+=dict1[num//100]+' Hundred'
                    num=num%100
                    if(num):
                        result+=' '
                if(num//10>1):
                    result+=dict3[num//10]
                    num=num%10
                    if(num):
                        result+=' '
                    print(result)
                if(num//10==1):
                    result+=dict2[num]
                    return result
                else:
                    result+=dict1[num]
                    return result
                
        if billion:
            result +=split(billion)+' Billion'
        if million:
            result +=' ' if result else ''
            result += split(million) + ' Million'
        if thousand:
            result +=' ' if result else ''
            result += split(thousand) + ' Thousand'
        if rest:
            result +=' ' if result else ''
            result += split(rest)
        
        return result
                    
                