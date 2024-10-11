

card_details = "4137894711755904"
#card_details = "5078720064172827"
#card_details = "4187451822793156"





mylist = [8, 6, 16, 8, 2, 14, 10, 0]
def list2string(mylist):
    total = 0
    for i in mylist:
        if i >= 10:
            strng = str(i)
            for i in strng:
                total = total + int(i)
        else:
            total = total + i
    #print("this is total: ", total)
    return total
#list2string(mylist)


def validity_test(card_details):
    odd_total = 0
    mul_list = []
    even_total = 0
    for i,j in enumerate(card_details):       
        if i % 2 == 0:           
            double = int(j)*2
            mul_list.append(double)
            #print("this is mul", mul_list)
            even_total = list2string(mul_list)
        elif i % 2 != 0:
            odd_total = odd_total + int(j)           
            #Done with this part
        else:
            print("error")
    total_total = odd_total + even_total
    #print(total_total)
    return total_total
validity_test(card_details)

#card_details_input = input("Enter Card details for Validity check: ")

def validity_print(card_details):
    total = validity_test(card_details)
    if total % 10 == 0:
        return "Card is Valid!!"
        #print("Card is Valid!!")
    elif total % 10 != 0:
        return "Card is Invalid!!"
        #print("Card is invalid!!!")

#validity_print(card_details)

####################### TEST using PYTEST #########################
