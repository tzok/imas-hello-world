CXXFLAGS	= -I$(IMAS_PREFIX)/include -pthread $(shell pkg-config --cflags blitz)
LDFLAGS		= -L$(IMAS_PREFIX)/lib $(shell pkg-config --libs blitz) -limas-cpp -limas

all: hello

%: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)
