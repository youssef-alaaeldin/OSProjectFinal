def fifo():
    count_page_faults = 0

    no_of_frames = int(input("Enter number of frames: "))
    frame = [-1 for i in range(no_of_frames)]
    no_of_pages = int(input("Enter number of pages: "))
    ref_string = list(map(str, input("Enter reference string: ").split()))

    j = 0

    for i in range(0, no_of_pages):
        free = 0
        for k in range(0, no_of_frames):
            if frame[k] == ref_string[i]:
                free = 1

        if free == 0:
            frame[j] = ref_string[i]
            j = (j + 1) % no_of_frames
            count_page_faults = count_page_faults + 1

    print("String after")
    for n in range(0, no_of_frames):
        print(frame[n])

    print("Page faults = " + str(count_page_faults))
    
    
    
    # main
if __name__ == "__main__":
    case = "Y"
    while case == 'Y' or case == 'y':

        c = str(input("Enter 'f' for FIFO , 'l' for LRU, and 'o' for optimal: "))
        if c == 'f' or c == 'F':
            fifo()
            
         case = str(input("Would you like another algorithm ? type 'Y'... and 'N' to End: "))
