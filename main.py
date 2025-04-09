from openai import OpenAI
import env
import lists_combiner
from concurrent.futures import ThreadPoolExecutor

client = OpenAI(
    api_key=env.api_key
)

with open('system_prompt.txt', 'r') as f:
    system_prompt = f.read()

coding_questions = lists_combiner.combine_all_lists()
print(f"Total coding questions: {len(coding_questions)}")


def get_completion(index, sample):
    client.chat.completions.create(
        model="o3-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": sample}
        ],
        reasoning_effort="high",
        store=True
    )
    print(f"Completion #{index} complete")

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(get_completion, idx, sample) for idx, sample in enumerate(coding_questions)]
    for future in futures:
        future.result()
