

---

Academic Search Engine






---

Project Overview

The Academic Search Engine is a web-based application developed using Python and the Flask framework. The main objective of this project is to retrieve relevant academic information based on a user’s search query and display the results in a ranked format.

The system uses fundamental Information Retrieval techniques such as TF-IDF (Term Frequency – Inverse Document Frequency) and Cosine Similarity within a Vector Space Model to analyze and measure the relevance between the user query and retrieved documents.

This project demonstrates how search engines process queries, analyze text data, and rank documents according to their similarity scores.


---

Features

• Search academic topics through a web interface
• Retrieve relevant summaries from Wikipedia
• Calculate Term Frequency (TF)
• Calculate Inverse Document Frequency (IDF)
• Generate TF-IDF scores for document ranking
• Compute Cosine Similarity between query and documents
• Rank documents based on similarity values
• Display results with summary and Wikipedia links
• Simple and user-friendly interface


---

Technologies Used

Technology	Purpose

Python	Core programming language
Flask	Web framework
Scikit-learn	TF-IDF vectorization and similarity calculation
Wikipedia API	Data retrieval
HTML	Web page structure
CSS	User interface styling



---

Project Structure

Academic_Search_Engine
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates
      └── index.html


---

Installation and Setup

1 Clone the Repository

GitHub :
https://github.com/AllanJenisha10/Academic_Search_Engine.git/

2 Install Required Packages

pip install -r requirements.txt

3 Run the Application

python app.py

4 Open in Browser

http://127.0.0.1:5000/


---

Working Methodology

1. The user enters a search query in the application.


2. The system retrieves related topics from Wikipedia.


3. The retrieved documents are processed using TF-IDF vectorization.


4. Cosine Similarity is calculated between the query and each document.


5. Documents are ranked based on similarity scores.


6. The ranked results are displayed with relevant metrics.




---

Output Details

Each search result provides the following information:

• Document Rank
• Term Frequency (TF)
• Inverse Document Frequency (IDF)
• TF-IDF Score
• Cosine Similarity Value
• Wikipedia Link
• Summary of the topic


---

Live Demo

You can access the deployed application here:

Application Link

https://academic-search-engine.onrender.com


---

Deployment

This project is deployed using Render.

Deployment Steps

1. Upload the project to GitHub.


2. Connect the repository to Render.


3. Select Web Service.


4. Configure the following commands.



Build Command

pip install -r requirements.txt

Start Command

gunicorn app:app

5. Render installs dependencies and builds the application.


6. A public URL is generated to access the application online.




---

Future Enhancements

The system can be improved further with additional features and capabilities.

• Integration with academic research databases and digital libraries
• Implementation of advanced Natural Language Processing (NLP) techniques
• Addition of user login and personalized search history
• Improved user interface with enhanced design
• Support for larger document collections
• Performance optimization using caching techniques

These improvements can make the search engine more efficient and suitable for real-world academic research applications.


---

Academic Purpose

This project was developed as part of an Information Retrieval assignment to demonstrate document retrieval and ranking techniques used in search engines.


---

Repository

https://github.com/AllanJenisha10/Academic_search_engine


