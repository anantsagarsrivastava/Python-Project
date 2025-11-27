<div style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 900px; margin: auto;">

<h1 style="color:#2563eb;">📸 Smart Attendance System (S.A.S.)</h1>
<p><strong>🎯 Automated real-time attendance tracking using Face Recognition & OpenCV</strong></p>

<p>
    <span style="background:#e1f5fe; padding:4px 8px; border-radius:4px;">🐍 Python 3.8+</span>
    <span style="background:#e8f5e9; padding:4px 8px; border-radius:4px;">📷 OpenCV</span>
    <span style="background:#fffde7; padding:4px 8px; border-radius:4px;">📄 MIT License</span>
</p>

<hr>

<h2 style="color:#2563eb;">🧠 What is S.A.S.?</h2>
<p>
    The <strong>Smart Attendance System</strong> uses real-time facial recognition to detect individuals and automatically log attendance with timestamps. Designed for <strong>schools, companies, and labs</strong>, it prevents proxy attendance and reduces manual work.
</p>

<hr>

<h2 style="color:#2563eb;">✨ Key Features</h2>
<table style="width:100%; border-collapse: collapse;">
<tr>
    <th style="text-align:left; padding:8px; background:#2563eb; color:white;">🚀 Feature</th>
    <th style="text-align:left; padding:8px; background:#2563eb; color:white;">📄 Description</th>
</tr>
<tr>
    <td style="padding:8px;">👁️ Face Detection</td>
    <td style="padding:8px;">Detects faces instantly using OpenCV.</td>
</tr>
<tr>
    <td style="padding:8px;">🧠 Recognition</td>
    <td style="padding:8px;">Identifies registered users with facial encodings.</td>
</tr>
<tr>
    <td style="padding:8px;">⏱️ Timestamp Logging</td>
    <td style="padding:8px;">Stores date and time automatically.</td>
</tr>
<tr>
    <td style="padding:8px;">🔒 Proxy Prevention</td>
    <td style="padding:8px;">Ensures attendance is marked only by the correct person.</td>
</tr>
<tr>
    <td style="padding:8px;">📊 Data Storage</td>
    <td style="padding:8px;">Saves records in CSV or databases.</td>
</tr>
<tr>
    <td style="padding:8px;">📷 Simple Enrollment</td>
    <td style="padding:8px;">Register new users by adding their photos.</td>
</tr>
</table>

<hr>

<h2 style="color:#2563eb;">🧪 Technology Stack</h2>
<ul>
    <li>🐍 <strong>Python 3.8+</strong></li>
    <li>🎥 <strong>OpenCV</strong> – Camera and image processing</li>
    <li>🧬 <strong>face_recognition</strong> – Face matching</li>
    <li>📦 <strong>Pandas</strong> – Data handling</li>
</ul>

<hr>

<h2 style="color:#2563eb;">⚙️ Installation</h2>

<h3>📥 Step 1: Clone Repository</h3>
<pre><code>git clone https://github.com/YourUsername/smart-attendance-system.git
cd smart-attendance-system
</code></pre>

<h3>📦 Step 2: Setup Virtual Environment</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate     # macOS/Linux
.\venv\Scripts\activate      # Windows
</code></pre>

<h3>🔧 Step 3: Install Dependencies</h3>
<pre><code>pip install -r requirements.txt
# Or manually
pip install opencv-python numpy pandas face_recognition
</code></pre>

<hr>

<h2 style="color:#2563eb;">🏃 Usage</h2>

<h3>🖼️ 1. Generate Face Encodings</h3>
<pre><code>python preencoding.py</code></pre>
<p><em>Run only when adding/removing user images.</em></p>

<h3>📸 2. Start Attendance System</h3>
<pre><code>python main.py</code></pre>

<hr>

<h2 style="color:#2563eb;">📁 Project Structure</h2>
<pre><code>smart-attendance-system/
├── main.py              # Real-time attendance
├── preencoding.py       # Generates face encodings
├── encodings.pkl        # Facial data
├── photos/              # User images
├── YYYY-MM-DD.csv       # Attendance logs
└── requirements.txt     # Dependencies
</code></pre>

<hr>

<h2 style="color:#2563eb;">📸 Example Output</h2>
<table style="width:100%; border-collapse: collapse;">
<tr>
    <th style="text-align:left; padding:8px; background:#2563eb; color:white;">Name</th>
    <th style="text-align:left; padding:8px; background:#2563eb; color:white;">Time</th>
    <th style="text-align:left; padding:8px; background:#2563eb; color:white;">Status</th>
</tr>
<tr>
    <td style="padding:8px;">John Doe</td>
    <td style="padding:8px;">09:05 AM</td>
    <td style="padding:8px;">✔️ Present</td>
</tr>
<tr>
    <td style="padding:8px;">Jane Smith</td>
    <td style="padding:8px;">09:07 AM</td>
    <td style="padding:8px;">✔️ Present</td>
</tr>
</table>

<hr>

<h2 style="color:#2563eb;">🚀 Future Enhancements</h2>
<ul>
    <li>📱 Mobile App Integration</li>
    <li>🌐 Web Dashboard</li>
    <li>🔔 Email/WhatsApp Notifications</li>
    <li>🧠 AI-based detection improvements</li>
</ul>

<hr>

<h2 style="color:#2563eb;">🤝 Contributing</h2>
<pre><code>git checkout -b feature-branch
git commit -m "Add new feature"
git push origin feature-branch
</code></pre>
<p>Pull requests are welcome!</p>

<hr>

<h2 style="color:#2563eb;">📜 License</h2>
<p>📝 This project is licensed under the <strong>MIT License</strong>.</p>

<hr>

<h2 style="color:#2563eb;">📞 Contact</h2>
<p><strong>Maintainer:</strong> Your Name</p>
<p>📧 <a href="mailto:your.email@example.com">your.email@example.com</a></p>
<p>🔗 <a href="https://github.com/YourUsername">GitHub Profile</a></p>

<hr>

<p style="text-align:center; color:#6b7280; font-size:14px;">
✨ © 2025 Smart Attendance System — Built with AI, OpenCV & Passion 💡
</p>

</div>
