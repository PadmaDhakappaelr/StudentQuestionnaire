# config.py

#MONGO_URI = "mongodb+srv://admin:admin@deveagelcluster.crhta.mongodb.net/?retryWrites=true&w=majority"
MONGO_URI = st.secrets["MONGO_URI"]
DB_NAME = "student_db"
COLLECTION_NAME = "questionnaires"
