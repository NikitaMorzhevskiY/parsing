import tkinter as tk
import gui.app as app

def main():
    
    root = tk.Tk()
    root.resizable(False, False)  
    app_instance = app.MyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()