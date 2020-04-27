# Exercise 5.12 Identical twins

In the exercise base you can find the `Person` class that is linked with an `SimpleDate` object. Add to the class Person the method `def __eq__(self,compared)`, which can be used to compare the similarity of people. The comparison should take into account the equality of all the variables of a person (birthday included).

There are no tests in the exercise template to check the correctness of the solution. Only return your answer after the comparison works as it should. Below is some code to help test the program.

```java
date = SimpleDate(24, 3, 2017)
date2 = SimpleDate(23, 7, 2017)

leo = Person("Leo", date, 62, 9)
lily = Person("Lily", date2, 65, 8)

if (leo == lily):
    print("Is this quite correct?")

leo_with_different_weight = Person("Leo", date, 62, 10)

if (leo == leo_with_different_weight):
    print("Is this quite correct?")
```
