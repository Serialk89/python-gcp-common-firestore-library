def firestore_instance():
  from google.cloud import firestore
  db = firestore.Client(project="my-budged-dev")
  return db

def add_document(col, body):
  if not col:
    raise ValueError("collection not defined")
  
  if not isinstance(body, dict) or not body:
    raise ValueError("body must be a non-empty dictionary")
  
  db = firestore_instance()
  doc_ref = db.collection(col).document()
  doc_ref.set(body)
  return doc_ref.id
  
    