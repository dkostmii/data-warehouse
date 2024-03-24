DIAGRAM_THEME := plain
DIAGRAM_FONT := "Times New Roman"
DIAGRAM_DPI := 300

all: diagrams

diagrams:
	plantuml docs/diagrams/src/*.pu -o ../out -theme $(DIAGRAM_THEME) -SDefaultFontName=$(DIAGRAM_FONT) -Sdpi=$(DIAGRAM_DPI) -Idocs/diagrams/settings.puml -progress -duration -checkmetadata -charset utf-8 -tpng -failfast

insert-gen:
	cd src/insert-gen && pipenv run python main.py
