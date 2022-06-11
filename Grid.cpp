#pragma once
#include <vector>
#include <SDL.h>
#include "Element.h"
#include "Sand.h"

class Grid {
public:
	std::vector<std::vector<Element>> grid;
	Grid::Grid(int width, int height) {
		grid.resize(width);
		for (int i = 0; i < width; i++) {
			grid[i].resize(height);
		}
	};
	void Grid::moveAll() {
		for (int i = 0; i < grid.size(); i++) {
			for (int j = 0; j < grid[i].size(); j++) {
				grid[i][j].move(grid);
			}
		}
	};
	/*void Grid::addElement(Element e) {
		grid.push_back(std::vector<Element>());
		grid[grid.size() - 1].push_back(e);
	};*/
	void Grid::addElement(Sand e) {
		grid.push_back(std::vector<Element>());
		grid[grid.size() - 1].push_back(e);
	};
	void Grid::draw(SDL_Renderer* renderer) {
		for (int i = 0; i < grid.size(); i++) {
			for (int j = 0; j < grid[i].size(); j++) {
				grid[i][j].draw(renderer);
			}
		}
	};
};