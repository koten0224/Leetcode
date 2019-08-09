class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["FizzBuzz" if not i%15 else("Fizz" if not i%3 else("Buzz" if not i%5 else str(i))) for i in range(1,n+1)]