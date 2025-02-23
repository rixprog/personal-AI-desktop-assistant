Here's a structured README for the **Personal AI Desktop Assistant** repository:  

---

# **Personal AI Desktop Assistant**  

An AI-powered desktop assistant using OpenAI's GPT model, designed to assist users with various tasks via a command-line interface (CLI) or graphical user interface (GUI).  

## **Features**  
✅ Natural language conversation with AI  
✅ CLI and GUI support  
✅ Uses OpenAI API for responses  
✅ Lightweight and easy to set up  

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/rixprog/personal-AI-desktop-assistant.git
cd personal-AI-desktop-assistant
```

### **2. Install Dependencies**  
Ensure Python is installed, then install required packages:  
```bash
pip install -r requirements.txt
```

### **3. Set Up OpenAI API Key**  
Get your API key from OpenAI and set it as an environment variable:  
```bash
export OPENAI_API_KEY='your-api-key-here'
```
(Replace `'your-api-key-here'` with your actual API key.)  

## **Usage**  

### **Command-Line Mode**  
Run the assistant in CLI mode:  
```bash
python gpt.py
```
To exit, type:  
```python
quit()
```

### **GUI Mode**  
Launch with a graphical interface:  
```bash
python gpt.py --gui
```

## **Contributing**  
Contributions are welcome! Fork the repo and submit a pull request.  

## **License**  
This project is licensed under the MIT License.  

---

