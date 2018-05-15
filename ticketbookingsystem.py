class TicketBooking:

    def __init__(self,title,tickets,evening,night):
        self.title=title
        self.tickets=tickets
        self.balance_tickets = tickets
        self.ticks=tickets
        self.evening=evening
        if (evening == 1):
            self.balance_tickets_evening = tickets
        else:
            self.balance_tickets_evening =0
        self.night=night
        if (night == 1):
            self.balance_tickets_night = tickets
        else:
            self.balance_tickets_night=0


        
    def book_tickets_evening(self,ticket_number):
        self.balance_tickets_evening-=ticket_number
        message="\n\n\n\t\ttickets for the show {} has been booked \nThe numbers are {}".format(self.title,ticket_number)
        return message

    
    def book_tickets_night(self,ticket_number):
        self.balance_tickets_night-=ticket_number
        message="\n\n\n\t\ttickets for the show {} has been booked \nThe numbers are {}".format(self.title,ticket_number)
        return message



    def print_show(self):
        message="\n\nTitle = {} \ntotal number of tickets = {} \nbalance tickets are = {} for evening \nbalance tickets are = {} for night ".format(self.title,self.tickets,self.balance_tickets_evening,self.balance_tickets_night)
        return message

    
    def print_title(self):
        return self.title

    
    def check_balance_evening(self,number):
        if (number <= self.balance_tickets_evening):
            print(self.book_tickets_evening(number),"for evening show")
        else:
            print("There are not enough tickets ...Please try again with lesser number of tickets")

            
    def check_balance_night(self,number):
        if (number <= self.balance_tickets_night):
            print(self.book_tickets_night(number),"for night show")
        else:
            print("There are not enough tickets ...Please try again with lesser number of tickets")

            
    def check_for_timing(self):
        if self.evening==1 and self.night==1:
            timing =" The timing available are \n\t1. Evening\n\t2. Night"
            return timing
        elif self.evening==1 and self.night==0:
            timing =" The timing available are \n\t1. Evening"
            return timing
        elif self.evening==0 and self.night==1:
            timing =" The timing available are \n\t1. Night"
            return timing           
            

show=[TicketBooking("102 Not Out",int(60),1,0),TicketBooking("Hellsing",int(70),0,1),TicketBooking("Avengers Infinty War",int(50),1,1)]



flag = 0
while flag ==0:
    choice=int(input("\n\n\nMenu \n\t1.Add a new show\n\n\t2.Book ticket for a show\n\n\t3.Delete a show\n\n\t4.Booked tickets\n\n\t5.Exit\n\nEnter your choice : "))



    #to add a new show
    if choice==1:
        temp_title=str(input("\n\n\n enter the title : "))       
        temp_ticket=int(input("\nenter the number of tickets per show : "))       
        eve=int(input("Is there a evening show??(1) for yes (0)for no : "))
        night=int(input("Is there a night show??(1) for yes (0)for no : "))
        show.append(TicketBooking(temp_title,temp_ticket,eve,night))





    #to book a ticket
    elif choice==2:
        print("The availabe shows are \n")
        
        for i in range(0,len(show)):
            print("\n{}. {}".format(i+1,show[i].print_title()))
            
        choice_for_show=int(input("\n\tEnter your choice : "))
        print(show[choice_for_show-1].check_for_timing())
        choice_for_timing=int(input("\n\tEnter your choice : "))
        tickets=int(input("Enter the number of tickets : "))
        
        if (choice_for_timing==1 and show[choice_for_show-1].evening==1):
            show[choice_for_show-1].check_balance_evening(tickets)
            
        elif (choice_for_timing==1 and show[choice_for_show-1].night==1):
            show[choice_for_show-1].check_balance_night(tickets)
            
        if (choice_for_timing==2 and show[choice_for_show-1].night==1):
            show[choice_for_show-1].check_balance_night(tickets)




    #to delete a show
    elif choice==3:
        print("The shows availabe are ")
        for i in range(0,len(show)):
            print("\n{}. {}".format(i+1,show[i].print_title()))
            
        delete_movie=int(input("enter the movie number you want to delete : "))
        delete_choice=str(input("Are you sure(y/n)"))
        
        if delete_choice=='y':
            temp=show[delete_movie-1].title
            del show[delete_movie-1]
            print("deleted..........{}".format(temp))
            
        elif delete_choice=="n" :
            continue




    #to print the shows avilabe
    elif choice==4:
        for i in range(0,len(show)):
            print("\n{}. {}".format(i+1,show[i].print_show()))
    
            
     # to exit       
    elif choice==5:
        
        exit_choice=str(input("Are you sure you want to exit(y/n) : "))
        
        if exit_choice=="y":
            print("exiting.......")
            flag=1
            
        elif exit_choice=="n": continue



    else:
        print("please check your input")
    
    
