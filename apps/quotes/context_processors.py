from datetime import date


days = {
    2: 'Unleash the fries!',
    4: 'It\'s fucking friday!'
}


def day_info(request):
    today = date.today()

    return {
        'date': today,
        'result': days.get(today.weekday(), ''),
    }
