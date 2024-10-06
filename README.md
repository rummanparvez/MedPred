
# MedPred - General Disease Prediction System

### Project Scope

MedPred is a disease prediction system that involves three types of users: doctors, patients, and administrators. Each user is authenticated within the system and has role-based access. The core functionalities include:

- **Patients**: Patients can enter their symptoms, and the system will predict potential diseases. It also suggests relevant doctors for the predicted diseases.
- **Doctors**: Patients can consult doctors online based on the system’s suggestions. The system allows online consultation from the comfort of home.
- **Admin**: Admins manage the system, ensuring smooth operation and authentication for both patients and doctors.

### Technologies Used

- **Front-end**: HTML, CSS, Bootstrap, JavaScript, jQuery
- **Back-end**: Django (Python-based web framework)
- **Database**: PostgreSQL
- **Tools**: PgAdmin, Orange (for data analytics)

### System Architecture

MedPred follows a structured, role-based architecture for different users (patients, doctors, and admins). All users interact with the system through an authenticated web interface.

### Data Collection

The dataset used for disease prediction consists of real symptoms and disease information, collected from reputable sources such as Kaggle and various health-related websites. The dataset contains:

- **5000 rows** of patient records
- **132 different symptoms**
- **40 general disease classes**

The data helps the machine learning model in predicting diseases based on the input symptoms.

### Webpages

MedPred features the following web interfaces:

- **Homepage**: User can view general information.
- **Login Modal**: Different login options for users.
- **Patient UI**: Patients can enter symptoms and view predictions.
- **Feedback Form**: Users can provide feedback on the predictions.
- **Consult a Doctor**: Patients can schedule consultations.
- **Admin Interface**: Admins can manage user accounts and system settings.

### How To Use This

First, make sure PostgreSQL and PgAdmin are installed on your system. Then, you need to manually create a database instance on PostgreSQL named "medpred" (it’s better to use PgAdmin for that).

Next, set up your environment and run the following commands:

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Finally, navigate to `http://127.0.0.1:8000/` in your browser to access the application.

### Dataset Used

You can find the dataset used for this project [here](https://www.kaggle.com/neelima98/disease-prediction-using-machine-learning).

If you like this project, do give it a "Star". Thank you!
