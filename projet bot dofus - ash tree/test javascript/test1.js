var bot=require('robotjs');

var tree1_x=650;
var tree1_y=350;
var tree2_x=1130;
var tree2_y=230;

function wood() {
    // juste pour deco (shhh...)
    console.log("starting...");

    sleep(4000);

    num_de_rep=0
    // loop inf test debut avc coord arbre 1 et 2
    while(num_de_rep < 5){
        bot.moveMouseSmooth(tree1_x, tree1_y);
        bot.mouseClick();

        //up pour arbre lvl plus haut
        sleep(2000);

        bot.moveMouseSmooth(tree2_x, tree2_y,);
        bot.mouseClick();

        num_de_rep=num_de_rep+1;
        
    else{
        stop;
    }
    }
}

function sleep(ms) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
}

wood();