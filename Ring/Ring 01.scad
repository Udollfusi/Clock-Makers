hole_angle = 35;
difference(){
    cylinder(h=16,r=32,center=true);
    cylinder(h=18,r=28,center=true);
    translate([0,27,0]){
        cylinder(h=18,r=2,center=true);
    }
    translate([30*cos(hole_angle),30*sin(hole_angle),0]){
        rotate([0,90,hole_angle]){
            cylinder(h=8,r=3,center=true);
        }
    }
}