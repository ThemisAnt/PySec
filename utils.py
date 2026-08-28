def classify_banner(banner):
    if not banner:
        return "No response received"
    elif banner.isprintable():
        return banner
    else:
        return "[Binary/non-text response]"

    