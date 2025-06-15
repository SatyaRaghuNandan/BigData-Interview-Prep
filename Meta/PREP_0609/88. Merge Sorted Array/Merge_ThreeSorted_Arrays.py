I am remving Duplicates here. 
result[-1] != min_val: with this statement. 

def merge_3_sorted_lists_second_variant_21(listA: List[int], 
                                           listB: List[int], 
                                           listC: List[int]) -> List[int]:
    result = []
    a, b, c = 0, 0, 0
    while a < len(listA) or b < len(listB) or c < len(listC):
        a_val = listA[a] if a < len(listA) else float('inf')
        b_val = listB[b] if b < len(listB) else float('inf')
        c_val = listC[c] if c < len(listC) else float('inf')

        min_val = min(a_val, b_val, c_val)

        if not result or result[-1] != min_val:
            result.append(min_val)

        if a_val == min_val:
            a += 1
        elif b_val == min_val:
            b += 1
        else:
            c += 1

    return result



from typing import List

def merge_3_sorted_lists_preserve_duplicates(listA: List[int], 
                                           listB: List[int], 
                                           listC: List[int]) -> List[int]:
    result = []
    a, b, c = 0, 0, 0
    while a < len(listA) or b < len(listB) or c < len(listC):
        a_val = listA[a] if a < len(listA) else float('inf')
        b_val = listB[b] if b < len(listB) else float('inf')
        c_val = listC[c] if c < len(listC) else float('inf')

        min_val = min(a_val, b_val, c_val)
        result.append(min_val)

        # Increment all pointers where the value equals min_val
        if a < len(listA) and a_val == min_val:
            a += 1
        if b < len(listB) and b_val == min_val:
            b += 1
        if c < len(listC) and c_val == min_val:
            c += 1

    return result
