
import openai
import time
import tkinter as tk
# Set up the API key
openai.api_key = "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"

messages = []
system_msg = input("RAJIV IKKA Initializing....\n")
messages.append({"role": "system", "content": system_msg})

print("Hey Riswan, ready for your assistance!")
while input != "quit()":
    message = input('Ask:')
    if message=='quit()':
        print('Thank You! Call me anytime for my assistance')
        time.sleep(2)
        break
    elif message=='--gui':
        class ChatBot(tk.Frame):
            def __init__(self, master=None):
                super().__init__(master, bg='#222831')
                self.master = master
                self.master.title("RAJIV IKKA BOT")
                self.create_widgets()
                self.messages = []
                self.system_msg = "RAJIV IKKA Initializing...."
                self.messages.append({"role": "system", "content": self.system_msg})
                self.update_chat()

            def create_widgets(self):
                self.chatlog = tk.Text(self.master, state="disabled", bg='#393e46', fg='#eeeeee', font=('Helvetica', 12))
                self.chatlog.pack(fill="both", expand=True)
                self.chatinput = tk.Entry(self.master, bg='#393e46', fg='#eeeeee', font=('Helvetica', 12))
                self.chatinput.pack(side="bottom", fill="x", padx=10, pady=10)
                self.chatinput.bind("<Return>", self.send_message)

            def send_message(self, event):
                message = self.chatinput.get()
                self.chatinput.delete(0, "end")
                self.messages.append({"role": "user", "content": message})
                if message == "quit()":
                    self.system_msg = "Thank you for using RAJIV IKKA BOT. Goodbye!"
                    self.messages.append({"role": "system", "content": self.system_msg})
                    self.update_chat()
                    time.sleep(3)
                    self.master.destroy()
                else:
                        response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=self.messages)
                        reply = response["choices"][0]["message"]["content"]
                        self.messages.append({"role": "assistant", "content": reply})
                        self.update_chat()

            def update_chat(self):
                self.chatlog.config(state="normal")
                self.chatlog.delete("1.0", "end")
                for message in self.messages:
                    if message["role"] == "system":
                        self.chatlog.insert("end", "RAJIV IKKA: " + message["content"] + "\n", "system")
                    elif message["role"] == "user":
                        self.chatlog.insert("end", "You: " + message["content"] + "\n", "user")
                    elif message["role"] == "assistant":
                        self.chatlog.insert("end", "RAJIV IKKA: " + message["content"] + "\n", "assistant")
                self.chatlog.config(state="disabled")
                self.chatlog.see("end")

                self.chatlog.tag_config("system", foreground="#FF5555")
                self.chatlog.tag_config("user", foreground="#00ADB5")
                self.chatlog.tag_config("assistant", foreground="#00B2A9")

        if __name__ == "__main__":
            root = tk.Tk()
            chatbot = ChatBot(root)
            chatbot.pack(fill="both", expand=True)
            root.mainloop()

    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + 'Reply:'+reply + "\n")

