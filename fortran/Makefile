FC		= gfortran
FFLAGS	= -I$(IMAS_PREFIX)/include/gfortran
LDFLAGS	= -L$(IMAS_PREFIX)/lib -limas-gfortran -limas

all: hello

%: %.f90
	$(FC) $(FFLAGS) -o $@ $^ $(LDFLAGS)
