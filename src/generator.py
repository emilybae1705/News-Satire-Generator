import openai
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

BIASES = {
    "authority_bias": "Headlines that reference fictional experts, studies, or prestigious institutions to seem credible",
    "confirmation_bias": "Headlines that play into existing stereotypes or beliefs people already hold",
    "anchoring_bias": "Headlines with specific numbers or statistics that sound legitimate but are false"
}

def generate_headlines(num_per_bias=7):
    """Generate satirical headlines leveraging different cognitive biases using OpenAI API"""
    headlines = []
    
    for bias_type, bias_description in BIASES.items():
        for i in range(num_per_bias):
            prompt = f"""Generate 1 satirical news headline that leverages {bias_type}.
            
            The headline should:
            - Be believable enough that some people might think it's real
            - Be humorous or absurd upon closer inspection
            - Specifically leverage {bias_description}
            - Be 10-15 words maximum
            - Choose any topic that would be suitable for satirical news
            
            Return ONLY the headline text with no additional commentary.
            """
            
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.8,
                    max_tokens=50
                )
                
                headline = response.choices[0].message.content.strip().strip('"')
                
                headlines.append({
                    "headline_id": len(headlines) + 1,
                    "bias_type": bias_type,
                    "headline": headline
                })
                
                print(f"Generated ({bias_type}): {headline}")
                time.sleep(1)
                
            except Exception as e:
                print(f"Error generating headline: {e}")
    
    df = pd.DataFrame(headlines)
    df.to_csv("generated_headlines.csv", index=False)
    print(f"Generated {len(headlines)} headlines and saved to generated_headlines.csv")
    
    return df

if __name__ == "__main__":
    headlines_df = generate_headlines(3)