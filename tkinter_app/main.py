import json
import subprocess
import tkinter as tk
from datetime import datetime
from tkinter import ttk

import paho.mqtt.client as mqtt

from configs import db, MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_TOPIC_SCRIPT_UPDATES
from schema import ExecutionLog, Script


class ScriptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Script App")

        self.script_name_label = tk.Label(root, text="Script Name:")
        self.script_name_label.pack(padx=10, pady=5)

        self.script_name_entry = tk.Entry(root, width=40)
        self.script_name_entry.pack(padx=10, pady=5)

        self.script_listbox = ttk.Treeview(root, columns=("Script Name"))
        self.script_listbox.heading("#1", text="Script Name")
        self.script_listbox.pack(padx=10, pady=5)
        self.script_listbox.bind("<<TreeviewSelect>>", self.on_script_select)

        self.script_text = tk.Text(root, height=10, width=40)
        self.script_text.pack(padx=10, pady=5)

        self.create_button = tk.Button(root, text="Create Script", command=self.create_script)
        self.create_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Script", command=self.update_script)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Script", command=self.delete_script)
        self.delete_button.pack(pady=5)

        self.run_button = tk.Button(root, text="Run Script", command=self.run_script)
        self.run_button.pack(pady=5)

        self.selected_script = None

        self.load_scripts()

    def load_scripts(self):
        scripts = Script.select()
        for script in scripts:
            self.script_listbox.insert("", "end", text=script.name)

    @staticmethod
    def publish_script_update(script_id, action):
        client = mqtt.Client()
        client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT)

        data = {
            "id": script_id,
            "action": action
        }
        message = json.dumps(data)
        client.publish(MQTT_TOPIC_SCRIPT_UPDATES, message)

        print(f'Published message :: {message}')

        client.disconnect()

    def on_script_select(self, event):
        selected_items = self.script_listbox.selection()
        if selected_items:
            selected_item = selected_items[0]
            name = self.script_listbox.item(selected_item, "text")
            if name:
                self.selected_script = Script.get(Script.name == name)
                self.script_name_entry.delete(0, tk.END)  # Clear the script name entry
                self.script_name_entry.insert(0, self.selected_script.name)  # Set script name
                self.script_text.delete("1.0", "end")
                self.script_text.insert("1.0", self.selected_script.content)

    def create_script(self):
        name = self.script_name_entry.get().strip()
        content = self.script_text.get("1.0", "end-1c").strip()
        if name and content:
            script = Script.create(name=name, content=content)
            self.refresh_script_list()
            self.script_name_entry.delete(0, tk.END)  # Clear the script name entry
            self.script_text.delete("1.0", "end")
            self.publish_script_update(script.id, "create")
            self.selected_script = None

    def update_script(self):
        if self.selected_script:
            name = self.script_name_entry.get()  # Get updated name from the entry
            content = self.script_text.get("1.0", "end-1c")  # Corrected
            if content:
                self.selected_script.name = name  # Update the name
                self.selected_script.content = content
                self.selected_script.save()
                self.refresh_script_list()
                self.publish_script_update(self.selected_script.id, "update")

    def delete_script(self):
        if self.selected_script:
            self.selected_script.delete_instance(recursive=True)
            self.refresh_script_list()
            self.script_text.delete("1.0", "end")
            self.publish_script_update(self.selected_script.id, "delete")

    def run_script(self):
        if self.selected_script:
            content = self.selected_script.content
            try:
                start_time = datetime.now()
                result = subprocess.run(["python", "-c", content], capture_output=True, text=True)
                end_time = datetime.now()
                execution_time = (end_time - start_time).total_seconds()

                output = result.stdout
                if result.returncode != 0:
                    output = f"Error: {result.stderr}"

                execution_log = ExecutionLog.create(
                    script=self.selected_script,
                    output=output,
                    execution_started_at=start_time,
                    execution_completed_at=end_time,
                    execution_time=execution_time
                )
                self.publish_script_update(execution_log.id, "execute")
                self.script_name_entry.delete(0, tk.END)
                self.selected_script = None
            except Exception as e:
                output = f"Error: {str(e)}"

            self.refresh_script_list()
            self.script_text.delete("1.0", "end")

    def refresh_script_list(self):
        self.script_listbox.delete(*self.script_listbox.get_children())
        scripts = Script.select()
        for script in scripts:
            self.script_listbox.insert("", "end", text=script.name)


if __name__ == "__main__":
    db.connect()
    # db.create_tables([Script, ExecutionLog], safe=True)
    tk_root = tk.Tk()
    app = ScriptApp(tk_root)
    tk_root.mainloop()
