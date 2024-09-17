#14/05/2024 team ANTIC's Ice Cream Van with dataframes
#completed 15/05/2024 and fully functional
import numpy as np
import pandas as pd
import random

"""
Learning objectives

Functions *
Exception Handling *
File Handling () missing in this instance
NumPy (*) (only small amount for n-array)
Pandas (*)


"""

ascii_art = """                                                                                                                                                      
  ,---.  ,--.  ,--.,--------.,--. ,-----.,--.                  
 /  O  \ |  ,'.|  |'--.  .--'|  |'  .--./|  |,---.             
|  .-.  ||  |' '  |   |  |   |  ||  |    `-'(  .-'             
|  | |  ||  | `   |   |  |   |  |'  '--'\   .-'  `)            
`--' `--'`--'  `--'   `--'   `--' `-----'   `----'             
,--.                                                           
|  | ,---. ,---.  ,---.,--.--. ,---.  ,--,--.,--,--,--. ,---.  
|  || .--'| .-. :| .--'|  .--'| .-. :' ,-.  ||        |(  .-'  
|  |\ `--.\   --.\ `--.|  |   \   --.\ '-'  ||  |  |  |.-'  `) 
`--' `---' `----' `---'`--'    `----' `--`--'`--`--`--'`----'                                                                                                                                                                         
"""
print(ascii_art)

####ice cream ascii_art source: https://ascii.co.uk/art/icecream
#### aside from the ice cream sandwich.
ascii_art_sundae = """                                                                                                                                                      

                 _
                //
        \,O.   //
       ,(:::)=//
      (  `~(###)
       %---'`"y
        \    /
         \  /
        __)(__  
       '------`                                                                                                                                                                      
"""
ascii_art_ice_cream = """
         _
       ,' `,.
       >-.(__)
      (_,-' |
        `.  |
          `.| 
            `
"""
ascii_art_whippy = """
       ()
      (__)
     (____)
    (______)
   (________)
  (__________)
   \/\/\/\/\/
    \/\/\/\/
     \/\/\/
      \/\/
       \/
"""
ascii_art_popcicle = """
         _.-.
       ,'/ //\.
      /// // /)
     /// // //|
    /// // ///
   /// // ///
  (`: // ///
   `;`: ///
   / /:`:/
  / /  `'
 / /
(_/  
"""
ascii_art_ice_cream_sandwich = """
          _____
         /\  \ \.
        /\/\  \ \*
       /\/\/\  \ \.
      /\/\/\/\__\_\.
     /\/\/\/\/  /_/
    /\/\/\/\/  /_/
    \/\/\/\/  /_/
     \/\/\/  /_/
      \/\/  /_/
       \/__/_/
"""
ascii_art_flake = """
       ()    /z/
      (__)  /z/
     (____)/z/
    (_____/_/
   (_____/_/)
  (__________)
   \/\/\/\/\/
    \/\/\/\/
     \/\/\/
      \/\/
       \/
"""

###import new icecream prices
#df = pd.read_csv(ice_cream_list.csv)

ice_cream_art_list = ["ascii_art_sundae", "ascii_art_popcicle",
                      "ascii_art_whippy","ascii_art_triple",
                       "ascii_art_ice_cream_sandwich", "ascii_art_flake"]

#ice cream selection and prices
ice_cream_selection = {"sundae": 2.49,
                       "popcicle":1.15,
                       "whippy": 0.99,
                       "triple": 3.50, 
                       "ice_cream_sandwich":4.10,
                       "flake":1.10,
                        }
#turned dictionary into dataframe
df_icecreams = pd.DataFrame(ice_cream_selection.items(), 
                            columns=['Ice_Creams', 'Cost_in_pound'])
###random number of ice cream in stock
df_icecreams["Stock"] = [random.randint(1, 15) for i in range(6)]

#Insert corresponding art into dataframe
df_icecreams["Art"] = ice_cream_art_list

#Ice cream van message
print("Today's Ice Cream menu: ")
print(df_icecreams[["Ice_Creams","Cost_in_pound"]])

#define function for transaction
def ice_cream_van(costumer_choice, money, number_icecream):
    ice_cream_cost = df_icecreams.loc[df_icecreams['Ice_Creams'] == costumer_choice,
                                      'Cost_in_pound'].item()
    total_cost =  (ice_cream_cost * number_icecream)
    money_left = round(money - total_cost, 2)
    if money_left < 0:
        print(f"Sorry you do not have enough cash, you are {money_left} short")
    else:
        print("Thank you for your purchase")
        return money_left

#while loops to repeat.
want_icecream = True

while want_icecream == True:   
    while True:
        costumer_choice = input("What is the ice cream you want")
        if (df_icecreams["Ice_Creams"]==costumer_choice).any() == True:
            #checks if value in index
            #costumer_choice in df_icecreams["Ice_Creams"]
            #break to exit infinite loop
            break
        else:            
            print("Choose an icecream we have available:")
            print(df_icecreams[["Ice_Creams","Cost_in_pound"]])

    while True:
        selected_ice_creams_left = df_icecreams.loc[df_icecreams \
            ["Ice_Creams"]==costumer_choice,["Stock"]].values[0].item()
        #See if input is valid        
        try:
            number_icecream = int(input("how many?"))
        #if not valid raise exception and print out and loops back with while.
        except:
            print("Choose a number of ice creams you are buying.")
                ###additional choice features later.
                #print("Would you like to buy them all or", 
                #      " select another ice cream?")

        #if input have no error
        else:
        #check for number of ice cream in stock for selected one, 
        #if enough continue    
            if df_icecreams.loc[df_icecreams["Ice_Creams"]==costumer_choice,
                                ["Stock"]].values[0].item() >= number_icecream:
                #exit loop 
                break
            else:
                print(f"Sorry, we have less than {selected_ice_creams_left} ", 
                    "of ice creams in stock.")                
                print("Please select less than number of ice creams in stock")
                
    while True:
        try:
            costumer_money = float(input("How much money do you have?"))
            break
        except ValueError:
            print("Insert a number total you are spending")
    
    try:        
        money_left = ice_cream_van(costumer_choice,
                                   costumer_money, number_icecream)
        if money_left < 0:
            print("You do not have enough money for this choice, ",
                "would you like to choose another iceream?")
        #if enough money, retrieve art string from dataframe, convert to narray
        #to singular value from narray value[first].item()    
        elif money_left >= 0:
            print_art = df_icecreams.loc[df_icecreams["Ice_Creams"] 
                                         ==costumer_choice, 
                                         ["Art"]].values[0].item()
            #print string from dataframe to call original variable, display art.
            print(globals()[print_art])
            #f-String to display values of previous choices and money left.
            print(f"thank you for your purchase, and here is your "
                  f"{number_icecream} {costumer_choice} ")
            print(f"and {money_left} pounds of change.")
            #Update ice cream van's stock in pandas array for selected condition
            df_icecreams.loc[df_icecreams["Ice_Creams"]==costumer_choice,
                                ["Stock"]]-=number_icecream            
            #ask if you want to buy another one
            ice_cream_choice = input("Type Y buy another ice cream : ")
            if ice_cream_choice != "y" and ice_cream_choice != "Y":
                want_icecream = False        
                print("Have a great time!")
                break         
    except:
        ice_cream_choice = input("Type Y to choose again : ")
        if ice_cream_choice != "y" and ice_cream_choice != "Y":
            want_icecream = False        
            print("Perhaps next time.")
            break

#####Some other thoughts on what we could do
#other stuff to develop, create numpy array to represent cities, 
#be a merchant to sell between places (different dimensions?)
#randomise prices etc.
##add random purchases?
##create a chart of how many ice creams are sold?

###purchase