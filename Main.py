from tkinter import *
import random
import string
from twilio.rest import Client 

def generate():
    
    win = Tk()
    win.geometry('2000x1000')
    def onClick():
        # praj start
        def send_sms():
            account_sid = side.get()
            auth_token = toke.get()
            twilio_phone = t_phe.get()
            recipient_phone = phe.get()
            if account_sid and auth_token and twilio_phone and recipient_phone :
                client = Client(account_sid, auth_token)
                disptext=""
                try:
                    message = client.messages.create(
                        body=f"Your randomly generated password is: {shuffled_password}",
                        from_=twilio_phone,
                        to=recipient_phone
                    )
                    disptext="Password sent successfully!"
                except Exception as e:
                    disptext=f"Failed to send password. Error: {e}"
                dispLabel=Label(win, text=disptext)
                dispLabel.place(x=1000, y=600)
                win.after(5000, dispLabel.destroy)
        # praj end
        
        
        
        user_input = (inp.get())    
        if user_input:  
            user_input=int(user_input)  
            if(user_input>=8):
                #praj start
                capital_letter = random.choice(string.ascii_uppercase)
                small_letter = random.choice(string.ascii_lowercase)
                digit = random.choice(string.digits)
                special_char = random.choice("!@#$%^&*()-=_+")
                remaining_length = user_input - 4
                other_characters = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()-=_+") for _ in range(remaining_length))
                password = capital_letter + small_letter + digit + special_char + other_characters
                password_list = list(password)
                random.shuffle(password_list)
                shuffled_password = ''.join(password_list)
                # praj end
                ww=Text(win, height=2, borderwidth=0)
                ww.insert(1.0,shuffled_password)
                ww.place(x=500, y=200)
                Label(win,text="Enter your Twilio account SID:", font=('Arial,18')).place(x=50, y=400)
                side=Entry(win)
                side.place(x=400,y=405)
                Label(win,text="Enter your Twilio auth token:", font=('Arial,18')).place(x=750, y=400)
                toke=Entry(win)
                toke.place(x=1200, y=405)
                Label(win, text="Enter your Twilio phone number:", font=('Arial,18')).place(x=50, y=500)
                t_phe=Entry(win)
                t_phe.place(x=400, y=505)
                Label(win, text="Enter your phone number to receive the password: ", font=('Arial,18')).place(x=750, y=500)
                phe=Entry(win)
                phe.place(x=1200, y=505)
                Button(win,text="Send password as sms", command=send_sms).place(x=50, y=550)
                
            





    spacel=Label(win,text='',font=('Arial, 60')).grid()
    n = Label(win, text='Length of password required:',font=('Arial, 30'),fg='BLack',bg='Yellow').place(x=100, y=100)
    inp = Entry(win,width=50,font=('Arial,30'))
    inp.place(x=650, y=115)
    cl = Button(win, text='Generate', command=onClick,font=('Arial', 18))
    cl.grid(padx=100, pady=100)
        



def stren():
    win = Tk()
    win.geometry('600x500')
    Label(win, text='Enter the password:', font = ('Arial',20)).place(x=50, y=50)
    inp = Entry(win)
    inp.place(x=300,y=60)
    rating=Label(win,text='')
    rating.place(x=100,y=200)

    def clickstrength():
        s = inp.get()  
        # abbas start      
        upper_case = any([1 if c in string.ascii_uppercase else 0 for c in s])
        lower_case = any([1 if c in string.ascii_uppercase else 0 for c in s])
        special = any([1 if c in string.punctuation else 0 for c in s])
        digits = any([1 if c in string.digits else 0 for c in s])

        characters = [upper_case, lower_case, special, digits]
        length = len(s)
        score = 0
        if length > 8:
            score += 1
        if length > 12:
            score += 1
        if length > 17:
            score += 1
        if length > 20:
            score += 1

        dispScore=f'Password length is {str(length)},adding {str(score)} points!\n'     
        if sum(characters) > 1:
            score += 1
        if sum(characters) > 2:
            score += 1
        if sum(characters) > 3:
            score += 1
        dispScore+=f'Password has {str(sum(characters))} different character types,adding {str(sum(characters) - 1)} points!\n'
        com=''
        if score < 4:
            com=(f'The password is quite weak! Score: {str(score)}/7')
        elif score == 4:
            com=(f'The password is OK! Score: {str(score)} /7')
        elif 4 < score < 6:
            com=(f'The password is good! Score: {str(score)} /7')
        elif score >= 6:
            com=(f'The password is strong! Score: {str(score)} /7')
        dispScore+=com
        # abbas end
        rating.config(text=dispScore)

    b = Button(win, text='Check', command=clickstrength)
    b.place(x=50,y=100)


root = Tk()
root.geometry('2000x2000')
titlebox = Label(root, text='Password generator', width=50, bg='Gold', fg='Purple', font=('Arial', 20)).grid(pady=15)
Mess = Label(root, text='What would you like to do? ', width=40, bg='Gold', fg='White', font=('Arial', 18)).grid(pady=35)
bg=PhotoImage(file='E:\Python\Python Miniproject\Mainscreen_BG.png')
bglab=Label( root, image = bg).place(x=800,y=200)
buttonframe = Frame(root)
btngen = Button(buttonframe, text='Generate Password', font=('Arial', 18), command=generate).grid()
btnchk = Button(buttonframe, text='Check Password Strength', font=('Arial', 18), command=stren).grid()
buttonframe.grid()
root.mainloop()