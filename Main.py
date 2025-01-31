from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

# Michigan Slang Dictionary
michigan_slang = {
    "What up doe?": "A Detroit greeting, similar to 'What’s up?'",
    "Bussin'": "Something that tastes really good (e.g., 'This Coney dog is bussin'!').",
    "No cap": "For real, no lie (e.g., 'That new Jordan drop was crazy, no cap.').",
    "The D": "Short for Detroit.",
    "Buffs": "Cartier glasses, a big status symbol in Detroit.",
    "Slide": "To come over or pull up (e.g., 'Slide through to the function.').",
    "Jit": "A young person, often a kid or someone younger than you.",
    "Bet": "Can mean 'okay,' 'we’ll see,' or 'it’s on' depending on the context.",
    "Heavy": "Serious or deep (e.g., 'That convo was heavy.').",
    "Dog": "A close friend or someone you roll with.",
    "Blowed": "Can mean mad, high, or surprised (e.g., 'Man, I was blowed when I saw that.').",
    "Ain’t it?": "Used at the end of a sentence for emphasis (e.g., 'That was wild, ain’t it?').",
    "Flick": "A picture or a movie (e.g., 'Let’s take a flick real quick.').",
    "Mug": "Can refer to a face or a person (e.g., 'Look at this mug.').",
    "Fasho": "For sure, meaning agreement (e.g., 'You coming through?' 'Fasho.').",
    "Coney": "Short for 'Coney Island,' a popular type of diner in Michigan, especially Detroit.",
    "You straight?": "A way of asking if someone is okay or if they need something.",
    "Finna": "About to (e.g., 'I’m finna go grab some food.').",
    "Out cold": "Something that’s really good or impressive (e.g., 'That fit is out cold.').",
    "Throwed": "Wild, crazy, or turnt (e.g., 'That party was throwed.').",
    "Wetty": "A term used to describe a clean outfit or someone looking fresh.",
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Michigan Slang API! Use /translate?word=Buffs"}

@app.get("/translate")
def translate_word(word: str = Query(..., description="Word to translate to Michigan slang")):
    """Returns the Michigan slang meaning of a word if available."""
    translation = michigan_slang.get(word, "No translation found. Try another word.")
    return {"word": word, "translation": translation}

# Only needed for local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)