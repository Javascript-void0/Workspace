void setup() {
    size(1000,1000);
    background(0);
    int c = (int) 255;
    final int count = floor(random(100,150));
    final int layers = floor(random(4,8));
    strokeWeight(0.25);
    noFill();
    Circle[] circles = new Circle[count];
    for (int l = 0; l < layers; l++) {
        float c1 = floor(c * l / layers);
        stroke(c1);

        for (int i = 0; i < circles.length; i++) {
            float x = random(width);
            float y = random(height);
            float r = random(60,100);
            circles[i] = new Circle(x,y,r);
        }

        for (int i = 0; i < circles.length; i++) {
            point(circles[i].x, circles[i].y);
            for (int j = 0; j < circles.length; j++) {
                if (circles[i].isIntersecting(circles[j]) == true) {
                    line(circles[i].x, circles[i].y, circles[j].x, circles[j].y);
                }
            }
        }
    }
}