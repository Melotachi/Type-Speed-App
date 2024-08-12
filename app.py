
from tkinter import *

class TypeSpeed(Tk):
    def __init__(self,words):
        super().__init__()
        self.minsize(1000,600)
        self.config(bg='#DEF9C4')
        
        self.label_frame = Frame(self, bg='#DEF9C4')
        self.label_frame.pack(fill='x', padx=20, pady=20)
        
        self.right_label = Label(self.label_frame,text=0,bg='#387F39',font=('calibre',30,'normal'))
        self.right_label.pack(side='left',padx=20,pady=20)
        
        self.wrong_label = Label(self.label_frame,text=0,bg='#973131',font=('calibre',30,'normal'))
        self.wrong_label.pack(side='right',padx=20,pady=20)
        
        self.time_label = Label(self.label_frame,text=60,bg='#F7EFE5',font=('calibre',30,'normal'))
        self.time_label.pack(padx=20,pady=20)
        
        self.play_frame = Frame(self,width=550,height=70,bg='#808D7C')
        self.play_frame.pack(fill='x',padx=20,pady=120)
        
        self.entry = Entry(self,font=('calibre',20,'normal'),width=15)
        self.entry.pack(padx=20)       
        self.entry.bind('<Return>',self.on_enter) # When the user presses enter, the entered text will be checked
        self.entry.bind('<KeyPress>',self.start_timer) # When the user starts typing, the timer will start
        self.words = words 
        
        
        self.words_label = Label(self.play_frame,bg='#F7EFE5',font=('calibre',20,'normal'),wraplength=0,width=30)
        self.words_label.pack(anchor='w')
        
        self.right = 0
        self.wrong = 0
        self.time_left = 60
        
        self.first_time_start = True # To start the timer only once
        
        self.show_words()
        self.mainloop()
        
    def start_timer(self,event): # This function will start the timer when the user starts typing
        if self.first_time_start:
            self.first_time_start = False
            self.update_timer()
        
        
    def on_enter(self,event): # This function will check the entered text when the user presses enter
        entered_text = self.entry.get()
        print(f'Entered text: {entered_text}')
        
        label = self.words_label.cget('text')
        first_word = label.split(' ')[0]
        if entered_text: # If the user entered something (I did not want to count empty strings)
            if entered_text==first_word:
                self.right+=1
            else:
                self.wrong+=1
            
            if self.words:
                self.words.pop(0) # Remove the first word from the list
                self.show_words()
            else:
                pass # game finish               
                
            self.right_label.config(text=self.right)
            self.wrong_label.config(text=self.wrong)
        
        self.entry.delete(0,END) # Clear the entry
        
    def show_words(self):
        my_words = ""
    
        for word in self.words[:12]: # Show only 12 words, you can change this number.
            my_words+= word+" "
        
        my_words.rsplit(' ')
        self.words_label.config(text=my_words,width=65)
        
    def update_timer(self): # This function will update the timer
        if self.time_left > 0: # If the time is not finished
            self.time_left-=1
            self.time_label.config(text=self.time_left)
            self.after(1000,self.update_timer)
        else:
            self.entry.config(state='disabled')
            self.time_label.config(text="Time finished!")
            self.entry.destroy() # Destroy the entry since the time is finished
              
            accuracy = round((self.right / (self.right + self.wrong)) * 100, 3)
            per_minute = round(self.right / 60, 3)

            self.words_label.config(text=f"Accuracy: {accuracy}%\nPer Minute: {per_minute} words.")
            # YOu can add more statistics here.
          
        