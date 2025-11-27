<div style="font-family: Arial, sans-serif; line-height: 1.6;">

<h1 style="color:#2563eb;">Smart Attendance System (S.A.S.)</h1>
<h3 style="color:#555;">Automated, Real-Time Attendance using Face Recognition</h3>
<p>
    The <strong>Smart Attendance System</strong> automates attendance using facial recognition and real-time camera feed.
    It logs attendance with timestamps, enhances accuracy, prevents proxy entries, and reduces manual workload. 
    Ideal for academic institutions and workplaces.
</p>

<hr>

<h2 style="color:#2563eb;">🚀 Key Features</h2>
<ul>
    <li><strong style="color:#10b981;">Real-Time Face Detection:</strong> Detects faces using OpenCV.</li>
    <li><strong style="color:#10b981;">High-Accuracy Recognition:</strong> Identifies registered individuals.</li>
    <li><strong style="color:#10b981;">Automated Time Stamping:</strong> Logs attendance instantly.</li>
    <li><strong style="color:#10b981;">Proxy Prevention:</strong> Ensures only the actual person can mark attendance.</li>
    <li><strong style="color:#10b981;">Data Management:</strong> Stores attendance in CSV or database.</li>
    <li><strong style="color:#10b981;">Easy Enrollment:</strong> Add new users by saving a few photos.</li>
</ul>

<hr>

<h2 style="color:#2563eb;">🧪 Technology Stack</h2>
<ul>
    <li><strong>Python 3.8+</strong></li>
    <li><strong>OpenCV</strong> – Live camera & image processing</li>
    <li><strong>face_recognition</strong> – Face matching</li>
    <li><strong>Pandas</strong> – Attendance storage</li>
</ul>

<hr>

<h2 style="color:#2563eb;">🔁 Architecture Workflow</h2>
<h3>1️⃣ Enrollment (Pre-encoding)</h3>
<p>Run <code style="background:#f3f4f6;">preencoding.py</code> to scan user photos and generate <code style="background:#f3f4f6;">encodings.pkl</code>.</p>

<h3>2️⃣ Attendance Logging</h3>
<p><code style="background:#f3f4f6;">main.py</code> captures live video, compares faces, and records attendance.</p>

<hr>

<h2 style="color:#2563eb;">⚙️ Installation</h2>

<h3>📥 Step 1: Clone Repository</h3>
<pre><code>git clone https://github.com/YourUsername/smart-attendance-system.git
cd smart-attendance-system
</code></pre>

<h3>🔧 Step 2: Create Virtual Environment (Recommended)</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate     # macOS/Linux
.\venv\Scripts\activate      # Windows
</code></pre>

<h3>📦 Step 3: Install Dependencies</h3>
<pre><code>pip install -r requirements.txt
# Or manually:
# pip install opencv-python numpy pandas face_recognition
</code></pre>

<hr>

<h2 style="color:#2563eb;">🏃 Usage</h2>

<h3>1️⃣ Generate Face Encodings</h3>
<pre><code>python preencoding.py</code></pre>

<h3>2️⃣ Start Attendance System</h3>
<pre><code>python main.py</code></pre>

<hr>

<h2 style="color:#2563eb;">📁 Project Structure</h2>
<pre><code>smart-attendance-system/
├── main.py              # Live attendance logging
├── preencoding.py       # Generate face encodings
├── encodings.pkl        # Stored facial data
├── photos/              # User images
├── [DATE].csv           # Daily attendance log
└── requirements.txt     # Libraries
</code></pre>

<hr>

<h2 style="color:#2563eb;">🤝 Contributing & License</h2>
<p>🛠️ Contributions welcome!<br>
📜 Licensed under the <strong>MIT License</strong>.</p>

<hr>

<h2 style="color:#2563eb;">📞 Contact</h2>
<p><strong>Maintainer:</strong> anantsagar064@gamil.com</p>
<a href="https://github.com/YourUsername/Python-Project" target="_blank">GitHub Repository</a>

<hr>

<p style="text-align:center; color:#6b7280;">
✨ © 2025 Smart Attendance System. Built with Python, OpenCV & AI Innovation.
</p>

</div>
