"""
运算符
- 算术运算符
    +
    -
    *
    /
    // 整除，取证
    %
    ** 幂运算
- 赋值运算符
     =
     +=
     -=
     *=
     /=
     %=
- 位运算符
     &
     ~
     <<
     >>
     ^
- 比较运算符
    ==
    !=
    <
    >
    <=
    >=
- 逻辑运算符
    and
    or
    not
- 成员运算符
    in
    not in
- 身份运算符
    is
"""

print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5//2)
print(5%2)
print(5**2)

print(True and False) # False




print(True and True)# True
print(True or True)# True
print(True or True and False)# True
print(not True)# False

print(3 in [1,2,3])# True
print(3 not in [1,2,3])# False


a=1
b=1
print(a is b) # True
print(a is not b) # False