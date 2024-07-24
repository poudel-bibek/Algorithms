"""
Algorithm: Insetion Sort
Sorts by one comparision at a time, the idea is to "insert" each item in its rightful place. 
Placement can be performed in-place, allowing for a low space complexity.

Time Complexity: O(n^2)
Space Complexity: O(n)

Advantages: 
- Easy to understand (simple)

Disadvantages: 
- Inefficient

# Test cases: 
1. [5, 2, 2, 3, 1, 0]
2. [-1, -20, 0, 0, 100, 5, -2562, 122, 3, 1, 990, 0]

"""

def insertion_sort(input_array):
    """
    Sorting in ascending order i.e. placing all smaller values to the left.
    """
    total = len(input_array)
    for i in range(total): # Considered item
        print(f"\nConsidered: {input_array[i]}")
        # Since we only actually need to check the upper triangular items in the pairwise comparision matrix. Because of the equivalence of comparisions. 
        for j in range(i, total): # Current item
            print(f"\tCurrent: {input_array[j]}")
            # If the considered item is smaller then the current item, then skip i.e., we are not going to insert it in current item's place  
            if input_array[i] < input_array[j]: # Change the arrow to make descending
                print("\tSkipped")
                continue 
               
            else: 
                
                # If the considered item is greater than the current item, then this place actually belongs to the considered item.
                # i.e., perform the in-place swap with a temp (constant additional space complexity)
                temp = input_array[i]
                input_array[i] = input_array[j]
                input_array[j] = temp
                print("\tSwapped")

            print(input_array,"\n")
                
    return input_array

def main():
    input_array = [5, 2, 2, 3, 1, 0]
    print(insertion_sort(input_array))

if __name__ == "__main__":
    main()