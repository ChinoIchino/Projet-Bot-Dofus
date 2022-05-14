var bot=require('robotjs');


function main() {
    console.log("Starting...");
    sleep(4000);
    while (true) {
        var arbre = trouve_arbre();
        if (arbre == false) {
            sleep(4000);
            continue;
        }
        bot.moveMouse(arbre.x, arbre.y);
        bot.mouseClick();
}

}

function screencap(){
    sleep(3000);

    var scrn=bot.screen.capture(0, 0, 1920, 1080);

    //take color to start code
    var pixel_color=scrn.colorAt(1270,216);
    console.log(pixel_color);
}

function trouve_arbre(){
    sleep(4000);
    //base de donnes couleur d'arbre
    var x=420, y=70, height=1000, width=1530;
    var scrn = bot.screen.capture(x, y, width, height);
    var couleur_arbre=["#352c18","#a59247","#f7ffff","#625934"];
    for (var i=0; i<500; i++) {
        var random_x=getRandomInt(0,width-1);
        var random_y=getRandomInt(0,height-1);
        var sample=scrn.colorAt(random_x,random_y);
        console.log("Starting&&&...");
        if (couleur_arbre.includes(sample)){
            var screen_x=random_x+x;
            var screen_y=random_y+y;
            console.log("Starting--...");
            console.log("un arbre a etait trouver en:"+screen_x+","+screen_y+"avec la couleur"+sample);
            bot.moveMouse(arbre.x, arbre.y);
            bot.mouseClick();
            console.log("YESSSS...");
            return {x:screen_x, y:screen_y};
        }
    }
    return false
}

function getRandomInt(min, max) {
    // inclusive of min and max
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function sleep(ms) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
}

main()

//screencap()
