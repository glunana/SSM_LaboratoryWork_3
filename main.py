# Варіант 7 з ІА-32
# U = {1, 2, 3, 4, 5, 6, 7, 8}
#A = {2, 3, 5, 7, 1}
#B = {2, 6, 7, 5, 3, 4}
print("Елементи в множиннах повинні бути вказані через кому та пробілом після неї.")
U = list(input('Множина U: ').split(", "))
A = list(input('Множина А: ').split(", "))
B = list(input('Множина B: ').split(", "))

# Завдання 1
def union(A, B):
    AuB = []
    for i in A:
        if i not in AuB:
            AuB.append(i)
    for i in B:
        if i not in AuB:
            AuB.append(i)
    AuB_sorted = sorted(AuB)
    return AuB_sorted
print("А U В: ", union(A, B))

def intersection(A, B):
    AintB = []
    for i in A:
      if i in B:
        AintB.append(i)
    AintB_sorted = sorted(AintB)
    return AintB_sorted
print("A ∩ B: ", intersection(A, B))

def difference (A, B):
    AdB = []
    for i in A:
        if i not in B:
            AdB.append(i)
    AdB_sorted = sorted(AdB)
    return AdB_sorted
print("A/B: ", difference(A, B))

def supplement (U, A):
    UsA = []
    for i in U:
        if i not in A:
            UsA.append(i)
    UsA_sorted = sorted(UsA)
    return UsA_sorted
print("U/A: ", supplement(U, A))

def symmetricalDifference (A, B):
    AsB = []
    for i in A:
        if i not in B:
            AsB.append(i)
    for i in B:
        if i not in A:
            AsB.append(i)
    AsB_sorted = sorted(AsB)
    return AsB_sorted
print("АΔВ: ", symmetricalDifference(A, B))

def cartesianProduct (A, B):
    AmB = []
    for i in A:
        for j in B:
            AmB.append((i, j))
    AmB_sorted = sorted(AmB)
    return AmB_sorted
print("A×B: ", cartesianProduct(A, B))

# Завдання 2

def subset (A, B):
    for i in A:
        if i not in B:
            return False
    return True
print("A⊂B: ", subset(A, B))

def equality (A, B):
    for i in A:
        if i not in B:
            return False
    for i in B:
        if i not in A:
            return False
    return True
print("A=B:", equality(A,B))

# Завдання 3

def bitStringA (A, U):
    Abit = []
    for i in U:
        if i in A:
            i = 1
        else:
            i = 0
        Abit.append(i)
    return Abit

def bitStringB (B, U):
    Bbit = []
    for i in U:
        if i in B:
            i = 1
        else:
            i = 0
        Bbit.append(i)
    return Bbit

print("Бітовий рядок А: ", bitStringA(A, U))
print("Бітовий рядок В: ", bitStringB(B, U))

# Завдання 4

def unionB (bitStringA, bitStringB):
    AuB = [bit1 | bit2 for bit1, bit2 in zip(bitStringA, bitStringB)]
    return AuB
bitStringA_result = bitStringA(A, U)
bitStringB_result = bitStringB(B, U)
result = unionB(bitStringA_result, bitStringB_result)
print("Бітове А U В: ", result)

def intersectionB (bitStringA, bitStringB):
    resultBitString = [bit1 & bit2 for bit1, bit2 in zip(bitStringA, bitStringB)]
    return resultBitString
bitStringA_result = bitStringA(A, U)
bitStringB_result = bitStringB(B, U)
result = intersectionB(bitStringA_result, bitStringB_result)
print("Бітове A ∩ B: ", result)

def differenceB (bitStringA, bitStringB):
    resultBitString = [bit1 & ~bit2 for bit1, bit2 in zip(bitStringA, bitStringB)]
    return resultBitString
bitStringA_result = bitStringA(A, U)
bitStringB_result = bitStringB(B, U)
result = differenceB(bitStringA_result, bitStringB_result)
print("Бітова A/B: ", result)

def symmetricalDifferenceB(bitStringA, bitStringB):
    resultBitString = [bit1 ^ bit2 for bit1, bit2 in zip(bitStringA, bitStringB)]
    return resultBitString
bitStringA_result = bitStringA(A, U)
bitStringB_result = bitStringB(B, U)
result = symmetricalDifferenceB(bitStringA_result, bitStringB_result)
print("Бітова АΔВ: ", result)

# з бів у ч. ; порівняння
def bitStringToList(bitString, U):
    return [U[i] for i in range(len(U)) if bitString[i] == 1]

def setToList(input_set):
    return list(input_set)

bitStringA_result = bitStringA(A, U)
bitStringB_result = bitStringB(B, U)

def unionB (bitStringA, bitStringB):
    AuB = [bit1 | bit2 for bit1, bit2 in zip(bitStringA, bitStringB)]
    return AuB

result = unionB(bitStringA_result, bitStringB_result)
list_union_result = bitStringToList(result, U)
print("Множина А U В:", list_union_result)

def intersectionB (bitStringA, bitStringB):
    resultBitString = [bit1 & bit2 for bit1, bit2 in zip(bitStringA, bitStringB)]
    return resultBitString

result = intersectionB(bitStringA_result, bitStringB_result)
list_intersection_result = bitStringToList(result, U)
print("Множина A ∩ B:", list_intersection_result)

def differenceB (bitStringA, bitStringB):
    resultBitString = [bit1 & ~bit2 for bit1, bit2 in zip(bitStringA, bitStringB)]
    return resultBitString

result = differenceB(bitStringA_result, bitStringB_result)
list_difference_result = bitStringToList(result, U)
print("Множина A/B:", list_difference_result)

def symmetricalDifferenceB(bitStringA, bitStringB):
    resultBitString = [bit1 ^ bit2 for bit1, bit2 in zip(bitStringA, bitStringB)]
    return resultBitString

result = symmetricalDifferenceB(bitStringA_result, bitStringB_result)
list_symmetric_difference_result = bitStringToList(result, U)
print("Множина АΔВ:", list_symmetric_difference_result)

print("Множини А U В співпадають: ", list_union_result == union(A, B))
print("Множини A ∩ B співпадають: ", list_intersection_result == intersection(A, B))
print("Множини A/B співпадають: ", list_difference_result == difference(A, B))
print("Множини АΔВ співпадають: ", list_symmetric_difference_result == symmetricalDifference(A, B))









