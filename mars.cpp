#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
#define MAXX 7000;
#define MAXY 3000;

struct Point{
    public:
        int x;
        int y;
};

class Land{
private:
    vector<Point> points;
    Point flat_left;
    Point flat_right;
    void compute_flat(){
        for(int i=0; i<points.size() - 1; ++i){
            if (points[i].y == points[i + 1].y)
            {
                flat_left = points[i];
                flat_right = points[i + 1];
            }
        }
    }
public:
    Land(vector<Point>& points){
        this->points = points;
        compute_flat();
    }


};

class Lander(){
public:
    int x, y, hs, vs, f, r, p;
    




}


int main()
{
    int N; // the number of points used to draw the surface of Mars.
    cin >> N; cin.ignore();
    for (int i = 0; i < N; i++) {
        int LAND_X; // X coordinate of a surface point. (0 to 6999)
        int LAND_Y; // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        cin >> LAND_X >> LAND_Y; cin.ignore();
    }

    // game loop
    while (1) {
        int X;
        int Y;
        int HS; // the horizontal speed (in m/s), can be negative.
        int VS; // the vertical speed (in m/s), can be negative.
        int F; // the quantity of remaining fuel in liters.
        int R; // the rotation angle in degrees (-90 to 90).
        int P; // the thrust power (0 to 4).
        cin >> X >> Y >> HS >> VS >> F >> R >> P; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;

        cout << "-20 3" << endl; // R P. R is the desired rotation angle. P is the desired thrust power.
    }
}