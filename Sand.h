#pragma once
#include "Element.h"
	class Sand : public Element {
	public:
		Sand(int x, int y) {
			this->x = x;
			this->y = y;
			this->r = 0.5;
			this->g = 0.5;
			this->b = 0.5;
		}
		void move(std::vector<std::vector<Element>> grid) {
			{
				if (this->isMoveable) {
					if (grid[x][y + 1].x != NULL) {
						y++;
					}
					else if (grid[x - 1][y + 1].x != NULL) {
						x--;
						y++;
					}
					else if (grid[x + 1][y + 1].x != NULL) {
						x++;
						y++;
					}
				}
			};
		};
	};