def practicing_function_scope():
    im_trapped_in_the_function = "You can't access me outside this function!"

    print(im_trapped_in_the_function)

    # Example 2
change_the_world = "change yourself"

def change_yourself():
    change_the_world = "world changed"
    
    change_yourself()
    print(change_the_world)