import tkinter as tk
import tkinter.messagebox as messagebox

# Function to execute a SQL command
def execute_sql_command(conn, c, sql_command):
    try:
        c.execute(sql_command)
        conn.commit()
        tk.messagebox.showinfo("Success", "SQL command executed successfully!")
    except Exception as e:
        tk.messagebox.showerror("Error", f"Error executing SQL command: {e}")

# Function to create a new SQL command window
def open_sql_command_window(conn, c, sql_command):
    new_window = tk.Toplevel()
    new_window.title("Execute SQL Command")

    label = tk.Label(new_window, text="Enter SQL command:")
    label.pack()

    sql_entry = tk.Entry(new_window)
    sql_entry.pack()

    def execute_command():
        command = sql_entry.get()
        try:
            c.execute(command)
            conn.commit()
            tk.messagebox.showinfo("Success", "SQL command executed successfully!")
            new_window.destroy()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error executing SQL command: {e}")

    execute_button = tk.Button(new_window, text="Execute", command=execute_command)
    execute_button.pack()


def total_profits(conn, c):
    try:
        c.execute("SELECT SUM(amount) FROM payments WHERE cID IS NOT NULL")
        result = c.fetchone()[0]
        return result
    except Exception as e:
        raise e
