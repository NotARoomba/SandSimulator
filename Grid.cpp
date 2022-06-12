#pragma once
#include <vector>
#include <iostream>
#include <SDL.h>
#include "Element.h"
#include "Sand.h"

class Grid {
public:
	std::vector<std::vector<Element>> grid;
	Grid::Grid(int width, int height) {
		grid.resize(height);
		for (int i = 0; i < height; i++) {
			grid[i].resize(width);
		}
	};
	void Grid::moveAll(std::vector<Element> temp) {
		for (int i = 0; i < grid.size(); i++) {
			for (int j = 0; j < grid[i].size(); j++) {
				if (grid[i][j].isMoveable && grid[i][j].x != 0) {
					grid[i][j].move(grid);
				}
			}
		}
	};
	/*void Grid::addElement(Element e) {
		grid.push_back(std::vector<Element>());
		grid[grid.size() - 1].push_back(e);
	};*/
	void Grid::addElement(Sand e) {
		std :: cout << "adding sand" << std::endl;
		grid[e.y][e.x] = e;	
	};
	void Grid::draw(SDL_Renderer* renderer) {
		for (int i = 0; i < grid.size(); i++) {
			for (int j = 0; j < grid[i].size(); j++) {
				if (grid[i][j].drawable) {
					SDL_SetRenderDrawColor(renderer, grid[i][j].r, grid[i][j].g, grid[i][j].b, 255);
					SDL_RenderDrawPoint(renderer, grid[i][j].x, grid[i][j].y);
				}
			}
		}
	};
};