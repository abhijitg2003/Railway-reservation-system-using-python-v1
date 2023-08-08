import mysql.connector
pnr=1000
#enter your username and password
mydb=mysql.connector.connect(host="localhost",user="",passwd="",database="Railway")
mycursor=mydb.cursor()
def railresmenu():
                print("Railway Reservation ")
                print("1.Train Detail")
                print("2.Reservation of Ticket")
                print("3.Cancellation of Ticket")
                print("4.Display PNR status")
                print("5.Quit")
                n=int(input("Enter your choice"))
                if(n==1):
                                traindetail()
                elif(n==2):
                                reservation()
                elif(n==3):
                                cancel()
                elif(n==4):
                                displayPNR()
                elif(n==5):
                                exit(0)
                else:
                                print("Wrong choice")
                 
                
def traindetail():
                print("Train Details")
                ch='y'
                while (ch=='y'):
                                l=[]
                                train_name=input("Enter the name of train :")
                                l.append(train_name)
                                train_no=int(input("Enter train number :"))
                                l.append(train_no)
                                ac1=int(input("Enter number of AC 1 class seats"))
                                l.append(ac1)
                                ac2=int(input("Enter number of AC 2 class seats"))
                                l.append(ac2)
                                ac3=int(input("Enter number of AC 3 class seats"))
                                l.append(ac3)
                                sleeper=int(input("Enter number of sleeper class seats"))
                                l.append(sleeper)
                                train=(l)
                                sql="insert into traindetail(train_name,train_no,ac1,ac2,ac3,sleeper)values(%s,%s,%s,%s,%s,%s)"
                                mycursor.execute(sql,train)
                                mydb.commit()
                                print("Insertion completed")
                                print("Do you want to insert more train Detail: ")
                                ch=input("Enter yes/no")
                print('\n' *10)

                print("===========================================================================================")
                railresmenu()
def reservation():
                global pnr
                l1=[]
                passenger_name=input("Enter passenger name: ")
                l1.append(passenger_name)
                age=input("Enter age of passenger")
                l1.append(age)
                train_no=input("Enter train number: ")
                l1.append(train_no)
                number_of_passengers=int(input("Enter number of passanger: "))
                l1.append(number_of_passengers)
                print("Select a class you would like to travel in")
                print("1.AC FIRST CLASS")
                print("2.AC SECOND CLASS")
                print("3.AC THIRD CLASS")
                print("4.SLEEPER CLASS")
                cp=int(input("Enter your choice:"))
                if(cp==1):
                                amount=number_of_passengers*1000
                                Class='ac1'
                elif(cp==2):
                                amount=number_of_passengers*800
                                Class='ac2'
                elif(cp==3):
                                amount=number_of_passengers*500
                                Class='ac3'
                else:
                                amount=number_of_passengers*350
                                Class='sleeper'
                l1.append(Class)           
                print("Total amount to be paid:",amount)
                l1.append(amount)
                pnr=pnr+1
                print("PNR Number:",pnr)
                print("Status: confirmed")
                status='confirm'
                l1.append(status)
                l1.append(pnr)
                train1=(l1)
                sql="insert into passengers(passenger_name,age,train_no,number_of_passengers,Class,amount,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql,train1)
                mydb.commit()
                print("Insertion completed ")
                print("Go back to menu ")
                print('\n' *10)
                railresmenu()
def cancel():
                print("Ticket cancel window ")
                p=input("Enter PNR for cancellation of Ticket ")
                pn=(pnr,) 
                sql="delete from passengers where pnr=p "
                mycursor.execute(sql,pn)
                mydb.commit()
                print("Deletion completed")
                print("Go back to menu")
                print('\n' *10)

                print("===========================================================================================")
                railresmenu()
def displayPNR():
                print("PNR STATUS window ")
                pnr=input("Enter PNR NUMBER ")
                pn=(pnr,) 
                sql="select * from passengers where pnrno=%s"
                mycursor.execute(sql,pn)
                res=mycursor.fetchall() 
                print("PNR STATUS are as follows : ")
                print("(passenger_name,age,train_no, number_of_passangers,Class,amount,status, pnrno)")
                for x in res:
                                print(x)
                print("Go back to menu")
                print('\n' *10)

                print("===========================================================================================")
                railresmenu()
railresmenu() 

