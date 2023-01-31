
s0: data/students.db
	python -B src/s0.py

# Create the students database
data/students.db:
	mkdir -p data
	python -B src/students.py

clean:
	rm data/students.db

copy:
	cp ../sqlite/src/students.py src
	cp ../sqlite/src/printit.py src
	cp ../sqlite/src/s0.py src
