import txtai.embeddings
from gtts import gTTS
import os

# Create an embedding index
embeddings = txtai.embeddings.Embeddings({"path": "sentence-transformers/all-MiniLM-L6-v2"})

# Add documents to the embedding index
embeddings.add("Document 1: This is a sample document.")
embeddings.add("Document 2: This is another sample document.")

# Define a function to respond to user queries
def respond(query):
    # Search for the query
    results = embeddings.search(query, limit=10)

    # Generate a response
    response = "I found the following results: "
    for result in results:
        response += f"{result['score']}: {result['text']}\n"

    # Convert the response to audio
    tts = gTTS(text=response, lang='en')
    tts.save("response.mp3")

    # Play the audio
    os.system("start response.mp3")

# Test the respond function
respond("sample")