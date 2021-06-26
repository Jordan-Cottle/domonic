test:
	python3 -m unittest tests.test_html
	python3 -m unittest tests.test_dom
	python3 -m unittest tests.test_style
	python3 -m unittest tests.test_javascript
	python3 -m unittest tests.test_terminal
	python3 -m unittest tests.test_CDN
	python3 -m unittest tests.test_JSON
	python3 -m unittest tests.test_svg
	python3 -m unittest tests.test_collada
	python3 -m unittest tests.test_x3d
	python3 -m unittest tests.test_dQuery
	python3 -m unittest tests.test_geom

build:
	rm -r dist/
	python3 setup.py sdist bdist_wheel
	rm -r build/

deploy:
	rm -r dist/
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -r build/