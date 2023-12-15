import tkinter as tk
from langdetect import detect

class LanguageDetectorApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Language Detector")
        
        self.label = tk.Label(root, text="Enter a Text: ")
        self.label.pack(pady=10)
        
        self.text_entry = tk.Entry(root, width=30)
        self.text_entry.pack(pady=10)

        self.detect_button = tk.Button(root, text="Detect Language", command=self.detect_language)
        self.detect_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
        
    def detect_language(self):
       text_to_detect = self.text_entry.get()
       
       try:
            language_code = detect(text_to_detect)
            language_name = self.get_language_name(language_code)

            result_text = f"The detected language is: {language_code} ({language_name})"
       except Exception as e:
            result_text = f"Error: {str(e)}"

       self.result_label.config(text=result_text)
    
    def get_language_name(self, language_code):
        # Add more language codes and names as needed
        language_names = {
           'Arabic': 'Ar',
           'English':'en',
           'Spanish':'es',
           'French': 'fr',
           'German': 'de',
            # Add more languages as needed
        }
        return language_names.get(language_code)
if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageDetectorApp(root)
    root.mainloop()