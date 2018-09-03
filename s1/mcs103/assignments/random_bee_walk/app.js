// Template class for our Bee and its Environment
class Walker{
    constructor(x,y){
        this.radius = 10    // Size of a hexagon in the grid
        this.x = x          // Current position of the Walker
        this.y = y
        this.prevx = x      // Last position of the Waker
        this.prevy = y
    }

    //Creates a grid and positions the Walker in that grid
    display(){

        //line from previous hexagon to current hexagon
        strokeWeight(2)
        stroke(255,235,59,200)
        line(this.prevx, this.prevy, this.x, this.y)

        //drawing the Hexagon where the Walker is at
        stroke(255,255,255,150)
        fill(255,255,255,100)
        //First and the last hexagon on the path gets a special color
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
                //the canvas where the grid is is drawn has an inverted y axis
                //hence the y is increased in the opposite direction
                var sy = y - sin(a) * radius
                vertex(sx, sy)
            }
            endShape(CLOSE)
        }
    }

    //Moves the Walker to the next Hexagon based on probability
    move(){
        let random_var = floor(random(6))
        let theta = (random_var * 60) + 30
        //30-Degrees added since walk happens across the center of each edge of the Hexagon
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
let w = 600                 //Width of the grid in pixels
let h = 600                 //Height of the grid in pixels
let bar                     //Visual Element: Progressbar
let walk_length = 16        //Lenght of the Path
let walk_iterator = 1       //Iterator for the Path
let max_iterations = 1000  
let iterator = 1
let expected = 0            
let secondIteration = false 
let distanceList = []       //Distances between start and end position for each iteration

//Setting up the Environment
function setup(){
    let beehive = createCanvas(w,h)
    beehive.parent('beehive')

    res1 = document.querySelector('#res1')
    res2 = document.querySelector('#res2')
    res3 = document.querySelector('#res3')
    res4 = document.querySelector('#res4')

    bee = new Walker(width/2, height/2)

    background(51)
    frameRate(100)

    //Visual Element : Progress of the Iterations
    bar = new ProgressBar.Line(progressBar, {
        strokeWidth: 4,
        easing: 'easeInOut',
        duration: 1400,
        color: '#333',
        trailColor: '#FFEB3B',
        trailWidth: 4,
        svgStyle: {width: '100%', height: '100%'}
    });
    bar.animate(0)
      
}

//This function executes according to the framerate
//and executes until noLoop() is called.
function draw(){
    background(51)

    //Every iteration for a particular walk_length has been completed
    if(iterator > max_iterations){
        noLoop()
        console.log(distanceList);

        let sd = standardDeviation(distanceList)
        
        if(secondIteration){
            res4.innerHTML = sd.toFixed(2)
        }else{
            res2.innerHTML = sd.toFixed(2)
        }

        //if second iteration has not been done then reset
        //all the variables and initiate second iteration
        if(!secondIteration){
            distanceList = []
            expected = 0
            walk_length = 64
            iterator = 1
            secondIteration = true
            bar.animate(0)
            loop()
        }else{
            return
        }
    }

    //For a particular iteration generate a Path for the Walker
    while(walk_iterator <= walk_length){
        bee.move()
        bee.display()
        walk_iterator++
    }

    //Calculate Distance between start and finish positions
    //of the Path and then update the Expected value accordingly.
    //Since the distance calculated is pixel based hence there is 
    //a need to divide it by the distance between 2 Hexagons.
    let dist2Hex = bee.radius * cos(radians(30))
    let distance = dist(bee.getX(), bee.getY(), w / 2, h / 2) / dist2Hex
    distanceList.push(distance)
    expected += distance / max_iterations
    if(!secondIteration){
        res1.innerHTML = expected.toFixed(2)
    }else{
        res3.innerHTML = expected.toFixed(2)
    }

    //Reset the Bee to the start position
    bee = new Walker(width/2,height/2)
    walk_iterator = 1

    //Go to the next iteration and update ProgressBar
    iterator++
    bar.set(iterator / 1000)
}


//Helper Functions

function standardDeviation(values){
    var avg = average(values);
    
    console.log("Expected Value",avg)

    var squareDiffs = values.map(function(value){
      var diff = value - avg;
      var sqrDiff = diff * diff;
      return sqrDiff;
    });
    
    var avgSquareDiff = average(squareDiffs);
  
    var stdDev = Math.sqrt(avgSquareDiff);
    return stdDev;
}
  
function average(data){
    var sum = data.reduce(function(sum, value){
        return sum + value;
    }, 0);

    var avg = sum / data.length;
    return avg;
}