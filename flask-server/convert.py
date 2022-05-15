def convert(dict):
    # dict = df.to_dict(orient='index')
    for i in range(len(dict)):
        dict[i]['Casts'] = eval(dict[i]['Casts'])
        dict[i]['OttLinks'] = eval(dict[i]['OttLinks'])
        if dict[i]['Director'] == 'null':
            dict[i]['Director'] = None
        else:
            dict[i]['Director'] = eval(dict[i]['Director'])

    return dict