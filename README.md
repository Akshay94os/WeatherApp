# WeatherApp

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.1.6-green.svg)](https://www.djangoproject.com/)

## Overview

WeatherApp is a simple yet elegant web application built with Django that provides real-time weather information for any city worldwide. Beyond just displaying temperature and weather conditions, it enhances the user experience by fetching and showcasing a dynamic background image of the queried city, making your weather checks visually engaging.

The application leverages the OpenWeatherMap API for accurate weather data and the Google Custom Search API to retrieve high-quality images of cities. It's designed for users who want quick, intuitive weather updates with a touch of visual flair.

## Features

*   **Real-time Weather Display**: Get current temperature, weather description (e.g., "clear sky", "partly cloudy"), and an indicative weather icon.
*   **City Search**: Easily search for weather conditions in any city by typing its name.
*   **Dynamic City Backgrounds**: Each city search dynamically updates the background with a relevant image of that city, powered by Google Custom Search.
*   **Graceful Error Handling**: If an invalid city is entered or data is unavailable, the application provides a user-friendly error message and defaults to a predefined city (Indore) to ensure continuous functionality.
*   **Modern UI**: A clean and straightforward user interface for an optimal experience.

## Tech Stack

*   **Backend**:
    *   [Python](https://www.python.org/)
    *   [Django](https://www.djangoproject.com/) (v3.1.6)
    *   [Requests](https://docs.python-requests.org/en/master/) for API calls
*   **Frontend**:
    *   HTML5
    *   CSS3 (basic styling)
*   **Database**:
    *   [SQLite3](https://www.sqlite.org/index.html) (default Django database)
*   **External APIs**:
    *   [OpenWeatherMap API](https://openweathermap.org/api) for weather data.
    *   [Google Custom Search API](https://developers.google.com/custom-search/v1/overview) for city images.

## Architecture

The project follows a standard Django application structure:

```
Weather-App/
├── db.sqlite3              # SQLite database file
├── manage.py               # Django's command-line utility
├── static/                 # Static files (CSS, images)
│   └── style.css           # Custom CSS for the application
├── weatherapp/             # Core Django application
│   ├── admin.py            # Django admin configurations
│   ├── apps.py             # Application configuration
│   ├── migrations/         # Database migration files
│   ├── models.py           # Database models (currently unused)
│   ├── templates/          # HTML templates
│   │   └── weatherapp/
│   │       └── index.html  # Main weather display template
│   ├── urls.py             # Application-specific URL routes
│   └── views.py            # Business logic for handling requests and rendering responses
└── weatherproject/         # Main Django project configuration
    ├── asgi.py             # ASGI entry point
    ├── settings.py         # Project settings (database, installed apps, static files, etc.)
    ├── urls.py             # Project-wide URL routes
    └── wsgi.py             # WSGI entry point
```

**Key Components:**

*   **`weatherapp/views.py`**: This is the heart of the application. The `home` view handles incoming requests, extracts the city name, makes API calls to OpenWeatherMap and Google Custom Search, processes the responses, and renders the `index.html` template with the collected data. It also includes error handling for invalid city inputs.
*   **`weatherapp/templates/weatherapp/index.html`**: The main template responsible for displaying the weather information and the city background image. It dynamically updates based on the data passed from the view.
*   **`weatherproject/settings.py`**: Configures the Django project, including `INSTALLED_APPS` (where `weatherapp` is registered), `STATIC_URL` for serving static files, and `DATABASES` for SQLite.
*   **`weatherproject/urls.py`**: Defines the root URL patterns, including routing all requests to the `weatherapp.urls` module.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.x**: [Download Python](https://www.python.org/downloads/) (Python 3.1.6 was used for development).
*   **pip**: Python package installer (usually comes with Python).
*   **Virtual Environment**: Recommended for managing project dependencies.

### API Keys

This project requires API keys from two services:

1.  **OpenWeatherMap API Key**:
    *   Go to [OpenWeatherMap](https://openweathermap.org/).
    *   Sign up for a free account.
    *   Generate an API key from your account dashboard.
2.  **Google Custom Search API Key & Search Engine ID**:
    *   Go to [Google Cloud Console](https://console.cloud.google.com/).
    *   Create a new project.
    *   Enable the "Custom Search API" for your project.
    *   Generate an API key.
    *   Go to [Google Custom Search Engine](https://cse.google.com/cse/all).
    *   Create a new search engine.
    *   In the "Sites to search" field, enter a dummy URL (e.g., `example.com`) as we'll be searching the entire web.
    *   Under "Setup" -> "Basics", copy your "Search engine ID".

### Installation

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/Akshay94os/WeatherApp.git
    cd WeatherApp/Weather-App
    ```

2.  **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install project dependencies**:

    Create a `requirements.txt` file in the `Weather-App/` directory with the following content:

    ```
    Django==3.1.6
    requests
    ```

    Then install:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys**:

    Open `Weather-App/weatherapp/views.py` and locate the following lines:

    ```python
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid='
    PARAMS = {'units':'metric'}

    API_KEY =  '' # This is for Google Custom Search API
    SEARCH_ENGINE_ID = '' # This is for Google Custom Search Engine ID
    ```

    *   **OpenWeatherMap API Key**: Append your OpenWeatherMap API key to the `url` string. It should look like this:
        ```python
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_OPENWEATHERMAP_API_KEY'
        ```
    *   **Google Custom Search API Key**: Replace the empty string for `API_KEY` with your Google Custom Search API Key.
    *   **Google Search Engine ID**: Replace the empty string for `SEARCH_ENGINE_ID` with your Google Custom Search Engine ID.

    *(Note: For production environments, it's highly recommended to store API keys in environment variables rather than directly in the code. This project currently hardcodes them for simplicity.)*

5.  **Run database migrations**:

    ```bash
    python manage.py migrate
    ```

### Configuration

No additional configuration files are required beyond the API key setup in `views.py`.

## Usage

1.  **Start the Django development server**:

    Ensure you are in the `Weather-App/` directory and your virtual environment is active.

    ```bash
    python manage.py runserver
    ```

2.  **Access the application**:

    Open your web browser and navigate to:
    ```
    http://127.0.0.1:8000/
    ```

3.  **Enter a city**:

    Type the name of a city into the input field and press Enter or click the submit button to see its current weather and a corresponding background image.

## Development

### Setting up Development Environment

The steps in the [Installation](#installation) section cover setting up the development environment.

### Running Tests

Currently, no specific test suite has been implemented for this project.

### Code Style Guidelines

No formal code style guidelines are enforced beyond standard Python PEP 8 practices.

## Deployment

For production deployment, consider the following general steps for a Django application:

1.  **Set `DEBUG = False`** in `weatherproject/settings.py`.
2.  **Configure `ALLOWED_HOSTS`** in `weatherproject/settings.py` with your domain names.
3.  **Collect static files**:
    ```bash
    python manage.py collectstatic
    ```
4.  **Use a production-ready web server** like Gunicorn or uWSGI to serve the Django application, and a reverse proxy like Nginx or Apache to handle static files and proxy requests to the application server.
5.  **Securely manage API keys** using environment variables or a secrets management service.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1.  **Fork** the repository.
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3.  **Make your changes** and ensure they adhere to the project's style.
4.  **Test your changes** thoroughly.
5.  **Commit your changes** with a clear and descriptive message: `git commit -m "feat: Add new feature X"`.
6.  **Push your branch** to your forked repository: `git push origin feature/your-feature-name`.
7.  **Open a Pull Request** to the `main` branch of the original repository, describing your changes and their benefits.

## Troubleshooting

*   **"Entered data is not available to API"**: This error message indicates that the OpenWeatherMap API could not find data for the city you entered. Double-check the spelling or try a more common city name.
*   **No weather data or images appear**:
    *   Ensure your API keys (OpenWeatherMap, Google Custom Search) and Search Engine ID are correctly entered in `weatherapp/views.py`.
    *   Verify your internet connection.
    *   Check the browser's developer console for any network errors or JavaScript issues.
*   **`ModuleNotFoundError: No module named 'django'`**: You likely forgot to activate your virtual environment or install dependencies. Run `source venv/bin/activate` (or `venv\Scripts\activate`) and `pip install -r requirements.txt`.
*   **Static files (CSS) not loading**: Ensure `STATICFILES_DIRS` is correctly configured in `settings.py` and that `style.css` is in the `static/` directory.

## Roadmap

*   Implement a 5-day weather forecast.
*   Add user authentication and the ability to save favorite cities.
*   Improve UI/UX with more advanced frontend frameworks or libraries.
*   Enhance error handling with more specific messages.
*   Make the application fully responsive for various screen sizes.
*   Migrate API keys to environment variables for better security.

## License & Credits

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Credits:**

*   Developed by [Akshay94os](https://github.com/Akshay94os)
*   Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
*   City images powered by [Google Custom Search](https://developers.google.com/custom-search/v1/overview)