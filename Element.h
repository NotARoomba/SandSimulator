#pragma once
#include <vector>
#include <SDL.h>
	class Element {
	public:
		int x, y;
		int r, g, b;
		bool isMoveable = false;
		bool drawable = false;
		Element(int _x, int _y) {
			x = _x;
			y = _y;
			r = 0;
			g = 0;
			b = 0;
		};
		Element() {};
		virtual void move(std::vector<std::vector<Element>> grid) {};
	};