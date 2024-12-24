def generate_response(prompt: str) -> str:
    """
    Foydalanuvchi tomonidan berilgan matnga javob generatsiya qiladi.

    Args:
        prompt (str): Savol yoki so'rov matni.

    Returns:
        str: Generatsiyalangan javob matni.
    """
    import google.generativeai as genai

    # API kalitni sozlash
    genai.configure(api_key="AIzaSyCXXwDe1J1XHiF5wCGdUJsCsc3hCRff9dU")  # "YOUR_API_KEY" o'rniga o'z API kalitingizni qo'ying

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
