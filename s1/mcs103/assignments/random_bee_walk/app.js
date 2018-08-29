class Walker{
    constructor(x,y){
        this.radius = 20
        this.x = x
        this.y = y
        this.prevx = x
        this.prevy = y
    }

    display(){
        //line from previous hexagon to current hexagon
        strokeWeight(2)
        stroke(255,235,59,200)
        line(this.prevx, this.prevy, this.x, this.y)

        //draw current hexagon
        stroke(255,255,255,150)
        fill(255,255,255,100)
        if((this.x == w / 2 && this.y == h / 2) || iterator > max_iteration){
            stroke(255,235,59,200)
            fill(255,235,59,100)
        }
        polygon(this.x, this.y, this.radius, 6)
        strokeWeight(this.radius / 2)
        point(this.x, this.y)

        //function to create the polygon
        function polygon(x, y, radius, npoints) {
            var angle = TWO_PI / npoints;
            beginShape();
            for (var a = 0; a < TWO_PI; a += angle) {
                var sx = x + cos(a) * radius;
                var sy = y - sin(a) * radius;
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
        this.x = this.x + 2 * this.radius * Math.cos(radians(theta))
        //y is negated because the y axis is inverted
        this.y = this.y - 2 * this.radius * Math.sin(radians(theta))
        console.log(theta)
    }
}

let bee
let w = 600
let h = 600
max_iteration = 16
iterator = 1

function setup(){
    let beehive = createCanvas(600,600)
    beehive.parent('beehive')
    background(51)
    // frameRate(1)
    bee = new Walker(width/2, height/2)
    bee.display()
}

function draw(){
    // background(51)
    iterator++
    if(iterator > max_iteration){
        noLoop()
    }
    bee.move()
    bee.display()
}
