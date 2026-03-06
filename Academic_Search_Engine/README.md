
---

# Academic Search Engine

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-green)
![Project](https://img.shields.io/badge/Type-Academic%20Project-orange)

---

## Project Overview

The **Academic Search Engine** is a web-based application developed using **Python and the Flask framework**. The purpose of this project is to retrieve relevant academic information based on a user’s search query and present the results in a ranked order.

The system uses important **Information Retrieval techniques** such as **TF-IDF (Term Frequency – Inverse Document Frequency)** and **Cosine Similarity** within a **Vector Space Model** to measure the relevance between the query and retrieved documents.

This project demonstrates how search engines analyze text data and rank documents according to similarity scores.

---

## Features

• Search academic topics dynamically through a web interface
• Retrieve relevant summaries from Wikipedia
• Calculate **Term Frequency (TF)**
• Calculate **Inverse Document Frequency (IDF)**
• Generate **TF-IDF scores** for document analysis
• Compute **Cosine Similarity** between query and documents
• Rank documents based on relevance score
• Display results with links and summaries

---

## Technologies Used

| Technology    | Purpose                                         |
| ------------- | ----------------------------------------------- |
| Python        | Main programming language                       |
| Flask         | Web application framework                       |
| Scikit-learn  | TF-IDF vectorization and similarity calculation |
| Wikipedia API | Data retrieval                                  |
| HTML          | Structure of the web page                       |
| CSS           | Styling and user interface                      |

---

## Project Structure

```
Academic_Search_Engine
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates
      └── index.html
```

---

## Installation and Setup

### 1. Clone the Repository

```
git clone https://github.com/AllanJenisha10/Academic_search_engine.git
cd Academic_search_engine
```

### 2. Install Required Packages

```
pip install -r requirements.txt  (OR) 
    pip freeze > requirements.txt
```

### 3. Run the Application

```
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000/
```

---

## Working Methodology

1. The user enters an academic topic in the search field.
2. The system retrieves related topics from Wikipedia.
3. The retrieved documents are processed using **TF-IDF vectorization**.
4. **Cosine Similarity** is calculated between the query and documents.
5. Documents are ranked according to similarity scores.
6. The ranked results are displayed to the user.

---

## Output Details

Each search result contains the following information:

• Document Rank

• Term Frequency (TF)

• Inverse Document Frequency (IDF)

• TF-IDF Score

• Cosine Similarity Score

• Wikipedia URL

• Short Summary of the Topic

---

## Live Demo

You can access the deployed application here:

**Application URL**

            https://academic-search-engine.onrender.com

---

## Deployment

This project is deployed using **Render**.

### Deployment Steps

1. Upload the project to **GitHub**.
2. Connect the repository to **Render**.
3. Create a **Web Service**.
4. Configure the following commands.

**Build Command**

```
pip install -r requirements.txt
```

**Start Command**

```
gunicorn app:app
```

After deployment, Render will generate a **public URL** that can be used to access the application online.

---

## Future Enhancements

The current system demonstrates a basic academic search engine using Information Retrieval techniques. Future improvements may include:

• Integration with additional academic databases and research journals
• Implementation of advanced **Natural Language Processing (NLP)** techniques
• Personalized user search history and authentication system
• Improved graphical user interface and design
• Optimization for faster search performance

These enhancements would make the system more efficient and suitable for real-world academic research.

---

## Academic Purpose

This project was developed as part of an **Information Retrieval assignment** to demonstrate the practical implementation of document ranking techniques used in search engines.

---

## GitHub Repository

[https://github.com/AllanJenisha10/Academic_search_engine](https://github.com/AllanJenisha10/Academic_search_engine)

---
