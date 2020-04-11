function Neuron(x, y) 
{

    this.position = createVector(x, y);
    this.connections = [];
    this.sum = 0;
    this.r = 32;
    //this connects the nodes with one another
    this.addConnection = function(c) 
    {
      this.connections.push(c);
    }
  
    this.feedforward = function(input) 
    {
      this.sum += input;
      if (this.sum > 4)//gap between the spwan of packets
     {
        this.fire();
        this.sum = 0;
      }
    }
    //this fires the nodes
    this.fire = function() 
    {
      this.r = 48;
  
      for (var i = 0; i < this.connections.length; i++) 
      {
         this.connections[i].feedforward(this.sum);
        
      }
    }
  
    this.display = function() 
    {
      //controls the appearances of the nodes
      fill('yellow');
      stroke(0);
      strokeWeight(1);
      //shape of the nodes
      ellipse(this.position.x, this.position.y, this.r, this.r);
      //the sudden bulge while firing
      this.r = lerp(this.r,32,0.1);
    }
  }
  