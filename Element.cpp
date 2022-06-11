#include <vector>
class Element {
	public:
		struct {
			float x, y;
		} pos;
		struct  {
			float r, g, b;
		} color;
		bool isMoveable;
		void move(std::vector<std::vector<Element>> grid) {
			if (isMoveable) {
				if (grid[pos.x][pos.y + 1].pos.x != NULL) {
					pos.y++;
				}
			}
		}
	
};