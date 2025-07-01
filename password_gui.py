import re
import tkinter as tk

def check_password_strength():
    password = entry.get()
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        strength += 1
    else:
        suggestions.append("Add special characters (e.g., @, #, $, etc.)")

    if strength <= 2:
        result = "❌ Weak"
    elif strength == 3 or strength == 4:
        result = "⚠️ Medium"
    else:
        result = "✅ Strong"

    output_text = f"Password Strength: {result}"
    if suggestions:
        output_text += "\n\nSuggestions:\n" + "\n".join(f"- {s}" for s in suggestions)

    result_label.config(text=output_text)


def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_button.config(text='👁️ Show')
    else:
        entry.config(show='')
        toggle_button.config(text='🙈 Hide')


# GUI Setup
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("430x360")
root.config(bg="#f0f4f7")

# Heading
heading = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"), bg="#f0f4f7")
heading.pack(pady=10)

# Frame for password input and toggle
frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

# Entry field (password input)
entry = tk.Entry(frame, width=28, font=("Arial", 13), show='*')
entry.pack(side="left", padx=(0, 5))

# Toggle Button (no image needed)
toggle_button = tk.Button(frame, text="👁️ Show", command=toggle_password, bg="#ddd", font=("Arial", 10))
toggle_button.pack(side="left")

# Check Button
check_button = tk.Button(root, text="Check Strength", command=check_password_strength, bg="#28a745", fg="white", font=("Arial", 12))
check_button.pack(pady=5)

# Output Label
result_label = tk.Label(root, text="", font=("Arial", 11), bg="#f0f4f7", justify="left", wraplength=400)
result_label.pack(pady=10)

# Run app
root.mainloop()
