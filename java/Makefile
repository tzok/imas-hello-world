all: target/hello.jar

clean:
	$(RM) -r target

run: target/hello.jar
	java -cp $(CLASSPATH):$< pl.psnc.imas.HelloWorld

target/hello.jar: target/classes/pl/psnc/imas/HelloWorld.class
	jar --create --file $@ --main-class pl.psnc.imas.HelloWorld -C target/classes pl/psnc/imas/HelloWorld.class

target/classes/%.class: src/%.java
	javac -d target/classes $^
