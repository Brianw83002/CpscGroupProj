
# Instructions

# CPSC 323 - PROJECT 1
**Project Description:** In this project, you will build a Lexical Analyzer that reads a .txt file containing code snippets and tokenizes the input while removing unnecessary
elements like whitespace and comments. The program should classify lexemes intotokens(keywords, operators, identifiers, separators, literals) and output them in a structured format.

**Objective:** Develop a lexical analysis tool that simulates the first phase of a compiler. Understand how tokenization and pattern recognition work in programming languages. Learn to handle comments and whitespace efficiently.

**Project Requirements:**

● Read an input .txt file containing source code.
● Remove unnecessary elements like whitespace and comments (// and / */).
● Identify and classify lexemes into the following token categories: Keywords (e.g.,
if, return, int) Operators (e.g., +, -, >=, !=) Separators (e.g., {, }, (, ), Identifiers
(e.g., variable_name, counter) Literals (e.g., 42, "Hello") Output the tokenized
format in the form <lexeme> = <token> Ensure correct handling of different
lexeme types using regular expressions.

## Example Input: 
    int main() { int a = 10; int b = a + 5; return b; // returning the value of b }
## Expected Output: 
    "int"   = keyword
    "main"  = identifier
    "("     = separator
    ")"     = separator
    "{"     = separator
    "int"   = keyword
    "a"     = identifier
    "="     = operator
    "10"    = integer
    ";"     = separator
    "}"     = separator


## What you’ll need to submit:
● Screenshot of Correct Output (20 points)
● PDF Report (Max 2 Pages) including: Explanation of code functionality
Tokenization methodology Time and space complexity analysis (30 points)
By the end of this project, you