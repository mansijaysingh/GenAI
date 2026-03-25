import tiktoken

enc=tiktoken.encoding_for_model("gpt-4o")
text="Hey there! My name is mansi"
tokens=enc.encode(text)
print("token:",tokens)

