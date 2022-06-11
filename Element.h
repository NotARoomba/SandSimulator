#pragma once
#include <vector>
#include <SDL.h>
	class Element {
	public:
		int x, y;
		int r, g, b;
		bool isMoveable = false;
		Element() {};
		virtual void move(std::vector<std::vector<Element>> grid) {};
		void draw(SDL_Renderer* renderer) {
			SDL_SetRenderDrawColor(renderer, r, g, b, 255);
			SDL_Rect rect = { x, y, 10, 10 };
			SDL_RenderFillRect(renderer, &rect);
		}

	};