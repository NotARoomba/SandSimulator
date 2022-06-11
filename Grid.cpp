#include <vector>
#include "Element.cpp"

class Grid {
public:
	std::vector<std::vector<Element>> grid;
	void moveAll() {
		for (int i = 0; i < grid.size(); i++) {
			for (int j = 0; j < grid[i].size(); j++) {
				grid[i][j].move();
			}
		}
	}
};