import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load model and features
model = joblib.load("bankruptcy_model.pkl")
features = joblib.load("features.pkl")

root = tk.Tk()
root.title("Bankruptcy Prediction System")
root.geometry("500x600")

entries = {}

for feature in features:
    tk.Label(root, text=feature).pack()
    entry = tk.Entry(root)
    entry.pack()
    entries[feature] = entry

def predict():
    try:
        values = [float(entries[f].get()) for f in features]
        values = np.array(values).reshape(1, -1)

        result = model.predict(values)[0]

        if result == 1:
            messagebox.showinfo("Result", "⚠️ Bankruptcy Risk")
        else:
            messagebox.showinfo("Result", "✅ Safe Company")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

tk.Button(root, text="Predict", command=predict).pack(pady=20)

root.mainloop()
