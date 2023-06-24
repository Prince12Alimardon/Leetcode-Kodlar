def selection_sort(arr):
    """
    Selection Sort (Tanlash tartibi) algoritmi.
    Berilgan ro'yxatni tartiblab yuboradi.

    Parameters:
        arr (list): Tartiblanadigan ro'yxat

    Returns:
        None
    """
    n = len(arr)  # 10
    for i in range(n):  # 1 < 10
        min_idx = i  # min_idx = 0
        for j in range(i + 1, n):  # 1 < 10
            if arr[j] < arr[min_idx]:  # 4 < 3
                print(arr[j], arr[min_idx])
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print('e=',arr[i], arr[min_idx])

    return arr


nums = [3, 4, 325, 235, 21, 5, 1235, 23, 15, 2]
print(selection_sort(nums))

#  Bu kodda selection_sort funksiyasi berilgan ro'yxatni tartiblaydi. Dastur to'g'ri ishlaganda, tartiblangan ro'yxat boshqacha bir o'zgaruvchida saqlanmaydi, to'g'ri ro'yxat o'zgartiriladi.
#
# selection_sort funksiyasiga beriladigan ro'yxatni boshqacha ro'yxat sifatida o'zgartirmaslik uchun tartiblangan ro'yxatni qaytarib bo'lish kerak bo'lsa, funksiya oxirida return operatori qo'shilishi mumkin.
#
# Kodni tushuntirish uchun funksiya nomining yonida, funksiya uchun kiruvchi argumentlarni va qaytaruvchi qiymatni to'liq tavsiflash maqsadga muvofiqdir.
