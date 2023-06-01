from transformers import GPT2Tokenizer, TFGPT2Model, pipeline, set_seed

class Lexgpt:

    def __init__(self, text, maxlen=100):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = TFGPT2Model.from_pretrained('gpt2')
        self.generator = pipeline('text-generation', model='gpt2')
        self.maxlen = maxlen
        self.text = text

    def __call__(self) -> str:
        return self.generator(self.text, max_length=self.maxlen, num_return_sequences=1)[0]["generated_text"]
    
    def setSeed(seed):
        set_seed(seed)      