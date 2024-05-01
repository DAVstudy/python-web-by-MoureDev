.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
Remove-Item public -Force -Recurse
reflex init
reflex export --frontend-only
Expand-Archive frontend.zip -DestinationPath public
Remove-Item frontend.zip -Force
deactivate