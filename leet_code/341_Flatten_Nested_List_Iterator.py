"""341. Flatten Nested List Iterator

https://leetcode.com/problems/flatten-nested-list-iterator/

You are given a nested list of integers nestedList.
Each element is either an integer or a list whose elements may also be integers
or other lists.
Implement an iterator to flatten it.

Implement the NestedIterator class:
- NestedIterator(List<NestedInteger> nestedList) Initializes the iterator
with the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers in the nested list
and false otherwise.

Your code will be tested with the following pseudocode:
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,4,6]. 

Constraints:
1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-10**6, 10**6].
"""

# Теги
# Рекурсия (recursion)

# Размышления
# Идейно задача лёгкая. Мы реализуем логику на для списка, а если внутри ещё список,
# то просто вызываем ту же самую логику, что и для текущего списка.
# То есть обыкновенное разбиение на рекурсию.
# Но это решение просто само по себе немного заковыристое,
# его не сразу получается реализовать.
# hasNext должен сказать есть ли ещё элементы, и обычно мы смотрим на текущий индекс
# и длину списка, но здесь может быть так, что индекс указывает на пустой
# или уже закончившийся список.
# По итогу появляется требование, что hasNext должен не просто проверять,
# но и перемещать текущий индекс дальше, к следующему действительному элементу.
# Может показаться, что это плохое медленное решение, но если задуматься,
# то оно даст амортизированное O(1), так как проход по пустым элементам будет
# произведён всего один раз, а затем индекс уже будет указывать на число.
# Далее стоит внимательно посмотреть на то, как в условии делается итерация.
# while(hasNext) гарантирует, что в next будет элемент для итерации.
# И в целом всю логику подготовки к итерации по вложенному списку можно разместить
# в проверке.
# Примечание: понятно, что мы можем разложить вложенный список в плоский.
# Опять же через рекурсию. Но это вызовет линейную экстра память.

from typing import List

class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """
       pass

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """
       pass

   def getList(self) -> ["NestedInteger"]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
       pass

class NestedIterator:

    def __init__(self, nestedList: List[NestedInteger]):
        self.index = 0
        self.nestedList = nestedList
        self.current_iterator = None
    
    def next(self) -> int:
        if self.current_iterator is not None:
            return self.current_iterator.next()
        else:
            val = self.nestedList[self.index].getInteger()
            self.index += 1
            return val   
    
    def hasNext(self) -> bool:
        while self.index < len(self.nestedList):
            val = self.nestedList[self.index]
            if val.isInteger():
                return True
            
            if self.current_iterator is None:
                self.current_iterator = NestedIterator(val.getList())

            if self.current_iterator.hasNext():
                return True
            else:
                self.current_iterator = None
                self.index += 1

        return False
