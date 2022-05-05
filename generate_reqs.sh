jupyter nbconvert --output-dir="./py" --to script *.ipynb
pipreqs "./py"
mv ./py/requirements.txt .
rm -rf "./py"
