CXXFLAGS	= -I$(IMAS_PREFIX)/include -pthread
LDFLAGS		= -L$(IMAS_PREFIX)/lib -limas-cpp -limas

all: hello

%: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)
