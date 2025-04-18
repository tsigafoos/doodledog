from typing import Optional

from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files directory for CSS/JS if needed
app.mount("/static", StaticFiles(directory="static"), name="static")

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Webpage with Nav and Toolbar</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Ensure the layout takes full height */
        html, body {
            height: 100%;
            margin: 0;
        }
        #sidebar {
            transition: width 0.3s;
        }
        #sidebar.collapsed {
            width: 64px;
        }
        #sidebar:not(.collapsed) {
            width: 200px;
        }
        #content {
            transition: margin-left 0.3s;
        }
        #sidebar.collapsed ~ #content {
            margin-left: 64px;
        }
        #sidebar:not(.collapsed) ~ #content {
            margin-left: 200px;
        }
    </style>
</head>
<body class="flex flex-col h-full bg-gray-100">
    <!-- Navigation Bar -->
    <nav class="bg-blue-600 text-white p-4 flex justify-between items-center">
        <div class="text-xl font-bold">My Application</div>
        <div class="space-x-4">
            <a href="#" class="hover:underline">Home</a>
            <a href="#" class="hover:underline">About</a>
            <a href="#" class="hover:underline">Services</a>
            <a href="#" class="hover:underline">Contact</a>
        </div>
    </nav>

    <!-- Main Layout -->
    <div class="flex flex-1 overflow-hidden">
        <!-- Sidebar/Toolbar -->
        <aside id="sidebar" class="bg-gray-800 text-white w-48 flex-shrink-0 flex flex-col">
            <div class="p-4 flex justify-between items-center">
                <span class="sidebar-title font-semibold">Toolbar</span>
                <button id="toggleSidebar" class="text-white focus:outline-none">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                    </svg>
                </button>
            </div>
            <nav class="flex-1">
                <a href="#" class="block py-2 px-4 hover:bg-gray-700">Dashboard</a>
                <a href="#" class="block py-2 px-4 hover:bg-gray-700">Profile</a>
                <a href="#" class="block py-2 px-4 hover:bg-gray-700">Settings</a>
                <a href="#" class="block py-2 px-4 hover:bg-gray-700">Reports</a>
            </nav>
        </aside>

        <!-- Main Content -->
        <main id="content" class="flex-1 p-6 overflow-auto">
            <h1 class="text-2xl font-bold mb-4">Welcome to the Dashboard</h1>
            <p class="text-gray-700">
                This is the main content area. You can add your application content here.
                The navigation bar is fixed at the top, and the toolbar is on the left.
                Click the toggle button in the toolbar to collapse or expand it.
            </p>
        </main>
    </div>

    <script>
        const sidebar = document.getElementById('sidebar');
        const content = document.getElementById('content');
        const toggleSidebar = document.getElementById('toggleSidebar');

        toggleSidebar.addEventListener('click', () => {
            sidebar.classList.toggle('collapsed');
            // Update sidebar title visibility
            const sidebarTitle = sidebar.querySelector('.sidebar-title');
            sidebarTitle.style.display = sidebar.classList.contains('collapsed') ? 'none' : 'block';
        });
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content=html_content)
