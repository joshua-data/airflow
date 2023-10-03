FRUIT=$1
if [ $FRUIT == APPLE ];then
    echo "You selected Apple!"
elif [ $FRUIT == ORANGE ];then
    echo "You selected Orange!"
elif [ $FRUIT == GRAPES ];then
    echo "You selected Grapes!"
else
    echo "You selected other fruits!"
fi
