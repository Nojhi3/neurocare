# Know N' Care

**Know N' Care** is a comprehensive platform designed to assist in the early detection and personalized intervention of neural disorders in young children. By connecting teachers and parents, we aim to provide timely support and resources to ensure the well-being of children aged 0-5.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Contributing](#contributing)
7. [License](#license)

---

## Introduction

Inspired by the film "Taare Zameen Par," **Know N' Care** addresses the challenges faced by parents and educators in identifying and managing neural disorders in children. Our platform provides tools for teachers to observe and record behavioral patterns in children, facilitating early detection. The system also offers parents access to resources and expert advice, aimed at fostering a nurturing environment for children's growth.

---

## Features

- **Teacher's Site**: A secure platform where teachers can log in, monitor children, and use engaging activities to observe behavior. Signs of potential neural disorders are recorded and analyzed.
- **Data-Driven Analysis**: Observations are stored in SQLite and processed using algorithms to estimate the likelihood of a neural disorder.
- **Parent's Site**: Parents are automatically notified if a potential issue is identified. They can access information about the disorder, connect with healthcare professionals, and find a curated list of remedial activities.
- **Community Support**: A platform for parents to connect, share experiences, and find support from others facing similar challenges.
- **Partnership with Experts**: Collaboration with doctors and educators to provide workshops, activities, and resources.

---

## Installation

### Prerequisites

- Python 3.x
- Flask framework
- SQLite for data storage
- Bootstrap for responsive design

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/knowncare.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd neurocare
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up SQLite database**:
   - Initialize the SQLite database by running the provided database setup script or by manually creating the database tables as defined in the project documentation.

5. **Run the Flask app**:
   ```bash
   flask run
   ```

6. **Access the platform**:
   - Open your browser and go to the provided local URL to start using the application.

---

## Usage

1. **Teacher's Site**: Teachers log in and engage children in activities like puzzles, coloring, and "Simon Says" to observe behavior. They record any signs of neural disorders, which are analyzed and stored in SQLite.
2. **Parent's Site**: Parents are notified if any issues are detected. They can access detailed information on the disorder and explore activities that help in the child's development.
3. **Community Engagement**: Parents can join a supportive community and participate in activities tailored to their child's needs.

*Screenshots of the Teacher's Site, Parent's Site, and community forum.*

---

## Technologies Used

- **Flask**: Backend framework for building the web application.
- **SQLite**: Database for storing and managing observational data.
- **Bootstrap**: For responsive and user-friendly design.
- **Python**: Core programming language for the app's functionality.
- **HTML/CSS**: For structuring and styling the web interface.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
