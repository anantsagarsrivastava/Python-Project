<h1>Smart Attendance System (S.A.S.)</h1>
<h3>Automated, Real-Time Attendance using Face Recognition</h3>
<p>
    The Smart Attendance System (S.A.S.) automates attendance by detecting and recognizing faces from a live camera feed.
    It logs attendance with accurate timestamps, prevents proxy attendance, and reduces manual work. Ideal for schools and workplaces.
</p>

<hr>

<h2>Key Features</h2>
<ul>
    <li><strong>Real-Time Face Detection:</strong> Detects faces using OpenCV.</li>
    <li><strong>High-Accuracy Recognition:</strong> Identifies individuals with face recognition library.</li>
    <li><strong>Automated Time Stamping:</strong> Records attendance instantly.</li>
    <li><strong>Proxy Prevention:</strong> Only registered users can mark attendance.</li>
    <li><strong>Data Management:</strong> Saves records in CSV/database.</li>
    <li><strong>Simple Enrollment:</strong> Capture a few images to register users.</li>
</ul>

<hr>

<h2>Technology Stack</h2>
<ul>
    <li>Python 3.8+</li>
    <li>OpenCV</li>
    <li>Face Recognition</li>
    <li>Pandas</li>
</ul>

<hr>

<h2>Architecture Workflow</h2>
<h3>1. Enrollment (Pre-encoding):</h3>
<p>User images are processed using <code>preencoding.py</code> to generate <code>encodings.pkl</code>.</p>

<h3>2. Attendance Logging:</h3>
<p><code>main.py</code> captures live video, compares faces, and logs the timestamp in a CSV file (e.g., <code>2025-11-27.csv</code>).</p>

<hr>

<h2>Installation Guide</h2>

<h3>Step 1: Clone the Repository</h3>
<pre><code>git clone https://github.com/YourUsername/smart-attendance-system.git
cd smart-attendance-system
</code></pre>

<h3>Step 2: Create and Activate Virtual Environment (Optional)</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate     # Linux/macOS
.\venv\Scripts\activate      # Windows
</code></pre>

<h3>Step 3: Install Required Packages</h3>
<pre><code>pip install -r requirements.txt
# If no requirements:
# pip install opencv-python numpy pandas face_recognition
</code></pre>

<hr>

<h2>Usage</h2>

<h3>1. Generate Face Encodings</h3>
<pre><code>python preencoding.py</code></pre>
<p><em>Run only when adding or removing user photos.</em></p>

<h3>2. Start Attendance System</h3>
<pre><code>python main.py</code></pre>

<hr>

<h2>Project Structure</h2>
<pre><code>smart-attendance-system/
├── main.py              # Real-time attendance logging
├── preencoding.py       # Generates encodings
├── encodings.pkl        # Stored facial data
├── photos/              # User images
├── [DATE].csv           # Attendance log
└── requirements.txt     # Dependencies
</code></pre>

<hr>

<h2>Contributing & License</h2>
<p>Contributions are welcome! Distributed under the <strong>MIT License</strong>.</p>

<hr>

<h2>Contact</h2>
<p><strong>Maintainer:</strong> your.email@example.com</p>
<p><a href="https://github.com/YourUsername/smart-attendance-system" target="_blank">
https://github.com/YourUsername/smart-attendance-system</a></p>

<hr>

<p><em>© 2025 Smart Attendance System. Built with Python and OpenCV.</em></p>
