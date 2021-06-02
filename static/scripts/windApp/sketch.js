var drop = []

function setup() {
    var myCanvas = createCanvas(760,400);
    
    myCanvas.parent("map-wrapper");
    
    myCanvas.id('over')
    angleMode(DEGREES)
    myCanvas.rotate(90);
    
    
  for(var i = 0; i < 100; i++) {
    
    drop[i] = new Drop();
}

}

function draw() {
    clear()
    rect(0, 0, 180, 180);
    background(255,0,0,0)
    
    
    
    for(var i = 0; i < 100; i++) {
    
    drop[i].show();
    drop[i].update();
  }
}

function Drop() {
  
  this.x = random(50, width)
  this.y = random(0, height)
  
  this.show = function() {
   
    noStroke();
    fill(0);
    // triangle geom
    let x1 =  this.x
    let y1 = this.y
    
    triangle(x1, y1, x1 -10, y1 -10, x1 + 10, y1 - 10)
  }
  this.update = function() {
    
    this.speed = 1
    this.gravity = 1.05;
    this.y = this.y + this.speed*this.gravity;
    
    
    if (this.y > height) {
      this.y = random(0, -height);
      this.gravity = 0;
    }
  }
}


