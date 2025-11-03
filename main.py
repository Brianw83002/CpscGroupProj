

# Define token categories
keywords = {"int", "float", "char", "string", "if", "else", "for", "while", "return"}
operators = {"+", "-", "*", "/", "=", "==", "!=", ">=", "<=", ">", "<", "++", "--"}
separators = {"(", ")", "{", "}", ";", ",", "[", "]"}

# Removes single-line (// ...) and multi-line (/* ... */) comments from code.
def remove_comments(code):

    cleaned_code = ""
    i = 0
    length = len(code)

    while i < length:
        # Handle single-line comment    (// ...)
        if code[i:i+2] == "//":
            # Skip until end of line
            while i < length and code[i] != "\n":
                i += 1

        # Handle multi-line comment     (/* ... */)
        elif code[i:i+2] == "/*":
            i += 2  # Skips the "/*"
            # Skips everything until "*/" is found
            while i < length - 1 and code[i:i+2] != "*/":
                i += 1
            i += 2  # Skip the "*/"

        # Normal code character, keep it
        else:
            cleaned_code += code[i]
            i += 1

    return cleaned_code


# Function to classify lexemes
def classify_lexeme(token):
    if token in keywords:
        return "keyword"
    elif token in operators:
        return "operator"
    elif token in separators:
        return "separator"
    elif token.isdigit():
        return "integer"
    elif token.replace(".", "", 1).isdigit() and token.count(".") == 1:
        return "float"
    elif len(token) == 3 and token[0] == "'" and token[2] == "'":
        return "char"
    elif len(token) >= 2 and token[0] == '"' and token[-1] == '"':
        return "string"
    else:
        return "identifier"

def tokenize(code):
    """
    Tokenizes the given code into lexemes and classifies each token.
    Handles operators, separators, identifiers, and literals.
    """
    # Step 1: Remove comments
    code = remove_comments(code)

    tokens = []         # List to store all tokens
    current_token = ""  # Accumulate characters for identifiers/literals
    i = 0
    length = len(code)

    while i < length:
        char = code[i]

        # Step 2: Check for multi-character operators (==, !=, >=, <=, ++, --)
        if i < length - 1 and code[i:i+2] in operators:
            if current_token.strip():
                tokens.append(current_token.strip())
            tokens.append(code[i:i+2])
            current_token = ""
            i += 2
            continue

        # Step 3: Handle single-character operators, separators, or whitespace
        if char in operators or char in separators or char.isspace():
            if current_token.strip():
                tokens.append(current_token.strip())
                current_token = ""
            if char in operators or char in separators:
                tokens.append(char)

        # Step 4: Part of an identifier, literal, or number
        else:
            current_token += char

        i += 1

    # Step 5: Append any remaining token
    if current_token.strip():
        tokens.append(current_token.strip())

    # Step 6: Classify and print tokens
    for token in tokens:
        token_type = classify_lexeme(token)
        print(f'"{token}" = {token_type}')



# Main function 
def main():

    ######################### Change File name ################
    file_name = "TestFiles/helloWorld.txt"  
    ###########################################################

    with open(file_name, "r") as f:
        code = f.read()

    tokenize(code)

if __name__ == "__main__":
    main()
