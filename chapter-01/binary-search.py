def binary_search(list, item):  #  БИНАРНЫЙ ПОИСК
    low = 0                     #  В nеременнь1х Low и high хранятся границы
    high = len(list)-1          #  той части списка, в которой выпопняется поиск

    while low <= high:
        mid = (low + high)//2   #  находим средний элемент
        guess = list[mid]       
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9] 
print (binary_search(my_list, 7))
        