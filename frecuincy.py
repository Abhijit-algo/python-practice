def count_words(text):
    # Step 1: Handle empty or whitespace-only inputs
    if not text.strip():
        return {}
    
    # Step 2: Convert to lowercase for case-insensitivity
    text = text.lower()
    
    # Step 3: Remove punctuation marks
    punctuation = [".", ",", "!", "?", ";", ":"]
    for p in punctuation:
        text = text.replace(p, "")
        
    # Step 4: Split the text into a list of words
    words = text.split()
    
    # Step 5: Count the frequencies using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return word_counts

# --- Test the function ---
sample_text = "The cat sat on the mat, and the dog sat on the rug!"
result = count_words(sample_text)
print(result)

