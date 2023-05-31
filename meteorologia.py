# API key openweathermap
API_KEY =  '02ce3117223858290ecc99b227f0577d'
# Coordinates
LANG = 'pt'
weather_data = []
@app.route('/temperatura', methods=['GET', 'POST'])
def temperatura():
    if request.method == 'POST':
        err_msg = ''
        new_city = request.form.get('city')
        new_city = new_city.lower()
        new_city = string.capwords(new_city)

        link = f"https://api.openweathermap.org/data/2.5/weather?q={new_city}&lang={LANG}&appid={API_KEY}&units=metric"
        r = requests.get(link).json()
        if r['cod'] == 200:
            weather = {
                'city' : r["name"],
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
            }
            weather_data.append(weather)
        else:
            err_msg = 'Esta cidade não é válida!'
        
        if err_msg:
            flash(err_msg, 'error')
        else:
            flash('Cidade adicionada com sucesso!', 'successo')

    return render_template('temperatura.html', weather_data=weather_data)