from fastapi import FastAPI, Query

app = FastAPI()

# Michigan Slang Dictionary (All lowercase keys)
slang_dict = {
    "what up doe": "A Detroit greeting, similar to 'What’s up?'",
    "bussin": "Something that tastes really good (e.g., 'This Coney dog is bussin!')",
    "no cap": "For real, no lie (e.g., 'That new Jordan drop was crazy, no cap.')",
    "the d": "Short for Detroit.",
    "buffs": "Cartier glasses, a big status symbol in Detroit.",
    "slide": "To come over or pull up (e.g., 'Slide through to the function.')",
    "jit": "A young person, often a kid or someone younger than you.",
    "bet": "Can mean 'okay,' 'we’ll see,' or 'it’s on' depending on the context.",
    "heavy": "Serious or deep (e.g., 'That convo was heavy.')",
    "dog": "A close friend or someone you roll with.",
    "blowed": "Can mean mad, high, or surprised (e.g., 'Man, I was blowed when I saw that.')",
    "ain't it": "Used at the end of a sentence for emphasis (e.g., 'That was wild, ain’t it?')",
    "flick": "A picture or a movie (e.g., 'Let’s take a flick real quick.')",
    "mug": "Can refer to a face or a person (e.g., 'Look at this mug.')",
    "fasho": "For sure, meaning agreement (e.g., 'You coming through?' 'Fasho.')",
    "coney": "Short for 'Coney Island,' a popular type of diner in Michigan, especially Detroit.",
    "you straight": "A way of asking if someone is okay or if they need something.",
    "finna": "About to (e.g., 'I’m finna go grab some food.')",
    "out cold": "Something that’s really good or impressive (e.g., 'That fit is out cold.')",
    "throwed": "Wild, crazy, or turnt (e.g., 'That party was throwed.')",
    "wetty": "A term used to describe a clean outfit or someone looking fresh."
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Michigan Slang API! Use /translate?word=Buffs"}

@app.get("/translate")
def translate_word(word: str = Query(..., description="Enter a Michigan slang word")):
    word_lower = word.lower()  # Convert input to lowercase
    translation = slang_dict.get(word_lower, "No translation found. Try another word.")
    return {"word": word, "translation": translation}

# Only needed for local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)