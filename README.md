# 🎓 Automated-Attendance-System-OpenCV
An AI-powered facial recognition-based attendance system that automates student identification and absence notifications using machine learning and computer vision.

📸 **Features**
- 🧑‍🎓 Student Registration via Webcam: Users can register by entering their name, roll number, and email. The system captures face images and stores them for training.

- 📷 Real-Time Face Recognition: During attendance, faces are recognized live using a trained model. Attendance is marked automatically.

- 📧 Automatic Email Notification: Absent students are identified and notified via email (configurable).

- 🖥️ User-Friendly GUI (Tkinter): All operations—registration and attendance—can be handled through an intuitive graphical interface.

🛠️ **Tech Stack**
-  Python
-  OpenCV
-  Tkinter
-  Pandas
-  face_recognition or LBPH model
-  SMTP (for email)

🗂️**Project Structure**
📦 Smart-Attendance-System
├── database/                  # Stored face images

├── records.csv               # Registered students info (rollno, name, email)

├── recognition.py            # Face recognition & training logic

├── notification.py           # Sends emails to absentees

├── main.py                   # Main GUI and application logic 

└── card_front.png            # Background image for GUI



![image](https://github.com/user-attachments/assets/c2965188-260c-423a-a15a-d4c56d7a478d)

🧪 **How to Use** 
➕ Register a Student

![image](https://github.com/user-attachments/assets/357cee81-916e-435c-ae83-8235777d4256)

Click Register on the GUI.

Enter Roll Number, Name, and Email.

![image](https://github.com/user-attachments/assets/be2906ac-99bc-4c6f-860e-37fa24183bc2)

The webcam will open to capture face images.

7 face samples will be saved and associated with the user.

✅ Take Attendance
Click Take Attendance.

![image](https://github.com/user-attachments/assets/0e79cff2-96a6-4886-86b8-1126853f5558)

The system will detect and recognize faces in real-time.

![image](https://github.com/user-attachments/assets/f9cd273b-3477-4d4c-bbc0-858eaa7da26d)

Attendance will be marked internally.

Emails will be sent to those who were not recognized during the session.

📨 Email Notification

![image](https://github.com/user-attachments/assets/908ce643-8cc4-497d-a2e0-cda194bf7c33)

The notification.py module compares registered emails with recognized users and sends an alert email to absentees using SMTP (e.g., Gmail).

Note: You may need to enable Less Secure Apps or use an App Password if using Gmail.
