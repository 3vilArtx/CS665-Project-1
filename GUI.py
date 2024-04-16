import sqlite3
import tkinter as tk
import tkinter.messagebox as messagebox
from unittest import result
from tkinterhtml import HtmlFrame
from PIL import Image, ImageTk  
import pandas as pd
import os

dbFile = 'projectDB.db'
conn = sqlite3.connect(dbFile)
c = conn.cursor()

# Function to create tables from SQL file
def create_tables():
    try:
        with open('create.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            print("Executing SQL script:")
            print(sql_script)
            c.executescript(sql_script)
        conn.commit()
        print("Tables created successfully")
        check_tables_exist()  # Add this line to check if tables exist after creation
    except Exception as e:
        print("Error creating tables:", e)

def check_tables_exist():
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = c.fetchall()
    table_names = [table[0] for table in tables]
    if len(table_names) == 0:
        create_tables()
    print("Tables in database:", table_names)
    return table_names

# Function to execute a SQL query and return result as a DataFrame
def execute_query_to_dataframe(query):
    try:
        # Execute the query
        c.execute(query)
        
        # Fetch all rows
        rows = c.fetchall()
        
        # Fetch column names
        columns = [desc[0] for desc in c.description]
        
        # Create DataFrame
        df = pd.DataFrame(rows, columns=columns)
        
        return df
    except Exception as e:
        print("Error executing query:", e)

# Function to open table selection window
def open_table_selection_window():
    table_names = check_tables_exist()
    new_window = tk.Toplevel(root)
    new_window.title("Select Table")
    
    selected_table = tk.StringVar(new_window)
    selected_table.set(table_names[0])  # Set the default value

    table_dropdown = tk.OptionMenu(new_window, selected_table, *table_names)
    table_dropdown.pack()

    def show_selected_table():
        selected = selected_table.get()
        query = f"SELECT * FROM {selected}"
        df = execute_query_to_dataframe(query)
        
        # Display DataFrame in a new window
        if df is not None:
            show_query_result(df, selected,show_delete=True)

    select_button = tk.Button(new_window, text="Select", command=show_selected_table)
    select_button.pack()

# Function to display query result in a new window
def show_query_result(df, selected_table, show_delete=False):
    new_window = tk.Toplevel(root)
    new_window.title(f"Query Result: {selected_table}")
    
    html_frame = HtmlFrame(new_window)
    html_frame.pack(fill="both", expand=True)
    
    # Convert DataFrame to HTML
    html_content = df.to_html(index=False, escape=False)

    # Display HTML content in the HtmlFrame widget
    html_frame.set_content(html_content)
    
    if show_delete:
        # Create a label and text box for entering the value to delete
        delete_label = tk.Label(new_window, text=f"Enter value to delete from {selected_table}:")
        delete_label.pack()
        
        delete_entry_widget = tk.Entry(new_window)
        delete_entry_widget.pack()
        
        # Function to delete entry
        def delete_entry():
            value = delete_entry_widget.get()
            column_name = df.columns[0]  # Assuming the primary key is always the first column
            delete_query = f"DELETE FROM {selected_table} WHERE {column_name} = ?"
            try:
                c.execute(delete_query, (value,))
                conn.commit()
                tk.messagebox.showinfo("Success", "Entry deleted successfully!")
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error deleting entry: {e}")
        
        # Create a button to delete entry
        delete_button = tk.Button(new_window, text="Delete Entry", command=delete_entry)
        delete_button.pack()

def insert_test_data():
    try:
        with open('insert.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            print("Executing SQL script:")
            print(sql_script)
            c.executescript(sql_script)
        conn.commit()
        print("Test data inserted successfully")
    except Exception as e:
        print("Error inserting test data:", e)
#Insert Fields
def open_insert_window():
    table_names = check_tables_exist()
    new_window = tk.Toplevel(root)
    new_window.title("Insert Data")
    
    selected_table = tk.StringVar(new_window)
    selected_table.set("Select Insert Table")  # Set the default value

    table_dropdown = tk.OptionMenu(new_window, selected_table, *table_names, command=lambda selected: show_insert_fields(selected, new_window))
    table_dropdown.pack()

def show_insert_fields(selected, new_window):
    if selected == "Select Insert Table":
        return
    
    # Clear existing text boxes and button
    for widget in new_window.winfo_children():
        if isinstance(widget, (tk.Frame, tk.Button)):
            widget.destroy()
    
    # Create a frame to hold the text boxes
    insert_frame = tk.Frame(new_window)
    insert_frame.pack()
    
    query = f"PRAGMA table_info({selected})"
    table_info = execute_query_to_dataframe(query)
    columns = table_info[table_info['pk'] != 1]['name'].tolist()  # Exclude autoincrement columns
    
    entry_fields = []
    for i, col in enumerate(columns):
        row_index = i % 3
        if row_index == 0:  # Start a new row every 3 columns
            row_frame = tk.Frame(insert_frame)
            row_frame.pack()
        
        label = tk.Label(row_frame, text=col)
        label.grid(row=row_index, column=0)
        
        entry = tk.Entry(row_frame)
        entry.grid(row=row_index, column=1)
        entry_fields.append(entry)
    
    def insert_data():
        values = [entry.get() for entry in entry_fields]
        columns_str = ', '.join(columns)
        values_str = ', '.join([f"'{value}'" for value in values])
        insert_query = f"INSERT INTO {selected} ({columns_str}) VALUES ({values_str})"
        try:
            c.execute(insert_query)
            conn.commit()
            print("Data inserted successfully")
            tk.messagebox.showinfo("Success", "Data inserted successfully!")
            # Clear text boxes and insert button
            for widget in insert_frame.winfo_children():
                widget.destroy()
            insert_button.destroy()
        except Exception as e:
            print("Error inserting data:", e)
    
    insert_button = tk.Button(new_window, text="Insert Data", command=insert_data)
    insert_button.pack()
#Update Fields
def show_update_fields(df, selected_table, new_window):
    # Clear existing widgets
    for widget in new_window.winfo_children():
        widget.destroy()
    
    # Create a frame to hold the table view
    table_frame = tk.Frame(new_window)
    table_frame.pack()
    
    # Display the table as HTML
    html_frame = HtmlFrame(table_frame)
    html_frame.pack(fill="both", expand=True)
    html_content = df.to_html(index=False, escape=False)
    html_frame.set_content(html_content)
    
    # Fetch column names and their data types
    columns = df.columns.tolist()
    unique_id_column = columns[0]  # Assuming the first column is the unique ID
    
    # Create a frame to hold the update fields
    update_frame = tk.Frame(new_window)
    update_frame.pack()
    
    entry_fields = {}
    for col in columns[1:]:  # Exclude the unique ID column from the update
        label = tk.Label(update_frame, text=col)
        label.pack(side="left")
        
        entry = tk.Entry(update_frame)
        entry.pack(side="left")
        
        entry_fields[col] = entry
    
    # Create a label and entry for the unique ID
    id_label = tk.Label(update_frame, text=f"{unique_id_column} to update:")
    id_label.pack(side="left")
    
    id_entry = tk.Entry(update_frame)
    id_entry.pack(side="left")
    
    def update_data():
        # Construct the SET part of the SQL UPDATE statement
        set_fields = []
        for col, entry in entry_fields.items():
            value = entry.get()
            if value:  # Exclude empty textboxes
                set_fields.append(f"{col} = '{value}'")
        
        set_clause = ",\n".join(set_fields)
        
        # Construct the WHERE part of the SQL UPDATE statement
        unique_id_value = id_entry.get()
        where_clause = f"{unique_id_column} = '{unique_id_value}'"
        
        # Construct the SQL UPDATE statement
        update_query = f"UPDATE {selected_table}\nSET {set_clause}\nWHERE {where_clause}"
        
        try:
            c.execute(update_query)
            conn.commit()
            print("Data updated successfully")
            tk.messagebox.showinfo("Success", "Data updated successfully!")
            new_window.destroy()
        except Exception as e:
            print("Error updating data:", e)
            tk.messagebox.showerror("Error", f"Error updating data: {e}")
    
    update_button = tk.Button(new_window, text="Update Data", command=update_data)
    update_button.pack()

def open_update_window():
    table_names = check_tables_exist()
    new_window = tk.Toplevel(root)
    new_window.title("Update Fields")
    
    selected_table = tk.StringVar(new_window)
    selected_table.set("Select Table")  # Set the default value

    table_dropdown = tk.OptionMenu(new_window, selected_table, *table_names, command=lambda selected: open_table_selection_window(selected, new_window))
    table_dropdown.pack()

def open_table_selection_window(selected, new_window):
    query = f"SELECT * FROM {selected}"
    df = execute_query_to_dataframe(query)
    show_update_fields(df, selected, new_window)

#Built-in Queries
def total_profits():
    try:
        c.execute("SELECT SUM(amount) FROM payments WHERE cID IS NOT NULL")
        result = c.fetchone()[0]
        tk.messagebox.showinfo("Total Profits", f"Total Profits: ${result}")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error executing Total Profits command: {e}")

def total_costs():
    try:
        c.execute("SELECT SUM(amount) FROM payments WHERE eID IS NOT NULL")
        result = c.fetchone()[0]
        tk.messagebox.showinfo("Total Costs", f"Total Costs: ${result}")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error executing Total Costs command: {e}")

def veh_loc():
    try:
        query = """
        SELECT make, model, address
        FROM vehicle
        INNER JOIN location ON location.lID = vehicle.lID
        WHERE availability = 1
        ORDER BY address DESC;
        """
        df = execute_query_to_dataframe(query)
        if df is not None:
            show_query_result(df, "Vehicle Location")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error executing Vehicle Location query: {e}")

def veh_avail():
    try:
        query = """
        SELECT make, model
        FROM vehicle
        WHERE availability = 1
        """
        df = execute_query_to_dataframe(query)
        if df is not None:
            show_query_result(df, "Vehicle Availability")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error executing Vehicle Availability query: {e}")

def verify_history():
    try:
        query = """
        SELECT make, model, availability, rh.* FROM vehicle v
        INNER JOIN rental_history rh on rh.vID = v.vID
        WHERE (return_date IS NULL OR return_loc IS NULL) AND availability = 1
        """
        df = execute_query_to_dataframe(query)
        if df is not None:
            show_query_result(df, "Verify History - Bad Entries")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error executing Verify History query: {e}")




# Main code
if __name__ == "__main__":
    dbFilePath = os.path.abspath(dbFile)
    cte = check_tables_exist()
    print("File Path: ", dbFilePath)
    print("File Exists: ", os.path.exists(dbFilePath))
    if not os.path.exists(dbFile):
        create_tables()

    check_tables_exist()

    # Create the main window
    root = tk.Tk()
    root.title("Rental Unit")

    menubar = tk.Menu(root)
    root.config(menu=menubar)
    sql_menu= tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Built-in Commands", menu=sql_menu)

    sql_commands = [
        ("Total Profits", total_profits),
        ("Total Costs", total_costs),
        ("Vehicle Availability", veh_avail),
        ("Verify History", verify_history),
        ("Vehicle Locations", veh_loc),
        ("Insert Test Data",insert_test_data)
    ]

    # Add commands to the menu
    for label, command in sql_commands:
        if command:
            sql_menu.add_command(label=label, command=command)
        else:
            # If no command is provided, disable the menu item
            sql_menu.add_command(label=label, state="disabled")

    # Create and place GUI components

    left_frame = tk.Frame(root, width=200, height=400, bg="light green")
    left_frame.grid(row=0, column=0, padx=10, pady=10)
    
    center_frame = tk.Frame(root, width=400, height=400, bg="light gray")
    center_frame.grid(row=0, column=1, padx=10, pady=10)
    
    right_frame = tk.Frame(root, width=200, height=400)
    right_frame.grid(row=0, column=2, padx=10, pady=10)

    image = Image.open("logo.jpg")
    image = ImageTk.PhotoImage(image)

    logo_label = tk.Label(center_frame, image=image)
    logo_label.pack()


    # Right-Side buttons
    open_window_button = tk.Button(right_frame, text="Open Table Selection Window", command=open_table_selection_window)
    open_window_button.pack(fill="x")
    
    open_insert_window_button = tk.Button(right_frame, text="Open Insert Window", command=open_insert_window)
    open_insert_window_button.pack(fill="x")
    
    open_update_window_button = tk.Button(right_frame, text="Open Update Window", command=open_update_window)
    open_update_window_button.pack(fill="x")

    # Start the GUI event loop
    root.mainloop()

    # Close the database connection when done
    conn.close()
