class Walker{
    constructor(x,y){
        this.radius = 10
        this.x = x
        this.y = y
        this.prevx = x
        this.prevy = y
    }

    display(){
        stroke(255,235,59,200)
        line(this.prevx, this.prevy, this.x, this.y)
        stroke(255,255,255,150)
        fill(255,255,255,100)
        if((this.x == w / 2 && this.y == h / 2) || iterator > max_iteration){
            stroke(255,235,59)
            fill(255,235,59)
        }
        // strokeWeight(this.radius)
        polygon(this.x, this.y, this.radius, 6)

        function polygon(x, y, radius, npoints) {
            var angle = TWO_PI / npoints;
            beginShape();
            for (var a = 0; a < TWO_PI; a += angle) {
                var sx = x + cos(a) * radius;
                var sy = y + sin(a) * radius;
                vertex(sx, sy);
            }
            endShape(CLOSE);
        }
    }

    move(){
        let random_var = floor(random(6))
        let theta = (random_var * 60) + 30
        this.prevx = this.x
        this.prevy = this.y
        this.x = this.x + 2 * this.radius * Math.cos(radians(theta - 60))
        this.y = this.y + 2 * this.radius * Math.sin(radians(theta - 60))
        console.log(theta)
    }
}

let bee
let w = 600
let h = 600
max_iteration = 64
iterator = 1

function setup(){
    createCanvas(600,600)
    background(51)
    frameRate(10)
    bee = new Walker(width/2, height/2)
}

function draw(){
    // background(51)
    bee.display()
    bee.move()
    if(iterator > max_iteration){
        noLoop()
    }
    iterator++
}
