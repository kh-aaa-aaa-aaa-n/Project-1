from tkinter import Tk, Frame, Label, StringVar, IntVar, Entry, Button, Radiobutton, OptionMenu
from shapes.area import circ_area, rect_area, square_area, tri_area
from shapes.perimeter import circ_circumference, rect_perimeter, square_perimeter, tri_perimeter

class FourShapeCalc:
    """
    Represents the details for a FourShapeCalc object.
    """
    def __init__(self) -> None:
        """
        Constructor to initialize a FourShapeCalc instance.
        """
        # Creates the main/root window.
        self.window = Tk()
        self.window.title('Four-Shape Math Calculator')
        self.window.geometry('320x225')
        self.window.resizable(False, False)
        
        # Creates all the frames used inside the main window.
        self.title_frame = Frame(self.window)
        self.selection_frame = Frame(self.window)
        self.calc_frame = Frame(self.window)
        self.result_frame = Frame(self.window)
        
        # Creates the label in title_frame.
        self.title_label = Label(self.title_frame, text = 'Select Shape', pady = 10)
        
        # Creates the labels in the calc_frame frame.
        self.calc_val1_label = Label(self.calc_frame, padx = 10, pady = 5)
        self.calc_val2_label = Label(self.calc_frame, padx = 10, pady = 5)
        self.calc_val3_label = Label(self.calc_frame, padx = 10, pady = 5)
        self.calc_err1_label = Label(self.calc_frame)
        self.calc_err2_label = Label(self.calc_frame)
        self.calc_err3_label = Label(self.calc_frame)
        
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
                                            command = self.update_window_size)
        
        # Packs title_label in title_frame.
        self.title_label.pack()
        
        # Puts the radio buttons and option menu in selection_frame with grid.
        self.area_perimeter_om.grid(row = 0, column = 1, rowspan = 2, padx = 7)
        self.circ_radiobutton.grid(row = 0, column = 0, pady = 2, sticky = 'w')
        self.rect_radiobutton.grid(row = 1, column = 0, pady = 2, sticky = 'w')
        self.square_radiobutton.grid(row = 0, column = 2, pady = 2, sticky = 'w')
        self.tri_radiobutton.grid(row = 1, column = 2, pady = 2, sticky = 'w')
        
        # Packs the frames to the main window.
        self.title_frame.pack()
        self.selection_frame.pack()
        self.calc_frame.pack(anchor = 'w', pady = 15)
        self.result_frame.pack()
    
    # FIXME: INESSENTIAL -
    #        Sends the window to the top left corner of the screen the first time a radio
    #        button is selected when called anywhere.
    def update_window_size(self, x = '') -> None:
        """
        Changes the size of the window slightly wider or slimmer depending on if the word
        'Circumference' is selected in the OptionMenu.
        
        :param x: I honestly don't know why this is here or why it works, but it's required for the
                  implementation to work properly. Don't touch it, or it may break the function.
        """
        if 'Circumference' != self.clicked.get():
            self.window.geometry('300x225')
        else:
            self.window.geometry('320x225')
    
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
        
        self.update_window_size()
        
        # Gets the current value of the OptionMenu.
        clicked: str = self.clicked.get()
        
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
                self.clear_calc_zone()
                
                self.calc_val1_label.config(text = 'Radius')
                set_grid(1)
                make_buttons()
            elif selected == 2:
                # Sets the frame to calculate the area of a rectangle.
                self.clear_calc_zone()
                
                self.calc_val1_label.config(text = 'Length')
                self.calc_val2_label.config(text = 'Width')
                set_grid(2)
                make_buttons()
            elif selected == 3:
                # Sets the frame to calculate the area of a square.
                self.clear_calc_zone()
                
                self.calc_val1_label.config(text = ' Side ')
                set_grid(1)
                make_buttons()
            elif selected == 4:
                # Sets the frame to calculate the area of a triangle.
                self.clear_calc_zone()
                
                self.calc_val1_label.config(text = 'Base')
                self.calc_val2_label.config(text = 'Height')
                set_grid(2)
                make_buttons()
        elif clicked == 'Perimeter':
            if selected == 1:
                # Sets the frame to calculate the circumference of a circle.
                self.clear_calc_zone()
                
                self.calc_val1_label.config(text = 'Radius')
                set_grid(1)
                make_buttons()
            elif selected == 2:
                # Sets the frame to calculate the perimeter of a rectangle.
                self.clear_calc_zone()
                
                self.calc_val1_label.config(text = 'Length')
                self.calc_val2_label.config(text = 'Width')
                set_grid(2)
                make_buttons()
            elif selected == 3:
                # Sets the frame to calculate the perimeter of a square.
                self.clear_calc_zone()
                
                self.calc_val1_label.config(text = ' Side ')
                set_grid(1)
                make_buttons()
            elif selected == 4:
                # Sets the frame to calculate the perimeter of a triangle.
                self.clear_calc_zone()
                
                self.calc_val1_label.config(text = 'Side 1')
                self.calc_val2_label.config(text = 'Side 2')
                self.calc_val3_label.config(text = 'Side 3')
                self.clear_button.config(height = 1, width = 6)
                set_grid(2)
                self.calc_val3_label.grid(row = 2, column = 0, sticky = 'w')
                self.calc_val3_entry.grid(row = 2, column = 1)
                self.submit_button.grid(row = 0, column = 2, padx = 10, pady = 5)
                self.clear_button.grid(row = 2, column = 2, padx = 10, pady = 5)
                
    def clear_calc_zone(self) -> None:
        """
        Clears the frame, so the widgets don't overlap and mess with the formatting.
        """
        self.calc_val1_label.grid_forget()
        self.calc_val2_label.grid_forget()
        self.calc_val3_label.grid_forget()
        self.calc_val1_entry.grid_forget()
        self.calc_val2_entry.grid_forget()
        self.calc_val3_entry.grid_forget()
        self.calc_err1_label.grid_forget()
        self.calc_err2_label.grid_forget()
        self.calc_err3_label.grid_forget()
        self.submit_button.grid_forget()
        self.clear_button.grid_forget()
        self.result_label.grid_forget()
    
    def clicked_submit(self) -> None:
        """
        Does the proper calculation according to the selected options and projects the results.
        """
        def clear_results():
            self.calc_err1_label.grid_forget()
            self.calc_err2_label.grid_forget()
            self.calc_err3_label.grid_forget()
            self.result_label.grid_forget()
        
        def clear_for_rearrange():
            self.calc_val2_label.grid_forget()
            self.calc_val2_entry.grid_forget()
            self.submit_button.grid_forget()
            self.clear_button.grid_forget()
        
        selected: int = self.selected.get()
        clicked: str = self.clicked.get()
        
        area: str
        radius: str
        length: str
        width: str
        leng: str
        wid: str
        side: str
        base: str
        height: str
        bas: str
        hei: str
        circumference: str
        perimeter: str
        side1: str
        side2: str
        side3: str
        sid1: str
        sid2: str
        sid3: str
        if clicked == 'Area':
            if selected == 1:
                # Calculates and projects the area of the circle.
                clear_results()
                
                radius = self.calc_val1_entry.get().strip()
                area = circ_area(radius)
                
                # Works with shapes.area to check for invalid inputs in circ_area.
                if area == 'ValErr':
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err1_label.grid(row = 1, column = 1)
                else:
                    self.result_label.config(text = f'Circle area = {area}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 2:
                # Calculates and projects the area of the rectangle.
                clear_results()
                
                length = self.calc_val1_entry.get().strip()
                width = self.calc_val2_entry.get().strip()
                area, leng, wid = rect_area(length, width)
                
                # Works with shapes.area to check for invalid inputs in rect_area.
                if area == 'ValErr':
                    clear_for_rearrange()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, rowspan = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, rowspan = 2, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_err2_label.grid(row = 3, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                elif leng == 'ValErr_l':
                    clear_for_rearrange()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                elif wid == 'ValErr_w':
                    clear_for_rearrange()
                    
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 1, column = 2, padx = 15, pady = 2)
                    self.calc_err2_label.grid(row = 2, column = 1)
                    self.calc_val2_label.grid(row = 1, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 1, column = 1)
                else:
                    self.result_label.config(text = f'Rectangle area = {area}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 3:
                # Calculates and projects the area of the square.
                clear_results()
                
                side = self.calc_val1_entry.get().strip()
                area = square_area(side)
                
                # Works with shapes.area to check for invalid inputs in square_area.
                if area == 'ValErr':
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err1_label.grid(row = 1, column = 1)
                else:
                    self.result_label.config(text = f'Square area = {area}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 4:
                # Calculates and projects the area of the triangle.
                clear_results()
                
                base = self.calc_val1_entry.get().strip()
                height = self.calc_val2_entry.get().strip()
                area, bas, hei = tri_area(base, height)
                
                # Works with shapes.area to check for invalid inputs in tri_area.
                if area == 'ValErr':
                    clear_for_rearrange()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, rowspan = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, rowspan = 2, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_err2_label.grid(row = 3, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                elif bas == 'ValErr_b':
                    clear_for_rearrange()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                elif hei == 'ValErr_h':
                    clear_for_rearrange()
                    
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 1, column = 2, padx = 15, pady = 2)
                    self.calc_err2_label.grid(row = 2, column = 1)
                    self.calc_val2_label.grid(row = 1, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 1, column = 1)
                else:
                    self.result_label.config(text = f'Triangle area = {area}')
                    self.result_label.grid(row = 2, column = 1)
        elif clicked == 'Perimeter':
            if selected == 1:
                # Calculates and projects the circumference of the circle.
                clear_results()
                
                radius = self.calc_val1_entry.get().strip()
                circumference = circ_circumference(radius)
                
                # Works with shapes.perimeter to check for invalid inputs in circ_circumference.
                if circumference == 'ValErr':
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err1_label.grid(row = 1, column = 1)
                else:
                    self.result_label.config(text = f'Circle circumference = {circumference}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 2:
                # Calculates and projects the perimeter of the rectangle.
                clear_results()
                
                length = self.calc_val1_entry.get().strip()
                width = self.calc_val2_entry.get().strip()
                perimeter, leng, wid = rect_perimeter(length, width)
                
                # Works with shapes.perimeter to check for invalid inputs in rect_perimeter.
                if perimeter == 'ValErr':
                    clear_for_rearrange()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, rowspan = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, rowspan = 2, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_err2_label.grid(row = 3, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                elif leng == 'ValErr_l':
                    clear_for_rearrange()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                elif wid == 'ValErr_w':
                    clear_for_rearrange()
                    
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 1, column = 2, padx = 15, pady = 2)
                    self.calc_err2_label.grid(row = 2, column = 1)
                    self.calc_val2_label.grid(row = 1, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 1, column = 1)
                else:
                    self.result_label.config(text = f'Rectangle perimeter = {perimeter}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 3:
                # Calculates and projects the perimeter of the square.
                clear_results()
                
                side = self.calc_val1_entry.get().strip()
                perimeter = square_perimeter(side)
                
                # Works with shapes.perimeter to check for invalid inputs in square_perimeter().
                if perimeter == 'ValErr':
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err1_label.grid(row = 1, column = 1)
                else:
                    self.result_label.config(text = f'Square perimeter = {perimeter}')
                    self.result_label.grid(row = 2, column = 1)
            elif selected == 4:
                # Calculates and projects the perimeter of the triangle.
                clear_results()
                
                side1 = self.calc_val1_entry.get().strip()
                side2 = self.calc_val2_entry.get().strip()
                side3 = self.calc_val3_entry.get().strip()
                perimeter, sid1, sid2, sid3 = tri_perimeter(side1, side2, side3)
                
                # Works with shapes.perimeter to check for invalid inputs in tri_perimeter.
                if perimeter == 'ValErr':
                    clear_for_rearrange()
                    self.calc_val3_label.grid_forget()
                    self.calc_val3_entry.grid_forget()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.calc_err3_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, rowspan = 3, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, rowspan = 3, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_err2_label.grid(row = 3, column = 1)
                    self.calc_err3_label.grid(row = 5, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val3_label.grid(row = 4, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                    self.calc_val3_entry.grid(row = 4, column = 1)
                elif perimeter == 'ValErr_s1s2':
                    clear_for_rearrange()
                    self.calc_val3_label.grid_forget()
                    self.calc_val3_entry.grid_forget()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, rowspan = 3, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, rowspan = 3, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_err2_label.grid(row = 3, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val3_label.grid(row = 4, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                    self.calc_val3_entry.grid(row = 4, column = 1)
                elif perimeter == 'ValErr_s1s3':
                    clear_for_rearrange()
                    self.calc_val3_label.grid_forget()
                    self.calc_val3_entry.grid_forget()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.calc_err3_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, rowspan = 3, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, rowspan = 3, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_err3_label.grid(row = 4, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val3_label.grid(row = 3, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                    self.calc_val3_entry.grid(row = 3, column = 1)
                elif perimeter == 'ValErr_s2s3':
                    clear_for_rearrange()
                    self.calc_val3_label.grid_forget()
                    self.calc_val3_entry.grid_forget()
                    
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.calc_err3_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, rowspan = 3, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, rowspan = 3, padx = 15, pady = 2)
                    self.calc_err2_label.grid(row = 2, column = 1)
                    self.calc_err3_label.grid(row = 4, column = 1)
                    self.calc_val2_label.grid(row = 1, column = 0, sticky = 'w')
                    self.calc_val3_label.grid(row = 3, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 1, column = 1)
                    self.calc_val3_entry.grid(row = 3, column = 1)
                elif sid1 == 'ValErr_s1':
                    clear_for_rearrange()
                    self.calc_val3_label.grid_forget()
                    self.calc_val3_entry.grid_forget()
                    
                    self.calc_err1_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 3, column = 2, padx = 15, pady = 2)
                    self.calc_err1_label.grid(row = 1, column = 1)
                    self.calc_val2_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val3_label.grid(row = 3, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 2, column = 1)
                    self.calc_val3_entry.grid(row = 3, column = 1)
                elif sid2 == 'ValErr_s2':
                    clear_for_rearrange()
                    self.calc_val3_label.grid_forget()
                    self.calc_val3_entry.grid_forget()
                    
                    self.calc_err2_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 3, column = 2, padx = 15, pady = 2)
                    self.calc_err2_label.grid(row = 2, column = 1)
                    self.calc_val2_label.grid(row = 1, column = 0, sticky = 'w')
                    self.calc_val3_label.grid(row = 3, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 1, column = 1)
                    self.calc_val3_entry.grid(row = 3, column = 1)
                elif sid3 == 'ValErr_s3':
                    clear_for_rearrange()
                    self.calc_val3_label.grid_forget()
                    self.calc_val3_entry.grid_forget()
                    
                    self.calc_err3_label.config(text = 'Numeric values only')
                    self.clear_button.config(height = 1, width = 6)
                    self.submit_button.grid(row = 0, column = 2, padx = 15, pady = 2)
                    self.clear_button.grid(row = 2, column = 2, padx = 15, pady = 2)
                    self.calc_err3_label.grid(row = 3, column = 1)
                    self.calc_val2_label.grid(row = 1, column = 0, sticky = 'w')
                    self.calc_val3_label.grid(row = 2, column = 0, sticky = 'w')
                    self.calc_val2_entry.grid(row = 1, column = 1)
                    self.calc_val3_entry.grid(row = 2, column = 1)
                else:
                    self.result_label.config(text = f'Triangle perimeter = {perimeter}')
                    self.result_label.grid(row = 2, column = 1)
    
    def clicked_clear(self) -> None:
        """
        Resets calc_frame based on the current selected radiobutton.
        """
        self.calc_val1_entry.delete(0, 'end')
        self.calc_val2_entry.delete(0, 'end')
        self.calc_val3_entry.delete(0, 'end')
        self.clear_calc_zone()
        self.set_calc_zone(self.selected.get())
    
    def start(self) -> None:
        """
        Engages the loop to open and keep the window on.
        """
        self.window.mainloop()

if __name__ == '__main__':
    FourShapeCalc().start()
