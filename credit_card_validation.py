# A module for credit card validation
#-----------------------------------------
def checksum(card_number):
    '''
    This function calculates checksum of the card number
    input : string i.e card number
    return : integer i.e checksum value
    '''
    
    digits = list(map(int,card_number))
    
    odd_digits = digits[-1::-2]
    odd_digits_sum = sum(odd_digits)
    
    even_digits = digits[-2::-2]
    # According to luhn's algorithm, even sum must be sum of 2*even numbers reduced to single digit by adding double digit numbers 
    even_digits_sum = sum(list(map(lambda x: sum(divmod(2 * x, 10)), even_digits)))
    
    final_sum = odd_digits_sum + even_digits_sum
    
    return final_sum


def is_valid(card_number):
    '''
    This function performs validation of the card number
    input : string i.e card number
    return : boolean i.e True or False
    '''
    
    card_number = card_number.replace(" ","")
    
    if card_number.isnumeric() != True:  # to check if there are only numbers
        return False
    
    final_sum = checksum(card_number)
    
    return (final_sum % 10) == 0


def get_brand(card_number, cvv):
    '''
    This functions gives the brand/type of the card based on card number and cvv
    input : strings i.e card number and cvv
    return : string i.e the brand or type of card
    '''
    
    if not is_valid(card_number):
        return "Invalid card number"
    
    card_number = card_number.replace(" ","")
    
    cvv = cvv.replace(" ","")
    
    if cvv.isnumeric() != True:
        return "Invalid cvv!"
    
    brands = ["Visa", "Mastercard", "American Express" ,"Discover", "Diners Club Carte Blanche"]
    
    # rules applied according to brand specifications:
    # Visa cards – Begin with a 4 and have 13 or 16 digits
    # Mastercard cards – Begin with a 5 and has 16 digits#
    # American Express cards – Begin with a 3, followed by a 4 or a 7  has 15 digits
    # Discover cards – Begin with a 6 and have 16 digits#
    # Diners Club and Carte Blanche cards – Begin with a 3, followed by a 0, 6, or 8 and have 14 digits
    # CVV codes are a 3-digit number for Visa, Mastercard, and Discover cards, and a 4-digit number for Amex.
    
    if len(cvv) == 3:
    
        if len(card_number)==16:
            if(card_number.startswith("4")):
                return "This is a {} card".format(brands[0])
            elif(card_number.startswith("5")):
                return "This is a {} card".format(brands[1])
            elif(card_number.startswith("6")):
                return "This is a {} card".format(brands[3])
            
        elif (len(card_number)==13) and (card_number.startswith("4")):
            return "This is a {} card".format(brands[0])
        
        elif (len(card_number)==14)and(card_number.startswith("30") or card_number.startswith("36") or card_number.startswith("38") ):    
                return "This is a {} card".format(brands[4])
            
    elif (len(cvv) == 4) and (len(card_number)==15) and (card_number.startswith("34") or card_number.startswith("37")):
            return "This is a {} card".format(brands[2])
        
    return "Unknown card brand"

