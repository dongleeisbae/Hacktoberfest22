class Solution:
  def happynoheh(self, n: int) -> bool:
    def squaredSum(n: int) -> bool:
      summ = 0
      while n:
        summ += pow(n % 10, 2)
        n //= 10
      return summ

    slow = squaredSum(n)
    fast = squaredSum(squaredSum(n))

    while slow != fast:
      slow = squaredSum(slow)
      fast = squaredSum(squaredSum(fast))

    return slow == 1
