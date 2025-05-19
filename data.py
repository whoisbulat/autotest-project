import mimesis


valid_data = [
    (mimesis.Person("ru").email(), mimesis.Person("ru").name(), mimesis.Person("ru").telephone(), mimesis.Text().text()),
]



