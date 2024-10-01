#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_length):
        try:
            # Check if we are out of range for either list
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                new_list.append(0)
            else:
                # Check if both elements are either int or float
                if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                    print("wrong type")
                    new_list.append(0)
                else:
                    # Perform the division
                    new_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except Exception:
            new_list.append(0)
        finally:
            continue  # Continue to the next iteration

    return new_list
