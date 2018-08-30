class Walker{
    constructor(x,y){
        this.radius = 10
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
        if((this.x == w / 2 && this.y == h / 2) || walk_iterator >= walk_length){
            stroke(255,235,59,200)
            fill(255,235,59,100)
        }
        polygon(this.x, this.y, this.radius, 6)
        strokeWeight(this.radius / 2)
        point(this.x, this.y)

        //function to create the polygon
        function polygon(x, y, radius, npoints) {
            var angle = TWO_PI / npoints;
            beginShape()
            for (var a = 0; a < TWO_PI; a += angle) {
                var sx = x + cos(a) * radius
                var sy = y - sin(a) * radius
                vertex(sx, sy)
            }
            endShape(CLOSE)
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
    }

    getX(){return this.x}
    getY(){return this.y}
}

let bee
let w = 600
let h = 600
let walk_length = 16
let walk_iterator = 1
let max_iterations = 500
let iterator = 1
let expected = 0
let sixtyFourDone = false

function setup(){
    let beehive = createCanvas(600,600)
    beehive.parent('beehive')

    res1 = document.querySelector('#res1')
    res3 = document.querySelector('#res3')
    console.log(res1);

    background(51)
    frameRate(100)
    bee = new Walker(width/2, height/2)
}

function draw(){
    background(51)
    bee.display()
    if(iterator >= max_iterations){
        noLoop()
        if(!sixtyFourDone){
            walk_length = 64
            iterator = 1
            sixtyFourDone = true
            loop()
        }
    }
    while(walk_iterator <= walk_length){
        bee.move()
        bee.display()
        walk_iterator++
    }

    expected += dist(bee.getX(), bee.getY(), width / 2, height / 2) / max_iterations / bee.radius
    console.log("dist = ", dist(bee.getX(), bee.getY(), width / 2, height / 2) / bee.radius,"expected = ", expected)
    if(!sixtyFourDone){
        res1.innerHTML = int(expected)
    }else{
        res3.innerHTML = int(expected)
    }

    bee = new Walker(width/2,height/2)
    walk_iterator = 1
    iterator++
}
