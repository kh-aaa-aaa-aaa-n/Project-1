from tkinter import Tk, Frame, Label, StringVar, IntVar, Entry, Button, Radiobutton, OptionMenu
from shapes.area import circ_area, rect_area, square_area, tri_area
from shapes.perimeter import circ_circumference, rect_perimeter, square_perimeter, tri_perimeter

class FourShapeCalc:
    """
    Represents the details for a FourShapeCalc object.
    """
    def __init__(self) -> None:
        """
        Constructor to initialize a FourShapeCalc object.
        """
        # Creates the main/root window.
        self.window = Tk()
        self.window.title('Four-Shape Math Calculator')
        self.window.geometry('320x225')
        self.window.resizable(False, False)
        
        # Creates all the frames used inside the main window.
        self.select_shape_label_frame = Frame(self.window)
        self.selection_frame = Frame(self.window)
        self.calc_frame = Frame(self.window)
        self.result_frame = Frame(self.window)
        
        # Creates the label in select_shape_label_frame.
        self.select_shape_label = Label(self.select_shape_label_frame, text = 'Select Shape', pady = 10)
        
        # Creates the labels in the calc_frame frame.
        self.calc_val1_label = Label(self.calc_frame, padx = 10, pady = 5)
        self.calc_val2_label = Label(self.calc_frame, padx = 10, pady = 5)
        self.calc_val3_label = Label(self.calc_frame, padx = 10, pady = 5)
        
        # Creates the label in result_frame.
        self.result_label = Label(self.result_frame)
        
        # Creates the entry boxes in calc_frame.
        self.calc_val1_val = StringVar()
        self.calc_val2_val = StringVar()
        self.calc_val3_val = StringVar()
        self.calc_val1_entry = Entry(self.calc_frame, textvariable = self.calc_val1_val)
        self.calc_val2_entry = Entry(self.calc_frame, textvariable = self.calc_val2_val)
        self.calc_val3_entry = Entry(self.calc_frame, textvariable = self.calc_val3_val)
        
        # Creates the buttons in calc_frame.
        self.submit_button = Button(self.calc_frame, text = 'Submit', command = self.clicked_submit)
        self.clear_button = Button(self.calc_frame, text = 'Clear', command = self.clicked_clear)
        
        # Creates the radio buttons in selection_frame.
        self.selected = IntVar()
        self.selected.set(5)
        self.circ_radiobutton = Radiobutton(self.selection_frame, text = 'Circle', value = 1, 
                                       variable = self.selected, command = lambda: self.set_calc_zone(1))
        self.rect_radiobutton = Radiobutton(self.selection_frame, text = 'Rectangle', value = 2, 
                                       variable = self.selected, command = lambda: self.set_calc_zone(2))
        self.square_radiobutton = Radiobutton(self.selection_frame, text = 'Square', value = 3, 
                                         variable = self.selected, command = lambda: self.set_calc_zone(3))
        self.tri_radiobutton = Radiobutton(self.selection_frame, text = 'Triangle', value = 4, 
                                      variable = self.selected, command = lambda: self.set_calc_zone(4))
        
        # Creates the option menu in selection_frame.
        self.options = ['Area', 'Perimeter']
        self.clicked = StringVar()
        self.clicked.set(self.options[0])
        self.area_perimeter_om = OptionMenu(self.selection_frame, self.clicked, *self.options,
                                            command = lambda: self.update_window_size())
        
        # Packs select_shape_label in select_shape_label_frame.
        self.select_shape_label.pack()
        
        # Puts the radio buttons and option menu in selection_frame with grid.
        self.area_perimeter_om.grid(row = 0, column = 1, rowspan = 2, padx = 7)
        self.circ_radiobutton.grid(row = 0, column = 0, pady = 2, sticky = 'w')
        self.rect_radiobutton.grid(row = 1, column = 0, pady = 2, sticky = 'w')
        self.square_radiobutton.grid(row = 0, column = 2, pady = 2, sticky = 'w')
        self.tri_radiobutton.grid(row = 1, column = 2, pady = 2, sticky = 'w')
        
        # Packs the frames to the main window.
        self.select_shape_label_frame.pack()
        self.selection_frame.pack()
        self.calc_frame.pack(anchor = 'w', pady = 15)
        self.result_frame.pack()
    
    # FIXME: INESSENTIAL -
    #        Gives 'TypeError: <lambda>() takes 0 positional arguments but 1 was given' before any
    #        radio button is selected when assigned to area_perimeter_om using 
    #        'command = lambda: self.update_window_size()'.
    #        Also sends the window to the top left corner of the screen the first time a radio
    #        button is selected when called anywhere.
    def update_window_size(self) -> None:
        """
        Changes the size of the window slightly wider or slimmer depending on if the word
        'Circumference' is used.
        """
        print(f'self.clicked.get()')
        # if 'Circumference' != self.clicked.get():
        #     self.window.resizable(True, True)
        #     self.window.geometry('300x225')
        #     self.window.resizable(False, False)
        # else:
        #     self.window.resizable(True, True)
        #     self.window.geometry('320x225')
        #     self.window.resizable(False, False)
    
    def set_calc_zone(self, selected: int) -> None:
        """
        Sets the screen/window state to the proper layout for the calculations according to the
        selected options.
        
        :param selected: The selected shape
        """
        # Sets 'Perimeter' to 'Circumference' when circle is selected and vice versa.
        if selected == 1:
            self.options[1] = 'Circumference'
            if self.clicked.get() == 'Perimeter':
                self.clicked.set(self.options[1])
            
        else:
            self.options[1] = 'Perimeter'
            if self.clicked.get() == 'Circumference':
                self.clicked.set(self.options[1])
        
        menu = self.area_perimeter_om['menu']
        menu.delete(0, "end")
        for option in self.options:
            menu.add_command(label = option, command = lambda value = option: self.clicked.set(value))
        
        # Definition is commented out, so this is, too.
        self.update_window_size()
        
        # Gets the current value of the OptionMenu.
        clicked = self.clicked.get()
        
        def make_buttons() -> None:
            """
            Sets the buttons to the right configuration and adds them to the frame with grid.
            """
            self.clear_button.config(height = 1, width = 6)
            self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
            self.clear_button.grid(row = 1, column = 2, padx = 15, pady = 2)
        
        def set_grid(version: int) -> None:
            """
            Sets the grid and label/entry widgets within the frame in two varieties.
            """
            if version == 1:
                self.calc_val1_label.grid(row = 0, column = 0, rowspan = 2)
                self.calc_val1_entry.grid(row = 0, column = 1, rowspan = 2)
            elif version == 2:
                self.calc_val1_label.grid(row = 0, column = 0, sticky = 'w')
                self.calc_val2_label.grid(row = 1, column = 0, sticky = 'w')
                self.calc_val1_entry.grid(row = 0, column = 1)
                self.calc_val2_entry.grid(row = 1, column = 1)
        
        if clicked == 'Area':
            if selected == 1:
                # Sets the frame to calculate the area of a circle.
                self.reset_calc_zone()
                
                self.calc_val1_label.config(text = 'Radius')
                set_grid(1)
                make_buttons()
            elif selected == 2:
                # Sets the frame to calculate the area of a rectangle.
                self.reset_calc_zone()
                
                self.calc_val1_label.config(text = 'Length')
                self.calc_val2_label.config(text = 'Width')
                set_grid(2)
                make_buttons()
            elif selected == 3:
                # Sets the frame to calculate the area of a square.
                self.reset_calc_zone()
                
                self.calc_val1_label.config(text = ' Side ')
                set_grid(1)
                make_buttons()
            elif selected == 4:
                # Sets the frame to calculate the area of a triangle.
                self.reset_calc_zone()
                
                self.calc_val1_label.config(text = 'Base')
                self.calc_val2_label.config(text = 'Height')
                set_grid(2)
                make_buttons()
        elif clicked == 'Perimeter':
            if selected == 1:
                # Sets the frame to calculate the circumference of a circle.
                self.reset_calc_zone()
                
                self.calc_val1_label.config(text = 'Radius')
                set_grid(1)
                make_buttons()
            elif selected == 2:
                # Sets the frame to calculate the perimeter of a rectangle.
                self.reset_calc_zone()
                
                self.calc_val1_label.config(text = 'Length')
                self.calc_val2_label.config(text = 'Width')
                set_grid(2)
                make_buttons()
            elif selected == 3:
                # Sets the frame to calculate the perimeter of a square.
                self.reset_calc_zone()
                
                self.calc_val1_label.config(text = ' Side ')
                set_grid(1)
                make_buttons()
            elif selected == 4:
                # Sets the frame to calculate the perimeter of a triangle.
                self.reset_calc_zone()
                
                self.calc_val1_label.config(text = 'Side 1')
                self.calc_val2_label.config(text = 'Side 2')
                self.calc_val3_label.config(text = 'Side 3')
                self.clear_button.config(height = 1, width = 6)
                set_grid(2)
                self.calc_val3_label.grid(row = 2, column = 0, sticky = 'w')
                self.calc_val3_entry.grid(row = 2, column = 1)
                self.submit_button.grid(row = 0, column = 2, padx = 10, pady = 5)
                self.clear_button.grid(row = 2, column = 2, padx = 10, pady = 5)
                
    def reset_calc_zone(self) -> None:
        """
        Clears the frame, so the widgets don't overlap and mess with the formatting.
        """
        self.calc_val1_label.grid_forget()
        self.calc_val2_label.grid_forget()
        self.calc_val3_label.grid_forget()
        self.calc_val1_entry.grid_forget()
        self.calc_val2_entry.grid_forget()
        self.calc_val3_entry.grid_forget()
        self.submit_button.grid_forget()
        self.clear_button.grid_forget()
    
    def clicked_submit(self) -> None:
        """
        Does the proper calculation according to the selected options and projects the results.
        """
        selected: int = self.selected.get()
        clicked: str = self.clicked.get()
        
        if clicked == 'Area':
            if selected == 1:
                # Calculates and projects the area of the circle.
                self.result_label.grid_forget()
                
                radius: str = self.calc_val1_entry.get().strip()
                area: str = circ_area(radius)
                
                # Works with shapes.area to check for invalid inputs.
                if area == 'ValErr':
                    self.result_label.config(text = 'Numeric values only')
                    self.result_label.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Circle area = {area}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 2:
                # Calculates and projects the area of the rectangle.
                self.result_label.grid_forget()
                
                length: str = self.calc_val1_entry.get().strip()
                width: str = self.calc_val2_entry.get().strip()
                area: str = rect_area(length, width)
                
                # Works with shapes.area to check for invalid inputs.
                if area == 'ValErr':
                    self.result_label.config(text = 'Numeric values only')
                    self.result_label.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Rectangle area = {area}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 3:
                # Calculates and projects the area of the square.
                self.result_label.grid_forget()
                
                side: str = self.calc_val1_entry.get().strip()
                area: str = square_area(side)
                
                # Works with shapes.area to check for invalid inputs.
                if area == 'ValErr':
                    self.result_label.config(text = 'Numeric values only')
                    self.result_label.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Square area = {area}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 4:
                # Calculates and projects the area of the triangle.
                self.result_label.grid_forget()
                
                base: str = self.calc_val1_entry.get().strip()
                height: str = self.calc_val2_entry.get().strip()
                area: str = tri_area(base, height)
                
                # Works with shapes.area to check for invalid inputs.
                if area == 'ValErr':
                    self.result_label.config(text = 'Numeric values only')
                    self.result_label.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Triangle area = {area}')
                    self.result_label.grid(row = 2, column = 1)
        elif clicked == 'Perimeter':
            if selected == 1:
                # Calculates and projects the circumference of the circle.
                self.result_label.grid_forget()
                
                radius: str = self.calc_val1_entry.get().strip()
                circumference: str = circ_circumference(radius)
                
                # Works with shapes.perimeter to check for invalid inputs.
                if circumference == 'ValErr':
                    self.result_label.config(text = 'Numeric values only')
                    self.result_label.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Circle circumference = {circumference}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 2:
                # Calculates and projects the perimeter of the rectangle.
                self.result_label.grid_forget()
                
                length: str = self.calc_val1_entry.get().strip()
                width: str = self.calc_val2_entry.get().strip()
                perimeter: str = rect_perimeter(length, width)
                
                # Works with shapes.perimeter to check for invalid inputs.
                if perimeter == 'ValErr':
                    self.result_label.config(text = 'Numeric values only')
                    self.result_label.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Rectangle perimeter = {perimeter}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 3:
                # Calculates and projects the perimeter of the square.
                self.result_label.grid_forget()
                
                side: str = self.calc_val1_entry.get().strip()
                perimeter: str = square_perimeter(side)
                
                # Works with shapes.perimeter to check for invalid inputs.
                if perimeter == 'ValErr':
                    self.result_label.config(text = 'Numeric values only')
                    self.result_label.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Square perimeter = {perimeter}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 4:
                # Calculates and projects the perimeter of the triangle.
                self.result_label.grid_forget()
                
                side1: str = self.calc_val1_entry.get().strip()
                side2: str = self.calc_val2_entry.get().strip()
                side3: str = self.calc_val3_entry.get().strip()
                perimeter: str = tri_perimeter(side1, side2, side3)
                
                # Works with shapes.perimeter to check for invalid inputs.
                if perimeter == 'ValErr':
                    self.result_label.config(text = 'Numeric values only')
                    self.result_label.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Triangle perimeter = {perimeter}')
                    self.result_label.grid(row = 2, column = 1)
    
    def clicked_clear(self) -> None:
        """
        Clears the entry boxes and removes the result message from the window.
        """
        self.calc_val1_entry.delete(0, 'end')
        self.calc_val2_entry.delete(0, 'end')
        self.result_label.grid_forget()
    
    def start(self) -> None:
        """
        Engages the loop to open and keep the window on.
        """
        self.window.mainloop()

if __name__ == '__main__':
    FourShapeCalc().start()
