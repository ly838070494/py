#from f_product import product
#s = product(3, 4, 5, 6)
#print(s)

#from f_hannuota import move
#move(10, 'X', 'Y', 'Z')

#find_min_and_max
#from f_findminmax import min_and_max
#if min_and_max([]) != (None, None):
#    print('测试失败')
#elif min_and_max([7]) != (7, 7):
#    print('测试失败')
#elif min_and_max([7, 1]) != (1, 7):
#    print('测试失败')
#elif min_and_max([1, 3, 5, 7, 9]) != (1, 9):
#    print('测试失败')
#else:
#    print('测试成功')
#
#from f_yanghui import yanghui
#n = 0
#result = []
#for t in yanghui():
#    print(t)
#    result.insert(len(result), t)
#    n = n + 1
#    if n == 10:
#        break
#
#print(result)
#if result == [
#        [1],
#        [1, 1],
#        [1, 2, 1],
#        [1, 3, 3, 1],
#        [1, 4, 6, 4, 1],
#        [1, 5, 10, 10, 5, 1],
#        [1, 6, 15, 20, 15, 6, 1],
#        [1, 7, 21, 35, 35, 21, 7, 1],
#        [1, 8, 28, 56, 70, 56, 28, 8, 1],
#        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
#    ]:
#    print('测试通过')
#else:
#    print('测试失败')
#print(result)
from f_count import createCounter
countA = createCounter()
list = [countA(), countA(), countA(), countA()]
print(list)
countB= createCounter()
list2 = [countB(), countB(), countB(), countB()]
print(list2)
