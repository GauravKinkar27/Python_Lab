"""
Typing Speed Test Application
A complete GUI application to test and improve typing speed
"""

import tkinter as tk
from tkinter import messagebox, ttk
import time
import random
import json
import os
from datetime import datetime

class TypingSpeedTest:
    """Main application class for Typing Speed Test"""
    
    def __init__(self, root):
        """Constructor - Initialize the application"""
        self.root = root
        self.root.title("Typing Speed Test Application")
        self.root.geometry("900x700")
        self.root.configure(bg="#2c3e50")
        
        # Application variables
        self.sample_text = ""
        self.user_input = ""
        self.start_time = 0
        self.end_time = 0
        self.timer_running = False
        self.time_left = 60  # 60 seconds default
        self.total_time = 60
        self.high_scores = []
        
        # Load sample texts and high scores
        self.load_sample_texts()
        self.load_high_scores()
        
        # Create GUI elements
        self.create_widgets()
        
        # Select random text to start
        self.select_random_text()
    
    def load_sample_texts(self):
        """Load sample texts for typing test"""
        self.sample_texts = {
            "Easy": [
                "The quick brown fox jumps over the lazy dog.",
                "Python is a great programming language for beginners.",
                "Practice makes perfect when learning to type faster.",
                "The sun rises in the east and sets in the west.",
                "Coding is fun and helps solve real world problems."
            ],
            "Medium": [
                "Artificial intelligence is transforming the way we live and work in modern society.",
                "The development of quantum computing could revolutionize science and technology.",
                "Learning to type quickly requires consistent practice and proper finger placement.",
                "Programming languages like Python and JavaScript are widely used in industry.",
                "The Internet of Things connects everyday devices to the digital world."
            ],
            "Hard": [
                "Machine learning algorithms enable computers to learn from data without being explicitly programmed for specific tasks, making them invaluable for complex problem-solving scenarios.",
                "Blockchain technology provides a decentralized and secure method for recording transactions across multiple computers, ensuring transparency and preventing data tampering.",
                "Cloud computing offers on-demand access to computing resources including servers, storage, databases, networking, and software over the internet with pay-as-you-go pricing."
            ]
        }
    
    def load_high_scores(self):
        """Load high scores from file"""
        try:
            if os.path.exists("typing_scores.json"):
                with open("typing_scores.json", "r") as f:
                    self.high_scores = json.load(f)
            else:
                self.high_scores = []
        except Exception as e:
            print(f"Error loading scores: {e}")
            self.high_scores = []
    
    def save_high_scores(self):
        """Save high scores to file"""
        try:
            # Keep only top 10 scores
            self.high_scores.sort(key=lambda x: x['wpm'], reverse=True)
            self.high_scores = self.high_scores[:10]
            with open("typing_scores.json", "w") as f:
                json.dump(self.high_scores, f, indent=2)
        except Exception as e:
            print(f"Error saving scores: {e}")
    
    def create_widgets(self):
        """Create all GUI widgets"""
        
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#2c3e50")
        title_frame.pack(pady=10)
        
        title_label = tk.Label(title_frame, text="⚡ TYPING SPEED TEST ⚡", 
                               font=("Arial", 24, "bold"), 
                               fg="#f1c40f", bg="#2c3e50")
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Test your typing speed and accuracy", 
                                  font=("Arial", 12), fg="#ecf0f1", bg="#2c3e50")
        subtitle_label.pack()
        
        # Difficulty and Timer Frame
        control_frame = tk.Frame(self.root, bg="#2c3e50")
        control_frame.pack(pady=10)
        
        # Difficulty selection
        tk.Label(control_frame, text="Difficulty:", font=("Arial", 11), 
                fg="white", bg="#2c3e50").grid(row=0, column=0, padx=10)
        
        self.difficulty_var = tk.StringVar(value="Medium")
        difficulty_menu = ttk.Combobox(control_frame, textvariable=self.difficulty_var, 
                                        values=["Easy", "Medium", "Hard"], state="readonly")
        difficulty_menu.grid(row=0, column=1, padx=10)
        difficulty_menu.bind("<<ComboboxSelected>>", self.on_difficulty_change)
        
        # Timer selection
        tk.Label(control_frame, text="Time (seconds):", font=("Arial", 11), 
                fg="white", bg="#2c3e50").grid(row=0, column=2, padx=10)
        
        self.time_var = tk.StringVar(value="60")
        time_menu = ttk.Combobox(control_frame, textvariable=self.time_var, 
                                  values=["30", "60", "90", "120"], state="readonly")
        time_menu.grid(row=0, column=3, padx=10)
        time_menu.bind("<<ComboboxSelected>>", self.on_time_change)
        
        # Sample Text Frame
        sample_frame = tk.LabelFrame(self.root, text="📝 Type this text:", 
                                     font=("Arial", 12, "bold"), 
                                     fg="#f1c40f", bg="#34495e", bd=2)
        sample_frame.pack(pady=10, padx=20, fill="both")
        
        self.sample_text_widget = tk.Text(sample_frame, height=5, width=80, 
                                          font=("Consolas", 12), wrap="word",
                                          bg="#ecf0f1", fg="#2c3e50")
        self.sample_text_widget.pack(padx=10, pady=10)
        self.sample_text_widget.config(state="disabled")
        
        # User Input Frame
        input_frame = tk.LabelFrame(self.root, text="✏️ Type here:", 
                                    font=("Arial", 12, "bold"), 
                                    fg="#f1c40f", bg="#34495e", bd=2)
        input_frame.pack(pady=10, padx=20, fill="both")
        
        self.input_text_widget = tk.Text(input_frame, height=8, width=80, 
                                         font=("Consolas", 12), wrap="word",
                                         bg="white", fg="#2c3e50")
        self.input_text_widget.pack(padx=10, pady=10)
        self.input_text_widget.bind("<KeyRelease>", self.on_key_release)
        self.input_text_widget.config(state="disabled")
        
        # Stats Frame
        stats_frame = tk.Frame(self.root, bg="#2c3e50")
        stats_frame.pack(pady=10)
        
        # Timer display
        self.timer_label = tk.Label(stats_frame, text="⏱️ Time Left: 60s", 
                                    font=("Arial", 16, "bold"), 
                                    fg="#e74c3c", bg="#2c3e50")
        self.timer_label.grid(row=0, column=0, padx=30)
        
        # WPM display
        self.wpm_label = tk.Label(stats_frame, text="📊 WPM: 0", 
                                  font=("Arial", 16, "bold"), 
                                  fg="#2ecc71", bg="#2c3e50")
        self.wpm_label.grid(row=0, column=1, padx=30)
        
        # Accuracy display
        self.accuracy_label = tk.Label(stats_frame, text="🎯 Accuracy: 0%", 
                                       font=("Arial", 16, "bold"), 
                                       fg="#3498db", bg="#2c3e50")
        self.accuracy_label.grid(row=0, column=2, padx=30)
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=15)
        
        self.start_button = tk.Button(button_frame, text="🚀 START TEST", 
                                      font=("Arial", 12, "bold"), 
                                      bg="#27ae60", fg="white", 
                                      padx=20, pady=8,
                                      command=self.start_test)
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.reset_button = tk.Button(button_frame, text="🔄 RESET", 
                                      font=("Arial", 12, "bold"), 
                                      bg="#e67e22", fg="white", 
                                      padx=20, pady=8,
                                      command=self.reset_test)
        self.reset_button.grid(row=0, column=1, padx=10)
        
        self.new_text_button = tk.Button(button_frame, text="📖 NEW TEXT", 
                                         font=("Arial", 12, "bold"), 
                                         bg="#3498db", fg="white", 
                                         padx=20, pady=8,
                                         command=self.select_random_text)
        self.new_text_button.grid(row=0, column=2, padx=10)
        
        self.high_scores_button = tk.Button(button_frame, text="🏆 HIGH SCORES", 
                                            font=("Arial", 12, "bold"), 
                                            bg="#9b59b6", fg="white", 
                                            padx=20, pady=8,
                                            command=self.show_high_scores)
        self.high_scores_button.grid(row=0, column=3, padx=10)
        
        # Result Frame
        self.result_frame = tk.LabelFrame(self.root, text="📈 Results", 
                                          font=("Arial", 12, "bold"), 
                                          fg="#f1c40f", bg="#34495e", bd=2)
        self.result_frame.pack(pady=10, padx=20, fill="both")
        
        self.result_label = tk.Label(self.result_frame, text="Click 'START TEST' to begin", 
                                     font=("Arial", 11), fg="#ecf0f1", 
                                     bg="#34495e", wraplength=800)
        self.result_label.pack(padx=10, pady=10)
    
    def on_difficulty_change(self, event=None):
        """Handle difficulty change"""
        if not self.timer_running:
            self.select_random_text()
    
    def on_time_change(self, event=None):
        """Handle time limit change"""
        if not self.timer_running:
            try:
                self.total_time = int(self.time_var.get())
                self.time_left = self.total_time
                self.timer_label.config(text=f"⏱️ Time Left: {self.time_left}s")
            except:
                pass
    
    def select_random_text(self):
        """Select random text based on difficulty"""
        if not self.timer_running:
            difficulty = self.difficulty_var.get()
            texts = self.sample_texts[difficulty]
            self.sample_text = random.choice(texts)
            self.sample_text_widget.config(state="normal")
            self.sample_text_widget.delete("1.0", tk.END)
            self.sample_text_widget.insert("1.0", self.sample_text)
            self.sample_text_widget.config(state="disabled")
            self.reset_test()
    
    def start_test(self):
        """Start the typing test"""
        if self.timer_running:
            return
        
        # Clear input and enable it
        self.input_text_widget.config(state="normal")
        self.input_text_widget.delete("1.0", tk.END)
        self.input_text_widget.focus_set()
        
        # Reset stats
        self.start_time = time.time()
        self.timer_running = True
        self.time_left = self.total_time
        
        # Update button states
        self.start_button.config(state="disabled", bg="#95a5a6")
        self.new_text_button.config(state="disabled")
        self.reset_button.config(state="normal")
        
        # Start timer
        self.update_timer()
        
        # Update result label
        self.result_label.config(text="⏳ Test in progress... Keep typing!", fg="#f1c40f")
    
    def update_timer(self):
        """Update timer display"""
        if self.timer_running:
            elapsed = time.time() - self.start_time
            self.time_left = max(0, self.total_time - int(elapsed))
            self.timer_label.config(text=f"⏱️ Time Left: {self.time_left}s")
            
            if self.time_left <= 0:
                self.end_test()
            else:
                # Update live WPM and accuracy
                self.update_live_stats()
                self.root.after(1000, self.update_timer)
    
    def update_live_stats(self):
        """Update WPM and accuracy in real-time"""
        user_text = self.input_text_widget.get("1.0", tk.END).strip()
        
        if user_text and self.start_time:
            elapsed_time = time.time() - self.start_time
            if elapsed_time > 0:
                words = len(user_text.split())
                minutes = elapsed_time / 60
                wpm = int(words / minutes) if minutes > 0 else 0
                self.wpm_label.config(text=f"📊 WPM: {wpm}")
                
                correct = 0
                min_len = min(len(user_text), len(self.sample_text))
                for i in range(min_len):
                    if i < len(user_text) and i < len(self.sample_text):
                        if user_text[i] == self.sample_text[i]:
                            correct += 1
                accuracy = int((correct / len(self.sample_text)) * 100) if len(self.sample_text) > 0 else 0
                self.accuracy_label.config(text=f"🎯 Accuracy: {accuracy}%")
    
    def on_key_release(self, event=None):
        """Handle key release events for live stats"""
        if self.timer_running:
            self.update_live_stats()
    
    def end_test(self):
        """End the typing test and calculate results"""
        self.timer_running = False
        self.end_time = time.time()
        
        # Disable input
        self.input_text_widget.config(state="disabled")
        
        # Get user input
        user_text = self.input_text_widget.get("1.0", tk.END).strip()
        
        # Calculate results
        results = self.calculate_results(user_text)
        
        # Display results
        self.display_results(results)
        
        # Save high score if good
        if results['wpm'] > 0:
            self.save_score(results)
        
        # Update button states
        self.start_button.config(state="normal", bg="#27ae60")
        self.new_text_button.config(state="normal")
    
    def calculate_results(self, user_text):
        """Calculate typing test results"""
        # Time taken
        time_taken = self.end_time - self.start_time
        minutes = time_taken / 60
        
        # Word count (standard: 5 characters = 1 word)
        char_count = len(user_text)
        word_count = char_count / 5
        
        wpm = int(word_count / minutes) if minutes > 0 else 0
        
        # Accuracy calculation
        correct_chars = 0
        for i in range(min(len(user_text), len(self.sample_text))):
            if user_text[i] == self.sample_text[i]:
                correct_chars += 1
        
        accuracy = (correct_chars / len(self.sample_text)) * 100 if len(self.sample_text) > 0 else 0
        
        errors = len(self.sample_text) - correct_chars
        
        # Time taken in seconds
        time_seconds = int(time_taken)
        
        return {
            'wpm': wpm,
            'accuracy': round(accuracy, 2),
            'correct_chars': correct_chars,
            'errors': errors,
            'total_chars': len(self.sample_text),
            'time_taken': time_seconds,
            'user_char_count': char_count
        }
    
    def display_results(self, results):
        """Display test results in result frame"""
        result_text = f"""
                          TEST RESULTS                             
                                                                  
   📊 Words Per Minute (WPM):     {results['wpm']} WPM                            
                                                                  
   🎯 Accuracy:                    {results['accuracy']}%                               
                                                                  
   ✅ Correct Characters:          {results['correct_chars']} / {results['total_chars']}                   
                                                                  
   ❌ Errors:                      {results['errors']}                                 
                                                                  
   ⏱️ Time Taken:                  {results['time_taken']} seconds                           
                                                                  
   📝 Characters Typed:            {results['user_char_count']}                                 
                                                                  

        """
        
        # Performance message
        if results['wpm'] >= 80:
            performance = "🏆 EXCELLENT! Professional typist level! 🏆"
        elif results['wpm'] >= 60:
            performance = "🌟 GREAT! Above average speed! 🌟"
        elif results['wpm'] >= 40:
            performance = "👍 GOOD! Keep practicing to improve! 👍"
        elif results['wpm'] >= 20:
            performance = "📈 FAIR! Regular practice will help! 📈"
        else:
            performance = "💪 STARTING! Every expert was once a beginner! 💪"
        
        self.result_label.config(text=result_text + f"\n\n{performance}", 
                                 fg="#2ecc71", justify="left")
    
    def save_score(self, results):
        """Save high score"""
        name = f"User_{len(self.high_scores) + 1}"
        
        score_entry = {
            'name': name,
            'wpm': results['wpm'],
            'accuracy': results['accuracy'],
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'difficulty': self.difficulty_var.get(),
            'time_setting': self.total_time
        }
        
        self.high_scores.append(score_entry)
        self.save_high_scores()
    
    def show_high_scores(self):
        """Display high scores in a new window"""
        scores_window = tk.Toplevel(self.root)
        scores_window.title("🏆 High Scores")
        scores_window.geometry("600x450")
        scores_window.configure(bg="#2c3e50")
        
        title = tk.Label(scores_window, text="🏆 TOP 10 HIGH SCORES 🏆", 
                        font=("Arial", 18, "bold"), fg="#f1c40f", bg="#2c3e50")
        title.pack(pady=10)
        
        # Create treeview for scores
        columns = ("Rank", "Name", "WPM", "Accuracy", "Difficulty", "Date")
        tree = ttk.Treeview(scores_window, columns=columns, show="headings", height=10)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100 if col != "Date" else 150)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(scores_window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        scrollbar.pack(side="right", fill="y", pady=10)
        
        # Sort and display scores
        sorted_scores = sorted(self.high_scores, key=lambda x: x['wpm'], reverse=True)
        
        for i, score in enumerate(sorted_scores[:10], 1):
            tree.insert("", "end", values=(
                i, 
                score['name'], 
                score['wpm'], 
                f"{score['accuracy']}%", 
                score['difficulty'],
                score['date']
            ))
        
        if not self.high_scores:
            no_data = tk.Label(scores_window, text="No high scores yet. Complete a test to appear here!", 
                              font=("Arial", 12), fg="#ecf0f1", bg="#2c3e50")
            no_data.pack(pady=50)
        
        close_button = tk.Button(scores_window, text="Close", command=scores_window.destroy,
                                 bg="#e74c3c", fg="white", font=("Arial", 11, "bold"),
                                 padx=20, pady=5)
        close_button.pack(pady=10)
    
    def reset_test(self):
        """Reset the test without changing text"""
        if self.timer_running:
            return
        
        # Clear input
        self.input_text_widget.config(state="normal")
        self.input_text_widget.delete("1.0", tk.END)
        self.input_text_widget.config(state="disabled")
        
        # Reset timer
        try:
            self.total_time = int(self.time_var.get())
        except:
            self.total_time = 60
        self.time_left = self.total_time
        self.timer_label.config(text=f"⏱️ Time Left: {self.time_left}s")
        
        # Reset stats
        self.wpm_label.config(text="📊 WPM: 0")
        self.accuracy_label.config(text="🎯 Accuracy: 0%")
        
        # Reset result
        self.result_label.config(text="Click 'START TEST' to begin", fg="#ecf0f1")
        
        # Update buttons
        self.start_button.config(state="normal", bg="#27ae60")


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()