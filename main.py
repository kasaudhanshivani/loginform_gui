from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
def handle_login():
    email =email_input.get()
    password=password_input.get()
    if email == 'shivanik@gmail.com'and password=='2222':
        messagebox.showinfo('Yayyy','login successful')

    else:
        messagebox.showerror('Error','login failec')


# Create the main window
root = Tk()
root.title("Login Form")
root.geometry('350x550')
root.configure(background='#FF4263')

# Load the image
image_path = "C:\\Users\\new pc\\OneDrive\\Documents\\portfolio\\download.jpeg"  # Update with your logo path
img = Image.open(image_path)
img = ImageTk.PhotoImage(img)

# Create a label to display the image
img_label = Label(root, image=img)
img_label.pack(pady=20)
text_label=Label(root,text="Meesho",fg='white',bg='#FF4263')
text_label.pack()
text_label.config(font=('italics',24))

email_label=Label(root,text='Enter Email',fg='black',bg='#FF4263')
email_label.pack(pady=(20,6))
email_label.config(font=('vardana',12))
email_input=Entry(root,width=50)
email_input.pack(ipady=6)

password_label=Label(root,text='Enter Password',fg='black',bg='#FF4263')
password_label.pack(pady=(20,6))
password_label.config(font=('vardana',12))
password_input=Entry(root,width=50)
password_input.pack(ipady=6)

login_btn=Button(root,text='Login here',bg='white',fg='black',width=20,height=2)
login_btn.pack(pady =(10,20))
login_btn.config(font=('vardana',14))


# Start the GUI event loop
root.mainloop()
