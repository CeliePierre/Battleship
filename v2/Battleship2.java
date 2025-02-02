/*
    NAME: Célie Pierre
    COS 161, Spring 2022, Prof. Andrew Amorelli
    Project 04
    File Name: Battleship.java
*/

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;

public class Battleship2 {

	// Static panel and graphics so they can be used be all methods
	static DrawingPanel panel = new DrawingPanel(325, 650);   
	static Graphics g = panel.getGraphics();   
	// Variables used for sizing 
	static int MAX_CONSOLE = 60;
	static int GRID_SIZE = 25;
	static Color cWATER = new Color(32,42,68);
	static Color cSHIP = Color.GRAY;
	static Color cHIT = Color.GRAY;
	static Color cMISS = Color.RED;
	// Players
	static Player p1 = new Player(1);
	static Player p2 = new Player(2);

	public static void main(String[] args) {
		
		System.out.println("LET'S PLAY BATTLESHIP!\n");
		
		// Create empty boards
		fillBoard(p1);
		fillBoard(p2);
		drawBoard(p1);
		drawBoard(p2);
		
		// Must allow for players to place their own ships at the beginning
		placeShips(p1, 0);
		placeShips(p2, 0);
		
		// Play game
		int winner = playGame(p1, p2);
		
		// Declare winner
		System.out.println("\nGAME OVER!");
		System.out.println("Player " + winner + " wins!");
		
	}
	
	public static int playGame(Player p, Player opponent) {
		// Must use recursion to run the game
		// Allow for at 2 players, and alternate turns guessing
		char target = ' ';
		boolean validMove = false;
		boolean shipHit = false;
		String square = "";
		while (!validMove || shipHit) {
			// The base case should be all a player’s ships being destroyed
			if (checkWinner(opponent, 0)) {
				return p.getPlayer();
			} else {
				// The recursive case should be a player taking their turn
				System.out.print("Player " + p.getPlayer() + " - Choose your target: ");
				Scanner scan = new Scanner(System.in);
				square = scan.next().toUpperCase();
				validMove = validMove(opponent, square);
				if (validMove) {
					target = checkTarget(opponent, square);
					if (target == 'H') {
						shipHit = true;
					} else {
						shipHit = false;
					}
					opponent.board.put(square, target);
					drawBoard(opponent);
				}
			}
		}
		// Update board & pass turn to next player
		return playGame(opponent, p);
	}
	
	public static void fillBoard(Player p) {
		for (char r = 'A'; r <= 'J'; r++) {
			for (int c = 1; c <= 10; c++) {
				String square = "" + r + c;
				p.board.put(square, 'E'); 
			}
		}
	}

	public static void drawBoard(Player p) {
		// Must display the 10x10 game board using the DrawingPanel.
		
		// Clear board
		g.setColor(Color.WHITE);
		if (p.getPlayer() == 1) g.fillRect(1, 1, 325, 325); 
		if (p.getPlayer() == 2) g.fillRect(1, 325, 325, 325);
		// Prints labels
		g.setColor(Color.BLACK);
		g.setFont(new Font("Courier", Font.PLAIN, 22)); 
		if (p.getPlayer() == 1) g.drawString("P L A Y E R   1", 50, 45);
		if (p.getPlayer() == 2) g.drawString("P L A Y E R   2", 50, 600);
		g.drawString("A B C D E F G H I J", 25, 322);
		int y = 0;
		if (p.getPlayer() == 1) y = 70;
		if (p.getPlayer() == 2) y = 350;
		for (int i = 1; i <= 10; i++, y+=GRID_SIZE) {
			g.drawString("" + i, 280, y);
		}
		// Draw players' grid
		drawGrid(p);
	}
	
	public static void drawGrid(Player p) {
		int r, c, y = 0;
		Color sColor;
		if (p.getPlayer() == 1) y = 50;
		else if (p.getPlayer() == 2) y = 330;
		Iterator<String> itr = p.board.keySet().iterator();
		while (itr.hasNext()) {
			String square = itr.next();
			// Convert row and column
			r = rowNum(square);
			c = colNum(square);
			// Set color based on status
			if (p.board.get(square).equals('E')) sColor = cWATER; 		// Empty
			else if (p.board.get(square).equals('S')) sColor = cWATER; 	// Hidden ship
			else if (p.board.get(square).equals('H')) sColor = cHIT; 	// Hit
			else if (p.board.get(square).equals('M')) sColor = cMISS; 	// Miss
			else if (p.board.get(square).equals('X')) sColor = cSHIP; 	// Placing ships
			else sColor = Color.white;
			// Draw grid
			g.setColor(sColor);
			g.fillRect(25 + GRID_SIZE*c, y + GRID_SIZE*r, GRID_SIZE, GRID_SIZE);
			g.setColor(Color.BLACK);
			g.drawRect(25 + GRID_SIZE*c, y + GRID_SIZE*r, GRID_SIZE, GRID_SIZE);
		}
	}
	
	public static void placeShips(Player p, int n) {
		if (n < p.ships.length) {
			boolean validPlace = false;
			Scanner scan = new Scanner(System.in);
			String square = "";
			char vh = ' ';
			String vhChoice = "";
			
			// Get user input of ship placement
			while (!validPlace) {
				System.out.print("Player " + p.getPlayer() + 
						   "\nShip: " + p.ships[n] +
						   "\n Where would you like to place your " + p.ships[n].getShipName() + 
						   "?\n Enter a letter (A-J) and a number (1-10): ");
				square = scan.next().toUpperCase();
				System.out.print(" How would you like to place the ship?" + 
								 "\n Enter V for vertical or H for horizontal: ");
				vh = scan.next().toUpperCase().charAt(0);
				validPlace = validPlace(p, p.ships[n], square, p.ships[n].getShipSize(), vh);
			}
			// Update p.board
			placeShip(p, p.ships[n], square, p.ships[n].getShipSize(), vh);
			if (vh == 'V') vhChoice = "vertically";
			if (vh == 'H') vhChoice = "horitontally";
			System.out.println(" Your " + p.ships[n].getShipName() + 
							   " has been placed " + vhChoice + " on " + square + ".\n");
			// Update ship status
			p.ships[n].setShipPos(vh);
			p.ships[n].setShipStart(square);
			drawBoard(p);
			placeShips(p, n+1);
		} else {
			Iterator<String> itr = p.board.keySet().iterator();
			while (itr.hasNext()) {
				String square = itr.next();
				if (p.board.get(square) == 'X') {
					p.board.put(square, 'S');
				}
			}
			drawBoard(p);
		}
	}
	
	public static void placeShip(Player p, Ship ship, String square, int size, char vh) {
		if (size != 0) {
			// Place ship
			p.board.put(square, 'X');
			// Vertical placement
			if (vh == 'V') {
				ship.setShipSquares(square);
				placeShip(p, ship, toSquare(colNum(square), rowNum(square)+1), size-1, vh);
			// Horizontal placement
			} else if (vh == 'H') {
				ship.setShipSquares(square);
				placeShip(p, ship, toSquare(colNum(square)+1, rowNum(square)), size-1, vh);
			}
		}
	}
	
	public static boolean validPlace(Player p, Ship ship, String square, int size, char vh) {
		if (size == 0) {
			return true;
		} else if (p.board.get(square).equals('E')) {
			// Check vertical placement
			if (vh == 'V') {
				return validPlace(p, ship, toSquare(colNum(square), rowNum(square)+1), size-1, vh);
			// Check horizontal placement
			} else if (vh == 'H') {
				return validPlace(p, ship, toSquare(colNum(square)+1, rowNum(square)), size-1, vh);
			} else {
				System.out.println("Invalid placement. Please try again.");
				return false;
			}
		} else {
			System.out.println("Invalid placement. Please try again.");
			return false;
		}
	}
	
	public static boolean validMove(Player p, String square) {
		// Check if space is empty or has a ship
		if (p.board.get(square).equals('E') || p.board.get(square).equals('S')) {
			return true;
		} else {
			System.out.println("Invalid move. Please try again.");
			return false;
		}
	}
	
	public static boolean checkWinner(Player p, int i) {
		// Check if all ships have sunk
		if (i >= p.ships.length) {
			return true;
		} else if (i < p.ships.length) {
			if (p.ships[i].isSunk()) {
				return checkWinner(p, i+1);
			} else {
				return false;
			}
		}
		return false;
	}

	public static char checkTarget(Player p, String square) {
		// If guess is a Ship, update to Hit
		if (p.board.get(square).equals('S')) {
			// Add hit to ship
			for (int i = 0; i < p.ships.length; i++) {
				if (p.ships[i].getShipSquares().contains(square)) {
					p.ships[i].addHit();
					// Check if sunk or just hit
					if (p.ships[i].isSunk()) {
						System.out.println("You sunk Player " + p.getPlayer() + "'s " + 
											p.ships[i].getShipName() + "!");
					} else {
						System.out.println("Hit!");
					}
				}
			}
			return 'H';
		// If guess is Empty, update to Miss
		} else if (p.board.get(square).equals('E')) {
			System.out.println("Miss!");
			return 'M';
		// Else, invalid
		} else {
			System.out.println("Invalid Selection. Please try again.");
			return 'I';
			
		}
	}
	
	public static int colNum(String square) {
		char col = square.charAt(0);
		int colNum = -1;
		if (col == 'A') colNum = 0;
		else if (col == 'B') colNum = 1;
		else if (col == 'C') colNum = 2;
		else if (col == 'D') colNum = 3;
		else if (col == 'E') colNum = 4;
		else if (col == 'F') colNum = 5;
		else if (col == 'G') colNum = 6;
		else if (col == 'H') colNum = 7;
		else if (col == 'I') colNum = 8;
		else if (col == 'J') colNum = 9;
		return colNum;
	}
	
	public static int rowNum(String square) {
		String row = square.substring(1);
		int rowNum = -1;
		if (row.equals("1")) rowNum = 0;
		else if (row.equals("2")) rowNum = 1;
		else if (row.equals("3")) rowNum = 2;
		else if (row.equals("4")) rowNum = 3;
		else if (row.equals("5")) rowNum = 4;
		else if (row.equals("6")) rowNum = 5;
		else if (row.equals("7")) rowNum = 6;
		else if (row.equals("8")) rowNum = 7;
		else if (row.equals("9")) rowNum = 8;
		else if (row.equals("10")) rowNum = 9;
		return rowNum;
	}
	
	public static String toSquare(int colNum, int rowNum) {
		rowNum += 1;
		char colLetter = ' ';
		if (colNum == 0) colLetter = 'A';
		else if (colNum == 1) colLetter = 'B';
		else if (colNum == 2) colLetter = 'C';
		else if (colNum == 3) colLetter = 'D';
		else if (colNum == 4) colLetter = 'E';
		else if (colNum == 5) colLetter = 'F';
		else if (colNum == 6) colLetter = 'G';
		else if (colNum == 7) colLetter = 'H';
		else if (colNum == 8) colLetter = 'I';
		else if (colNum == 9) colLetter = 'J';
		String square = "" + colLetter + rowNum;
		return square;
	}
	
}
