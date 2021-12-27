from chat import get_response

if __name__ == "__main__":
    print("Para salir escribir 'salir'")
    while True:
        sentence = input("Usuario: ")
        if sentence == "salir":
            break

        resp = get_response(sentence)
        print(resp)
