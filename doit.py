from chord2note import chord2note
from note2chord import note2chord
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def doit():
    return render_template('home.html')


@app.route('/search', methods=['POST'])
def dosearch() -> 'html':
    name = request.form['name']
    Mmad = request.form['Mmad']
    sharpflat = request.form['sharpflat']
    noteres = chord2note(name, Mmad, sharpflat)

    note1st = request.form['note1st']
    note2nd = request.form['note2nd']
    note3rd = request.form['note3rd']
    chordres = note2chord(note1st, note2nd, note3rd)
    return render_template('results.html',
                           note1st=noteres[0],
                           note2nd=noteres[1],
                           note3rd=noteres[2],
                           thechord=chordres)


app.run(debug=True)
