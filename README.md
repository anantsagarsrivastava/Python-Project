<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Attendance System (S.A.S.)</title>
    <!-- Load Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Configure Tailwind for a clean, professional dark mode aesthetic -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        // Using a slightly more vibrant blue
                        'primary-blue': '#3b82f6', 
                        'secondary-gray': '#161b22', // GitHub's standard element background
                        'dark-bg': '#0d1117', // GitHub's standard page background
                        'text-light': '#c9d1d9',
                        'code-bg': '#161b22',
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom scrollbar for a clean look */
        body::-webkit-scrollbar {
            width: 8px;
        }
        body::-webkit-scrollbar-thumb {
            background-color: #3b82f6;
            border-radius: 4px;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0d1117; 
            color: #c9d1d9; 
        }
        .code-block {
            background-color: #161b22; 
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 1.25rem;
            overflow-x: auto;
            white-space: pre-wrap;
            transition: all 0.2s ease-in-out;
        }
        .code-block:hover {
            border-color: #3b82f6; /* Highlight border on hover */
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.2);
        }
        .icon {
            color: #58a6ff; 
        }
        /* Custom class for the header background effect */
        .header-bg {
            background: linear-gradient(180deg, rgba(22, 27, 34, 1) 0%, rgba(13, 17, 23, 1) 100%);
        }
    </style>
</head>

<body class="min-h-screen antialiased">

    <!-- Header Section -->
    <header class="py-16 header-bg shadow-xl border-b border-gray-700">
        <div class="max-w-4xl mx-auto px-4 text-center">
            
            <!-- High-Tech Icon SVG -->
            <div class="mb-4 inline-block p-3 rounded-full bg-primary-blue/20 ring-4 ring-primary-blue/50">
                <svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="text-primary-blue stroke-1 hover:stroke-2 transition-all duration-300">
                    <path d="M21 12c0-4.42-3.58-8-8-8"/>
                    <path d="M12 21c-4.42 0-8-3.58-8-8"/>
                    <path d="M16 12a4 4 0 1 1-8 0 4 4 0 0 1 8 0z"/>
                    <path d="M21 4L14 4"/>
                    <path d="M3 4L10 4"/>
                    <path d="M3 20L10 20"/>
                    <path d="M21 20L14 20"/>
                    <path d="M20 3L20 10"/>
                    <path d="M4 3L4 10"/>
                    <path d="M4 21L4 14"/>
                    <path d="M20 21L20 14"/>
                </svg>
            </div>
            
            <h1 class="text-7xl font-extrabold text-white mb-4">
                Smart Attendance System 
                <span class="text-primary-blue">S.A.S.</span>
            </h1>
            <p class="text-2xl text-text-light font-light mt-4">
                Automated, Real-Time Attendance using Face Recognition
            </p>
        </div>
    </header>

    <!-- Main Content Container with Subtle Shadow -->
    <main class="max-w-4xl mx-auto px-6 py-16 bg-[#0f131a] shadow-2xl shadow-gray-900/50 rounded-xl">

        <!-- Introduction -->
        <section class="mb-16 border-b border-gray-800 pb-10">
            <p class="text-xl leading-relaxed text-gray-400">
                The Smart Attendance System (S.A.S.) is an innovative solution designed to modernize and automate the traditional attendance process. Leveraging the power of Computer Vision and Deep Learning, this system detects and identifies registered individuals in real-time, instantly logging their presence with accurate timestamps. Ideal for educational institutions and corporate environments, S.A.S. eliminates proxy attendance, drastically reduces administrative load, and provides reliable attendance data.
            </p>
        </section>

        <!-- Key Features -->
        <section class="mb-16">
            <h2 class="text-4xl font-bold mb-10 border-l-4 border-primary-blue pl-4">
                <span class="icon mr-3 text-3xl">✨</span> Key Features
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                
                <!-- Feature Card 1 -->
                <div class="bg-secondary-gray p-6 rounded-xl shadow-lg hover:shadow-primary-blue/30 transition duration-300 transform hover:scale-[1.03] border border-secondary-gray hover:border-primary-blue/50">
                    <div class="text-4xl mb-3">👁️</div>
                    <h3 class="text-xl font-semibold text-white">Real-Time Face Detection</h3>
                    <p class="text-gray-400 mt-2 text-sm">Utilizes OpenCV to detect faces instantly from a webcam or connected camera stream.</p>
                </div>

                <!-- Feature Card 2 -->
                <div class="bg-secondary-gray p-6 rounded-xl shadow-lg hover:shadow-primary-blue/30 transition duration-300 transform hover:scale-[1.03] border border-secondary-gray hover:border-primary-blue/50">
                    <div class="text-4xl mb-3">🧠</div>
                    <h3 class="text-xl font-semibold text-white">High-Accuracy Recognition</h3>
                    <p class="text-gray-400 mt-2 text-sm">Employs a robust face recognition library to accurately identify registered users.</p>
                </div>

                <!-- Feature Card 3 -->
                <div class="bg-secondary-gray p-6 rounded-xl shadow-lg hover:shadow-primary-blue/30 transition duration-300 transform hover:scale-[1.03] border border-secondary-gray hover:border-primary-blue/50">
                    <div class="text-4xl mb-3">⏱️</div>
                    <h3 class="text-xl font-semibold text-white">Automated Time Stamping</h3>
                    <p class="text-gray-400 mt-2 text-sm">Automatically records the attendance time and date upon successful identification.</p>
                </div>

                <!-- Feature Card 4 -->
                <div class="bg-secondary-gray p-6 rounded-xl shadow-lg hover:shadow-primary-blue/30 transition duration-300 transform hover:scale-[1.03] border border-secondary-gray hover:border-primary-blue/50">
                    <div class="text-4xl mb-3">🔒</div>
                    <h3 class="text-xl font-semibold text-white">Proxy Prevention</h3>
                    <p class="text-gray-400 mt-2 text-sm">Ensures only the registered individual can mark attendance, preventing fraudulent check-ins.</p>
                </div>
                
                <!-- Feature Card 5 -->
                <div class="bg-secondary-gray p-6 rounded-xl shadow-lg hover:shadow-primary-blue/30 transition duration-300 transform hover:scale-[1.03] border border-secondary-gray hover:border-primary-blue/50">
                    <div class="text-4xl mb-3">📊</div>
                    <h3 class="text-xl font-semibold text-white">Data Management</h3>
                    <p class="text-gray-400 mt-2 text-sm">Stores attendance records securely, typically in a CSV or simple database for analysis.</p>
                </div>

                <!-- Feature Card 6 -->
                <div class="bg-secondary-gray p-6 rounded-xl shadow-lg hover:shadow-primary-blue/30 transition duration-300 transform hover:scale-[1.03] border border-secondary-gray hover:border-primary-blue/50">
                    <div class="text-4xl mb-3">🛠️</div>
                    <h3 class="text-xl font-semibold text-white">Simple Enrollment</h3>
                    <p class="text-gray-400 mt-2 text-sm">Easy process to register new users by capturing a few image samples.</p>
                </div>
            </div>
        </section>

        <!-- Technology Stack -->
        <section class="mb-16">
            <h2 class="text-4xl font-bold mb-10 border-l-4 border-primary-blue pl-4">
                <span class="icon mr-3 text-3xl">🚀</span> Technology Stack
            </h2>
            <div class="bg-secondary-gray rounded-xl p-8 shadow-xl border border-gray-700">
                <ul class="space-y-4">
                    <li class="flex items-center space-x-4">
                        <span class="text-2xl font-bold w-32 text-primary-blue">Python 3.8+</span>
                        <span class="text-gray-400">- Core programming language, tested with 3.8.</span>
                    </li>
                    <li class="flex items-center space-x-4">
                        <span class="text-2xl font-bold w-32 text-primary-blue">OpenCV</span>
                        <span class="text-gray-400">- Real-time video stream capture and image processing.</span>
                    </li>
                    <li class="flex items-center space-x-4">
                        <span class="text-2xl font-bold w-32 text-primary-blue">Face Rec.</span>
                        <span class="text-gray-400">- Deep learning model for embedding and identifying faces.</span>
                    </li>
                    <li class="flex items-center space-x-4">
                        <span class="text-2xl font-bold w-32 text-primary-blue">Pandas</span>
                        <span class="text-gray-400">- Managing and exporting attendance records (CSV/DataFrames).</span>
                    </li>
                </ul>
            </div>
        </section>
        
        <!-- Architecture Workflow -->
        <section class="mb-16">
            <h2 class="text-4xl font-bold mb-10 border-l-4 border-primary-blue pl-4">
                <span class="icon mr-3 text-3xl">🛠️</span> Architecture Workflow
            </h2>
            <p class="text-gray-400 mb-6 text-lg">
                The system operates in two main modes: Enrollment and Attendance Logging.
            </p>
            <div class="bg-secondary-gray p-8 rounded-xl shadow-xl space-y-6 text-base border border-gray-700">
                <div class="border-b border-gray-700 pb-4">
                    <strong class="text-white text-xl block mb-1">1. Enrollment (Pre-encoding):</strong>
                    <p class="text-gray-300">A user's face is captured, processed, and their unique facial <span class="text-green-400">encoding</span> is generated using <code class="bg-gray-800 text-sm p-1 rounded">preencoding.py</code>. This data is stored in <code class="bg-gray-800 text-sm p-1 rounded">encodings.pkl</code> for fast access.</p>
                </div>
                <div>
                    <strong class="text-white text-xl block mb-1">2. Attendance Logging (Real-time):</strong>
                    <p class="text-gray-300">The live camera feed is continuously monitored by <code class="bg-gray-800 text-sm p-1 rounded">main.py</code>. Detected faces are matched against the stored encodings. Upon positive match, the individual is marked present with a timestamp in the daily CSV report.</p>
                </div>
            </div>
            <!-- Diagram placeholder removed for better flow -->
        </section>

        <!-- Installation Guide -->
        <section class="mb-16">
            <h2 class="text-4xl font-bold mb-10 border-l-4 border-primary-blue pl-4">
                <span class="icon mr-3 text-3xl">⚙️</span> Installation Guide
            </h2>
            
            <h3 class="text-2xl font-semibold text-white mb-4">Prerequisites</h3>
            <ul class="list-disc list-inside ml-4 mb-8 text-gray-400 space-y-2">
                <li>**Python 3.8 (Tested version)** or a newer 3.x release.</li>
                <li>A functional webcam/camera connected to the system.</li>
                <li>`pip` package installer.</li>
            </ul>

            <h3 class="text-2xl font-semibold text-white mt-6 mb-2">Step 1: Clone the Repository</h3>
            <div class="code-block">
<pre><code>git clone [https://github.com/YourUsername/smart-attendance-system.git](https://github.com/YourUsername/smart-attendance-system.git)
cd smart-attendance-system</code></pre>
            </div>

            <h3 class="text-2xl font-semibold text-white mt-8 mb-2">Step 2: Create and Activate a Virtual Environment (Recommended)</h3>
            <div class="code-block">
<pre><code># Create environment
python3 -m venv venv

# Activate environment (Linux/macOS)
source venv/bin/activate

# Activate environment (Windows)
.\venv\Scripts\activate</code></pre>
            </div>

            <h3 class="text-2xl font-semibold text-white mt-8 mb-2">Step 3: Install Required Libraries</h3>
            <div class="code-block">
<pre><code>pip install -r requirements.txt
# If you don't have a requirements.txt, you'll need to install them individually:
# pip install opencv-python numpy pandas face_recognition</code></pre>
            </div>
        </section>

        <!-- Usage -->
        <section class="mb-16">
            <h2 class="text-4xl font-bold mb-10 border-l-4 border-primary-blue pl-4">
                <span class="icon mr-3 text-3xl">🏃</span> Usage
            </h2>
            
            <h3 class="text-3xl font-bold text-white mt-8 mb-4 flex items-center">
                <span class="text-primary-blue mr-3">1.</span> Pre-Setup: Generate Face Encodings
            </h3>
            <p class="text-gray-400 mb-4 text-lg">
                Ensure you have user photos in the `photos` directory (named by their ID/Name). Run this script once to process images and create the high-performance **`encodings.pkl`** file.
            </p>
            <div class="code-block">
<pre><code># This processes images in the 'photos' folder and saves the face data
python preencoding.py</code></pre>
            </div>
            <p class="text-sm italic text-gray-500 mt-2">
                *Tip: Only run this command when adding/removing user photos from the `photos` directory.*
            </p>

            <h3 class="text-3xl font-bold text-white mt-10 mb-4 flex items-center">
                <span class="text-primary-blue mr-3">2.</span> Runtime: Start Attendance System
            </h3>
            <p class="text-gray-400 mb-4 text-lg">
                With the **`encodings.pkl`** file ready, start the main application to begin real-time detection and logging.
            </p>
            <div class="code-block">
<pre><code># Run the main attendance script
python main.py</code></pre>
            </div>
            <p class="text-sm text-gray-400 mt-2">
                The webcam will open, and attendance will be logged to a daily CSV file (e.g., `2025-11-27.csv`).
            </p>
        </section>

        <!-- Project Structure -->
        <section class="mb-16">
            <h2 class="text-4xl font-bold mb-10 border-l-4 border-primary-blue pl-4">
                <span class="icon mr-3 text-3xl">📁</span> Project Structure
            </h2>
            <div class="code-block">
<pre><code>smart-attendance-system/
├── main.py                 # Main script for real-time attendance logging
├── preencoding.py          # Dedicated script for generating face encodings
├── encodings.pkl           # Output file for stored user face encodings (binary)
├── photos/                 # Directory containing user photos (e.g., John_Doe.jpg)
├── [DATE].csv              # Output file for daily attendance records
└── requirements.txt        # List of required Python packages</code></pre>
            </div>
        </section>

        <!-- Contact & License -->
        <section class="mb-8 p-8 bg-secondary-gray rounded-xl shadow-2xl border border-gray-700">
            <h2 class="text-3xl font-bold mb-6 flex items-center">
                <span class="icon mr-3 text-3xl">🤝</span> Get Involved
            </h2>
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center">
                <div class="space-y-3 mb-4 md:mb-0">
                    <p class="text-lg text-white font-semibold">Contributing & License</p>
                    <p class="text-gray-400">
                        Contributions are welcome! See the <a href="#" class="text-primary-blue hover:text-blue-400 font-medium">Contributing Guide</a> for details.
                    </p>
                    <p class="text-gray-400">
                        Distributed under the MIT License. See <a href="#" class="text-primary-blue hover:text-blue-400 font-medium">LICENSE.txt</a> for more information.
                    </p>
                </div>
                <div class="text-right mt-4 md:mt-0">
                    <p class="text-lg text-white font-semibold">Contact</p>
                    <p class="text-gray-400">Project Maintainer - <a href="mailto:your.email@example.com" class="text-primary-blue hover:text-blue-400">your.email@example.com</a></p>
                    <a href="https://github.com/YourUsername/smart-attendance-system" target="_blank" class="text-gray-400 hover:text-primary-blue transition duration-200 mt-1 inline-block text-sm">
                        github.com/.../smart-attendance-system
                    </a>
                </div>
            </div>
        </section>
        
        <!-- Footer -->
        <footer class="text-center text-sm text-gray-500 pt-8 border-t border-gray-800 mt-12">
            &copy; 2025 Smart Attendance System. Built with Python, OpenCV, and a passion for automation.
        </footer>

    </main>

</body>
</html>
