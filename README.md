# Neobis Shortener Project

This project is a simple URL shortening service implemented using Django and Django REST framework.

## Installation

1. Clone the repository:

    git clone https://github.com/AibekYrysbekov/Neobis_Shortener_Project.git


2. Change to the project directory:

   cd Neobis_Shortener_Project


3. Create and activate a virtual environment (recommended):
   
   python -m venv venv

   source venv/bin/activate  # For Linux/Mac

   venv\Scripts\activate  # For Windows


4. Install dependencies from the requirements.txt file:

   pip install -r requirements.txt


5. Apply migrations to the database:

   python manage.py migrate


6. Start the server:

   python manage.py runserver

After these steps, your server will be accessible at http://localhost:8000/.


## Usage

Create a short link: Send a POST request to /api/create/ with a JSON body containing the original_url. For example: {"original_url": "https://example.com"}.

Get a list of all short links: You can retrieve a list of all created short links by sending a GET request to /api/list/.

Follow a short link: Simply navigate to the URL containing the short link to perform a redirection to the original URL.

## Additional Configuration

Configure the database: By default, the project uses Postgresql as the database. You can configure other databases by changing the settings in the settings.py file.

Additional Features: You can add additional features to the project, such as link expiration, click analytics, and more.


   
   