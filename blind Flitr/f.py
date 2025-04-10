import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# فلاتر لعمى الألوان
def apply_protanopia_filter(frame):
    transform = np.array([
        [0.567, 0.433, 0],
        [0.558, 0.442, 0],
        [0,     0.242, 0.758]
    ])
    return np.clip(frame @ transform.T, 0, 255).astype(np.uint8)

def apply_deuteranopia_filter(frame):
    transform = np.array([
        [0.625, 0.375, 0],
        [0.7,   0.3,   0],
        [0,     0.3,   0.7]
    ])
    return np.clip(frame @ transform.T, 0, 255).astype(np.uint8)

# تشغيل الفيديو مع الفلتر المختار
def play_video(filter_type, video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("فشل فتح الفيديو")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        frame = frame.astype(np.float32)

        if filter_type == "Protanopia":
            filtered = apply_protanopia_filter(frame)
        elif filter_type == "Deuteranopia":
            filtered = apply_deuteranopia_filter(frame)
        else:
            filtered = frame.astype(np.uint8)

        cv2.imshow("فيديو معدل - اضغط Q للخروج", filtered)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# اختيار ملف فيديو من الجهاز
def choose_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
    if file_path:
        selected_filter = filter_var.get()
        play_video(selected_filter, file_path)

# واجهة المستخدم
root = tk.Tk()
root.title("فلتر فيديو لعمى الألوان")
root.geometry("400x200")

ttk.Label(root, text="اختاري نوع الفلتر:").pack(pady=10)

filter_var = tk.StringVar()
filter_dropdown = ttk.Combobox(root, textvariable=filter_var, state="readonly")
filter_dropdown['values'] = ("Protanopia", "Deuteranopia")
filter_dropdown.current(0)
filter_dropdown.pack(pady=5)

ttk.Button(root, text="اختاري فيديو وشغّليه 🎬", command=choose_video).pack(pady=20)

root.mainloop()
