# News Satire Generator

## Project Structure

- `src/generator.py`: The main script that generates satirical headlines. It uses OpenAI's GPT-4 to create headlines based on three types of cognitive biases:
  - Authority bias: Headlines referencing fictional experts or institutions
  - Confirmation bias: Headlines playing into existing stereotypes
  - Anchoring bias: Headlines with specific but false statistics

The script saves the generated headlines to `generated_headlines.csv` for future reference.

## Usage

Run the generator script to create satirical headlines:
```bash
python src/generator.py
```

This will generate 3 headlines for each bias type (9 total) and save them to a CSV file.