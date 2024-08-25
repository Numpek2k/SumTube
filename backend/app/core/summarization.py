from transformers import pipeline


def split_text(text, max_tokens=1012):
    """Splits text into chunks of maximum `max_tokens` tokens."""
    tokenizer = pipeline("summarization", model="facebook/bart-large-cnn").tokenizer
    tokens = tokenizer(text)['input_ids']

    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]

    chunked_text = [tokenizer.decode(chunk, skip_special_tokens=True) for chunk in chunks]
    return chunked_text

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    chunks = split_text(text)

    summaries = [summarizer(chunk, max_length=250, min_length=80, do_sample=False)[0]['summary_text'] for chunk in
                 chunks]

    final_summary = " ".join(summaries)
    return final_summary
