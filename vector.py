from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/legal_text_classification.csv")

# Replace NaN values with empty strings
df = df.fillna("")

print(f"Loaded {len(df)} rows from CSV.")

# -----------------------------
# Embedding Model
# -----------------------------
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)

# -----------------------------
# Chroma Vector Store
# -----------------------------
db_location = "./chrome_langchain_db"

vector_store = Chroma(
    collection_name="legal_cases",
    persist_directory=db_location,
    embedding_function=embeddings,
)

collection_count = vector_store._collection.count()

print(f"Collection contains {collection_count} documents.")

# -----------------------------
# Build Database ONLY if Empty
# -----------------------------
from tqdm import tqdm

if collection_count == 0:

    print("Building Chroma Database...")

    BATCH_SIZE = 25

    documents = []
    ids = []

    for i, row in tqdm(df.iterrows(), total=len(df)):

        document = Document(
            page_content=f"""
Case ID: {row['case_id']}

Case Title:
{row['case_title']}

Case Description:
{row['case_text']}

Case Outcome:
{row['case_outcome']}
""",
            metadata={
                "Case_ID": str(row["case_id"]),
                "Case_Title": str(row["case_title"]),
                "Case_Outcome": str(row["case_outcome"]),
            },
        )

        documents.append(document)
        ids.append(str(i))

        # Insert one batch
        if len(documents) == BATCH_SIZE:
            vector_store.add_documents(
                documents=documents,
                ids=ids
            )

            documents = []
            ids = []

    # Insert remaining documents
    if documents:
        vector_store.add_documents(
            documents=documents,
            ids=ids
        )

    print("Finished building database!")
    print("Collection count:", vector_store._collection.count())
# -----------------------------
# Retriever
# -----------------------------
retriever = vector_store.as_retriever(
    search_kwargs={"k": 7}
)