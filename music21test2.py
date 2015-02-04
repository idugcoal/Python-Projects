from music21 import *
results = stream.Stream()
for chorale in corpus.chorales.Iterator():
    keyObj = chorale.analyze('key')
    if keyObj.mode == 'minor':
        lastChordPitches = []
        for part in chorale.parts:
                lastChordPitches.append(part.flat.pitches[-1])
        cLast = chord.Chord(lastChordPitches)
        cLast.duration.type = "whole"
        cLast.transpose("P8", inPlace=True)
        if cLast.isMinorTriad() or cLast.isIncompleteMinorTriad():
            cLast.lyric = chorale.metadata.title
            m = stream.Measure()
            m.keySignature = chorale.flat.getElementsByClass(
                'KeySignature')[0]
            m.append(cLast)
            results.append(m.makeAccidentals(inPlace=True))
