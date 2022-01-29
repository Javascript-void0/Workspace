void setup() {
  size(1500,1500);
  noStroke();
  frameRate(500);
} 
void draw() {
  background(0);
  surface.setTitle("FPS: " + frameRate);
  for (int i = 0; i < 50; i++) {
    float x = random(width/5);
    float y = random(height/5);
    fill((x+y)/2);
    ellipse(x*5,y*5,x*5+random(5,10),y*5+random(5,10));
  }
}
