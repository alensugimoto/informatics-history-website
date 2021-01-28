#!/bin/bash

echo "Hello, I will take the bonus_question_2.py python file and execute it to create a PDF you desire!"
echo ""
echo "This might take aound 20 seconds because our repository is packed with amazing content."
echo ""
echo "Sit back and get a coffee! "
python3 ./bonus_question_2.py > html-pages-to-latex.tex | grep -m 1 -o "abc" | grep -o "123"

pdflatex -interaction=nonstopmode html-pages-to-latex.tex | grep -m 1 -o "abc" | grep -o "123"

rm html-pages-to-latex.aux html-pages-to-latex.log html-pages-to-latex.tex | grep -m 1 -o "abc" | grep -o "123"



