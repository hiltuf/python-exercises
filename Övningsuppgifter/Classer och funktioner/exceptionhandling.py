class OgiltigÅlderError(Exception):
    """Ett undantag för ogiltig ålder."""
    pass

def kontrollera_ålder(age):
    if age < 0:
        raise OgiltigÅlderError("Åldern kan inte vara negativ!")
    print(f"Åldern är giltig: {age}")

# Testa
try:
    kontrollera_ålder('tjo')
except OgiltigÅlderError as e:
    print(f"Fel: {e}")
