
#!/bin/bash

[[ $(pip show nwdiag) ]] || pip install -r requirements.txt

if [ ! -f ~/.blockdiagrc ]; then 

cat << EOF > $HOME/.blockdiagrc
[nwdiag]
fontpath = $HOME/Library/Fonts/Hack-Regular.ttf
EOF

fi
cat $HOME/.blockdiagrc

echo '\nSetup complete.'
