# 📦 KPA API Assignment – FastAPI + SQLite

This project implements 2 selected APIs from the [KPA Form Data Postman Collection] using **FastAPI** and **SQLite**.

---

## 🚀 Tech Stack

- **Python 3.10+**
- **FastAPI** – Web framework
- **SQLite** – Lightweight embedded database
- **SQLAlchemy** – ORM for DB interaction
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server
- **dotenv** – Environment variable support

---

## ✅ Implemented APIs

### 1. `POST /user/register`

Registers a new user using form-data.

- **Method:** `POST`
- **Consumes:** `application/x-www-form-urlencoded`
- **Validates:** Unique phone number
- **Form Parameters:**
  - `phone_number`: string (required)
  - `password`: string (required)

#### ✅ Sample Response:

```json
{
  "message": "User registered successfully"
}
```

---

### 2. `POST /upload-document`

Uploads a file and stores its path in the DB.

- **Method:** `POST`
- **Consumes:** `multipart/form-data`
- **Form Parameter:**
  - `file`: any file

#### ✅ Sample Response:

```json
{
  "filename": "invoice.pdf",
  "path": "./uploads/invoice.pdf"
}
```

---

## ⚙️ Setup Instructions

### 1. Clone & set up the project

```bash
git clone <your_repo_url>
cd kpa_api_assignment
python -m venv env
env\Scripts\activate  # On Windows
pip install -r requirements.txt
```

---

### 2. Configure Environment Variables

Create a `.env` file in the root folder:

```env
UPLOAD_DIR=./uploads
DATABASE_URL=sqlite:///./kpa.db
```

Create the `uploads/` folder if not present:

```bash
mkdir uploads
```

---

### 3. Create Tables in SQLite

Tables are auto-created via:

```python
Base.metadata.create_all(bind=engine)
```

---

### 4. Run the API server

```bash
uvicorn app.main:app --reload
```

Visit the docs:  
📍 http://localhost:8000/docs

---

## 🧪 Testing with Postman

1. Import the file `poojit_kpa_postman_collection.json`
2. Two saved requests will be available:
   - `POST /user/register`
   - `POST /upload-document`
3. Run locally against `http://localhost:8000`
4. Verify working responses

---

## 📁 Project Structure

```
kpa_api_assignment/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── user.py
│       └── document.py
├── uploads/                 # Uploaded files go here
├── .env
├── requirements.txt
├── postman_collection.json # Final collection
├── README.md
```

---

## 📝 Notes

- Duplicate `phone_number` is prevented with a `UNIQUE` constraint
- All APIs strictly follow the structure from the original KPA Postman Collection
- SQLite DB (`kpa.db`) is used for local dev and demo purposes

---

## 📤 Submission Requirements

You must submit the following:

| Label           | What to Submit                                    |
| --------------- | ------------------------------------------------- |
| ✅ Source Code  | GitHub repo link or zipped folder                 |
| ✅ Postman JSON | `poojit_kpa_postman_collection.json`              |
| ✅ README       | This file                                         |
| ✅ Video Demo   | Screen recording explaining APIs & implementation |

---

#### ✅ Suggested Format:

```
source-code: https://github.com/mr-poojit/kpa_api
postman-collection: https://drive.google.com/drive/folders/1LrYuv3xdH8t2DyYtv32YrjI5ccnpM-PV?usp=sharing
demo-video: https://www.loom.com/share/3935213b4233407c915b7476f0612a22?sid=4d30b203-06c7-48d6-9a69-e1f4e9ab47b6
```

---

## 👨‍💻 Author

**Poojit Jagadeesh Nagaloti**  
Backend Developer – KPA Form Data
