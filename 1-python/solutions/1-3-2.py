def cleanup( text: str) -> str:
    for ch in "!?,.":
        if ch in text:
            text = text.replace(ch, "")

    return text.lower().strip()




text = "  THis! Is. , a tEST? "
cleaned = cleanup(text)
print(cleaned)

