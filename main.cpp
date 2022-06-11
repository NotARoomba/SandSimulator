#include <SDL.h>
#include <iostream>
#include "Grid.cpp"
#define FPS 60
#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600

bool running = true;
int main(int argc, char* argv[])
{
	SDL_Init(SDL_INIT_EVERYTHING);
	SDL_Window* window = SDL_CreateWindow("Sand Simulator", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
	SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, 0);
	Uint32 tick;
	const Uint8* keystates = SDL_GetKeyboardState(NULL);
	int xMouse, yMouse;
	Grid *grid = new Grid(SCREEN_WIDTH, SCREEN_HEIGHT);
	while (running) {
		SDL_Event event;
		tick = SDL_GetTicks();
		if (SDL_GetTicks() - tick < (1000 / FPS)) SDL_Delay(1000 / FPS - (SDL_GetTicks() - tick));
		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				running = false;
			}
			
		}
		SDL_PumpEvents();
		if (keystates[SDL_SCANCODE_W]) {
			SDL_GetGlobalMouseState(&xMouse, &yMouse);
			grid->addElement(*new Sand(xMouse, xMouse));
		}
		SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
		SDL_RenderClear(renderer);
		SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
		grid->draw(renderer);
		SDL_RenderPresent(renderer);
	}
	if (renderer) {
		SDL_DestroyRenderer(renderer);
	}
	if (window) {
		SDL_DestroyWindow(window);
	}
	SDL_Quit();
	return 0;
}