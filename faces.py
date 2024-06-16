def convert_emoticons_to_emojis(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    faceText = input()
    converted_text = convert_emoticons_to_emojis(faceText)
    print(converted_text)

main()
