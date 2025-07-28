from typing import List
import sys

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
            result = []

            for i in range(1,n+1):
                if i%3 == 0 and i%5 == 0:
                    result.append("FizzBuzz")
                elif i%3 == 0:
                    result.append("Fizz")
                elif i%5== 0:
                    result.append("Buzz")
                else:
                    result.append(str(i))
            
            return result
    
def main():
     n:int = 0
     n = int(input())

     my_answer = Solution()
     print(my_answer.fizzBuzz(n))

if __name__ == "__main__":
    main()