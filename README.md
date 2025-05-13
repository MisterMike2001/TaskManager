📝 TaskManager
A simple, user-friendly Task Manager web application built with Django.

🔧 Project Structure
Main Project: TodoManagerProject

Apps:
members: Handles user authentication and profile management.
TodoManagerApp: Manages user tasks and project-related functionalities.

👤 Members App
Manages user-related functionality: login, registration, account settings, and logout.

🔐 Login
Uses Django’s built-in authentication system.
Authenticated users can access and manage their tasks.
Unauthenticated users see a public homepage with basic information and options to log in or register.
Access to all other pages is restricted unless the user is logged in.

📝 Register
Allows new users to create an account using a custom form (forms.py).
On successful registration:
  User is automatically logged in.
  Redirected to the authenticated homepage.
  
On failure:
  Error messages are displayed.
User stays on the registration page.

⚙️ Account
Lets users update their profile information:
  Username
  First name
  Last name
  Email

On success: redirected to the homepage.
On failure: displays appropriate error messages.

🚪 Logout
Logs the user out and redirects them to the public homepage.


✅ TodoManagerApp
Handles all task-related functionality.

🏠 Home Page
Displays task statistics:
  Tasks completed
  Tasks in progress
  Tasks in queue
  
Lists ongoing projects.
(Note: Still under development.)

📋 Todo Page
Displays all user tasks categorized into:
Completed
In Progress
In Queue
Each task is clickable and redirects to its detailed view/edit page.
Includes an “Add New Task” button to create new tasks.

📝 TaskItem Page
Allows users to edit an existing task.
Fields include:
  Title
  Description
  Progress 
  (with more attributes to be added).
  
On successful update: redirects back to the Todo page.

➕ Add New Task
Lets users create a new task.
Form fields are the same as the TaskItem page.

🚀 Future Improvements
Add support for deadlines, priorities, and tags.
Implement notifications or reminders.
Improve home page analytics and dashboard UI.

🛠 Built With
Python
Django
HTML/CSS (Bootstrap recommended)

📩 Contact
For suggestions, issues, or contributions, feel free to open an issue or pull request.
