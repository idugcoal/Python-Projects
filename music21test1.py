from music21 import *

catalog = stream.Opus()
for workName in corpus.getBachChorales():
    work = converter.parse(workName)
    firstTS = work.flat.getTimeSignatures()[0]
    if firstTS.ratioString == '6/8':
        catalog.append(work.measureRange(0,2))
catalog.show()
