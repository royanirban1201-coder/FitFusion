# FitFusion

AI powered fitness and calorie analysis system.

## Tech Stack
Backend: FastAPI
ML: Scikit-Learn
Frontend: (React / Next / etc)

---

## Setup Instructions

### 1 Clone repository
git clone <repo-link>

cd FitFusion

### 2 Create virtual environment
python -m venv venv

### 3 Activate virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 4 Install dependencies
pip install -r requirements.txt

### 5 Run backend
uvicorn backend.main:app --reload