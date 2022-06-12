#pragma once
#include <iostream>
#include "Element.h"
	class Sand : public Element {
	public:
		Sand(int _x, int _y) : Element(_x, _y) {
			x = _x;
			y = _y;
			r = 255;
			g = 255;
			b = 255;
			isMoveable = true;
			drawable = true;
		}
		void move(std::vector<std::vector<Element>> grid) {
			{
				if (isMoveable) {
					if (grid[x][y + 1].x != 0) {
						y++;
					}
					else if (grid[x - 1][y + 1].x != 0) {
						x--;
						y++;
					}
					else if (grid[x + 1][y + 1].x != 0) {
						x++;
						y++;
					}
				}
			};
		};
		void draw(SDL_Renderer* renderer) {
			SDL_SetRenderDrawColor(renderer, r, g, b, 255);
			SDL_Rect rect = { x, y, 10, 10 };
			SDL_RenderFillRect(renderer, &rect);
		}
	};