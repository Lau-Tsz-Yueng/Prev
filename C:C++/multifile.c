CFILES =\
    factorial.c\
    squareroot.c\
    exponential.c

HFILES =\
    factorial.h\
    squareroot.h\
    exponential.h

all: calc.exe rpn.exe

calc.exe: calcmain.c $(CFILES) $(HFILES)
    gcc calcmain.c $(CFILES) -o calc.exe

rpn.exe: rpnmain.c $(CFILES) $(HFILES)
    gcc rpnmain.c $(CFILES) -o rpn.exe