# Task 1

filename = "lexeme1.txt"
user_input = "import maths\n\n def area():\n\n # This is a simple function that calculates the area of a rectangle\n\n  length=10\n\n width=4\n\n result=10*4\n\n return result"

def save_data_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

save_data_to_file(filename, user_input)

input_file = "lexeme1.txt"
output_file = "lexeme2.txt"

# Task 1 Preprocessor

class Preprocessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def remove_blank_lines(self):
        with open(self.input_file, 'r') as file:
            lines = file.readlines()
            non_blank_lines = [line for line in lines if line.strip()]

        with open(self.output_file, 'w') as file:
            file.writelines(non_blank_lines)

    def remove_imports_annotations(self):
        with open(self.output_file, 'r') as file:
            lines = file.readlines()
            modified_lines = [line for line in lines if not line.strip().startswith(('import', '@'))]

        with open(self.output_file, 'w') as file:
            file.writelines(modified_lines) 

    def remove_comments_statements(self):
        with open(self.output_file, 'r') as file:
            lines = file.readlines()
            modified_lines = [line for line in lines if not line.strip().startswith(('#', '"""'))]

        with open(self.output_file, 'w') as file:
            file.writelines(modified_lines)

    def preprocess_file(self):
        try:
            self.remove_blank_lines()
            self.remove_comments_statements()
            self.remove_imports_annotations()

            print(f"Processed file saved to {self.output_file}")
            print()
            with open(self.output_file, 'r') as file:
                data = file.read()
                print("TASK 1 OUTPUT IS: \n" + data)
        except:
            print(f"Error during preprocessing")

# Run Task 1
processor = Preprocessor(input_file, output_file)
processor.preprocess_file()

# Task 2

class Processor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def break_data_in_characters(self):
        try:
            with open(self.input_file, 'r') as input_file:
                buffer = []
                while True:
                    char = input_file.read(1)

                    if not char:
                        break

                    if char != '\n':
                        buffer.append(char)

                buffer.append('$')

            with open(self.output_file, 'w') as output_file:
                output_file.write(''.join(buffer))

            with open(self.output_file, 'r') as output_file:
                data = output_file.read()
                print("TASK 2 OUTPUT \n" + data)
        except:
            print(f"Error during processing")
# Run Task 2
input_file2 = "lexeme2.txt"
output_file2 = "lexeme3.txt"
processor2 = Processor(input_file2, output_file2)
processor2.break_data_in_characters()

# Task 3

import re

class LexicalAnalysis:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def generate_lexemes(self):
        try:
            with open(self.input_file, 'r') as file:
                content = file.read()

            keyword_pattern = r'\b(?:and|as|assert|break|class|continue|def|del|elif|else|except|False|finally|for|from|global|if|import|in|is|lambda|None|nonlocal|not|or|pass|raise|return|True|try|while|with|yield)\b'
            identifier_pattern = r'\b[a-zA-Z_]\w*\b'
            operator_pattern = r'\+|-|\*|\/|%|=|==|!=|<|>|<=|>=|and|or|not|in|is'
            punctuator_pattern = r'{|}|\[|\]|\(|\)|,|;|:|\.'
            literal_pattern = r'\b(?:\d+\.?\d*|".*?"|\'.*?\')\b'

            combined_pattern = re.compile(f'({keyword_pattern}|{identifier_pattern}|{operator_pattern}|{punctuator_pattern}|{literal_pattern})', re.DOTALL)

            lexemes = [token for token in combined_pattern.findall(content) if token.strip()]

            with open(self.output_file, 'w') as file:
                file.write("\n".join(f"Lexeme: {lexeme}" for lexeme in lexemes))

            with open(self.output_file, 'r') as file:
                data = file.read()
                print("Task 3 output is: \n" + data)
        except:
            print(f"Error during lexical analysis")

# Run Task 3
input_file3 = "lexeme3.txt"
output_file3 = "lexeme4.txt"
analyzer = LexicalAnalysis(input_file3, output_file3)
analyzer.generate_lexemes()
