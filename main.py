from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (Allows frontend to communicate with backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Allow GET and POST methods
    allow_headers=["*"],  # Allow all headers
)

# Michigan Slang Dictionary
slang_dict = {
    "what up doe": "A Detroit greeting, similar to 'What’s up?'",
    "bussin": "Something that tastes really good.",
    "no cap": "For real, no lie.",
    "the d": "Short for Detroit.",
    "buffs": "Cartier glasses, a big status symbol in Detroit.",
    "slide": "To come over or pull up.",
    "jit": "A young person, often a kid or someone younger than you.",
    "bet": "Can mean 'okay,' 'we’ll see,' or 'it’s on' depending on the context.",
    "heavy": "Serious or deep.",
    "dog": "A close friend or someone you roll with.",
    "blowed": "Can mean mad, high, or surprised.",
    "ain’t it": "Used at the end of a sentence for emphasis.",
    "flick": "A picture or a movie.",
    "mug": "Can refer to a face or a person.",
    "fasho": "For sure, meaning agreement.",
    "coney": "Short for 'Coney Island,' a popular diner in Michigan.",
    "you straight": "A way of asking if someone is okay or if they need something.",
    "finna": "About to.",
    "out cold": "Something that’s really good or impressive.",
    "throwed": "Wild, crazy, or turnt.",
    "wetty": "A term used to describe a clean outfit or someone looking fresh.",
}

@app.get("/")
def home():
    return {"message": "Welcome to the Michigan Slang API! Use /translate?word=your_word"}

@app.get("/translate")
def translate_word(word: str = Query(None, description="Word to translate")):
    """Returns the Michigan slang meaning of the word."""
    if not word:
        return {"error": "Please provide a word to translate."}
    
    word = word.lower()
    meaning = slang_dict.get(word, "No translation found. Try another word.")
    
    return {"word": word, "translation": meaning}