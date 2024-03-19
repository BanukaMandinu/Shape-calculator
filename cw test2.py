def main():
    main_menu = ('''--------------------
Shapes Calculator
--------------------
1. Calculate Surface area of a cone:
2. Calculate Volume of a cone:
3. Calculate Base are of a cone:
4. Calculate Volume of a rectangular pyramid:
5. Calculate surface Area of a rectangular pyramid:
6. Exit: \n''')
    print(main_menu)
    calculation_type = int(input("Enter Your Preferred Option: "))
    while(calculation_type>=7):
        print("Invalid input")
        calculation_type = int(input("Enter Your Preferred Option: "))
    while(calculation_type<=0):
        print("Invalid input")
        calculation_type = int(input("Enter Your Preferred Option: "))  
    if (calculation_type==1):
        radius=0
        length=0
        import math
        need_to_continue="YES"
        while(need_to_continue.upper()=="YES"):
            #Get the Radius
            radius=float(input("Insert the radius of cone: "))
            if(radius<0):
                print("Radius value can't be Negative.")
            if(radius==0):
                print("Radius value can't be zero.")
            #get the Length
            if (radius>0 and radius!=0):
                length=float(input("Insert the length of cone: "))
                if(length<0):
                    print("Length can't be Negative: ")
                if(radius==0):
                    print("Length can't be zero")
            if(radius>0 and radius!=0 and length>0 and length!=0):
                calculate_1= math.pi*radius**2+math.pi*radius*length
                print("Surface area of the cone:",calculate_1,"\n")
                need_to_continue = str(input("Do you want to calculate another area of a cone? (Yes/No): "))
                if need_to_continue.upper()=="NO":
                    restart=str(input("Do you want to Continue with another shape?(Yes/No): "))
                    if restart.upper()=="YES":
                        main()
                    if restart.upper()=="NO":
                        print("---END OF THE PROGRAM---")
    if (calculation_type==2):
        radius=0
        length=0
        import math
        need_to_continue="YES"
        while(need_to_continue.upper()=="YES"):
            #get the Radius
            radius=float(input("Insert the radius of cone: "))
            if(radius<0):
                print("Radius value can't be Negative.")
            if(radius==0):
                print("Radius value can't be zero.")
            #get the Height
            if (radius>0 and radius!=0):
                height=float(input("Insert the Height of cone: "))
                if(height<0):
                    print("Height can't be Negative: ")
                if(height==0):
                    print("Height can't be zero")
            if(radius>0 and radius!=0 and height>0 and height!=0):
                calculate_2= 1/3*math.pi*radius**2*height
                print("Surface area of the cone:",calculate_2,"\n")
                need_to_continue = str(input("Do you want to calculate another area of a cone? (Yes/No): "))
                if(need_to_continue.upper()=="NO"):
                    restart=str(input("Do you want to Continue with another shape?(Yes/No): "))
                    if (restart.upper()=="YES"):
                        main()
                    if(restart.upper()=="NO"):
                        print("---END OF THE PROGRAM---")
    if (calculation_type==3):
        radius=0
        import math
        need_to_continue="YES"
        while(need_to_continue.upper()=="YES"):
            #get the radius
            radius=float(input("Insert the radius of cone: "))
            if(radius<0):
                print("Radius value can't be Negative.")
            if(radius==0):
                print("Radius value can't be zero.")
            #get the Height
            if (radius>0 and radius!=0):
                calculate_3= math.pi*radius**2
                print("Base of cone: ",calculate_3,"\n")
                need_to_continue = str(input("Do you want to calculate another area of a cone? (Yes/No): "))
                if(need_to_continue.upper()=="NO"):
                    restart=str(input("Do you want to Continue with another shape?(Yes/No): "))
                    if (restart.upper()=="YES"):
                        main()
                    if(restart.upper()=="NO"):
                        print("---END OF THE PROGRAM---")
    if (calculation_type==4):
        a=0
        b=0
        h=0
        need_to_continue="YES"
        while(need_to_continue.upper()=="YES"):
            #one side of the rectangular pyramid(a)
            a=float(input("Insert the length of one side of base in Rectangular pyramid : "))
            if(a<0):
                print("Length can't be Negative")
            if(a==0):
                print("Length can't be zero")
            #one side of the rectangular pyramid(b)
            if(a>0 and a!=0):
                b=float(input("Insert the Length of the other side of base in Rectangular pyramid: "))
            if(b<0):
                print("Length can't be negative")
            if(b==0):
                print("Length can't be Zero")
              #height of Rectangular pyramid
            if(a>0 and a!=0 and b>0 and b!=0):
                h=float(input("Insert height of the Rectangular pyramid: "))
            if(h<0):
                print("Height can't be Negative")
            if(h==0):
                print("Height can't be Zero")
            #calculation
            if(a>0 and a!=0 and b>0 and b!=0 and h>0 and h!=0):
                calculate_4= a*b*h/3
                print("Volume of a rectangular pyramid",calculate_4,"\n")
                need_to_continue = str(input("Do you want to calculate another area of a cone? (Yes/No): "))
                if(need_to_continue.upper()=="NO"):
                    restart=str(input("Do you want to Continue with another shape?(Yes/No): "))
                    if (restart.upper()=="YES"):
                        main()
                    if(restart.upper()=="NO"):
                        print("---END OF THE PROGRAM---")
    if (calculation_type==5):
        a=0
        b=0
        h=0
        need_to_continue="YES"
        while(need_to_continue.upper()=="YES"):
              #one side of the rectangular pyramid(a)
              a=float(input("Insert the length of one side of base in Rectangular pyramid : "))
              if(a<0):
                  print("Length can't be Negative")
              if(a==0):
                  print("Length can't be zero")
              #one side of the rectangular pyramid(b)
              if(a>0 and a!=0):
                  b=float(input("Insert the Length of the other side of base in Rectangular pyramid: "))
              if(b<0):
                  print("Length can't be negative")
              if(b==0):
                  print("Length can't be Zero")
              #height of Rectangular pyramid
              if(a>0 and a!=0 and b>0 and b!=0):
                  h=float(input("Insert height of the Rectangular pyramid: "))
              if(h<0):
                  print("Height can't be Negative")
              if(h==0):
                  print("Height can't be Zero")
              #calculation
              if(a>0 and a!=0 and b>0 and b!=0 and h>0 and h!=0):
                  calculate_5= a*b+(a*((b/2)**2+h**2)**0.5)+(b*((a/2)**2+h**2)**0.5)
                  print("Area of a rectangular pyramid",calculate_,5,"\n")
                  need_to_continue = str(input("Do you want to calculate another area of a cone? (Yes/No): "))
                  if(need_to_continue.upper()=="NO"):
                    restart=str(input("Do you want to Continue with another shape?(Yes/No): "))
                    if (restart.upper()=="YES"):
                        main()
                    if(restart.upper()=="NO"):
                        print("---END OF THE PROGRAM---")
    if(calculation_type==6):
        print("\n---END OF THE PROGRAM---")
main()
        




