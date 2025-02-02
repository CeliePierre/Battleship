import java.util.*;

/*
    NAME: Celie Pierre
    COS 161, Spring 2022, Prof. Andrew Amorelli
    Project 04
    File Name: Ship.java
*/

public class Ship {

	private String shipName;
	private boolean isSunk;
	private int shipSize;
	private char shipPos = ' ';
	private String shipStart;
	private int shipHits;
	private int shipRow;
	private int shipCol;
	private int shipCoord;
	private Set<String> shipSquares = new HashSet<String>();
	
	// Constructor
	public Ship(String shipName) {
		setShipName(shipName);
		setSunk(false);
		setShipSize(shipName);
	}
	
	public String toString() {
		return getShipName() + " (size " + getShipSize() + ")";
	}
	
	public String getShipStart() {
		return shipStart;
	}

	public void setShipStart(String shipStart) {
		// Top of ship
		setShipRow(shipStart.charAt(0));
		setShipCol(Integer.parseInt(shipStart.substring(1)));
		setShipCoord();
		this.shipStart = shipStart;
	}
	
	public String getShipName() {
		return shipName;
	}

	public void setShipName(String shipName) {
		this.shipName = shipName;
	}

	public boolean isSunk() {
		if (getShipSize() == getShipHits()) {
			isSunk = true;
		} else {
			isSunk = false;
		}
		return isSunk;
	}

	public void setSunk(boolean isSunk) {
		this.isSunk = isSunk;
	}
	
	public int getShipSize() {
		return shipSize;
	}

	public void setShipSize(String shipName) {
		if (shipName == "Carrier")
			this.shipSize = 5;
		if (shipName == "Battleship")
			this.shipSize = 4;
		if (shipName == "Destroyer")
			this.shipSize = 3;
		if (shipName == "Submarine")
			this.shipSize = 3;
		if (shipName == "Patrol Boat")
			this.shipSize = 3;
	}

	public char getShipPos() {
		return shipPos;
	}
	
	public int getShipHits() {
		return shipHits;
	}
	
	public void addHit() {
		this.shipHits += 1;
	}

	public void setShipPos(char shipPos) {
		// Vertical or horizontal
		this.shipPos = shipPos;
	}
	
	public Set<String> getShipSquares() {
		return shipSquares;
	}

	public void setShipSquares(String square) {
		this.shipSquares.add(square);
	}

	public int getShipRow() {
		return shipRow;
	}

	public void setShipRow(int shipRow) {
		this.shipRow = shipRow;
	}

	public int getShipCol() {
		return shipCol;
	}

	public void setShipCol(int shipCol) {
		this.shipCol = shipCol;
	}

	public int getShipCoord() {
		return shipCoord;
	}

	public void setShipCoord() {
		// Row x Col
		int rowNum = getShipRow() - 1;
		int colNum = -110;
		if (getShipCol() == 'A') colNum = 0;
		if (getShipCol() == 'B') colNum = 1;
		if (getShipCol() == 'C') colNum = 2;
		if (getShipCol() == 'D') colNum = 3;
		if (getShipCol() == 'E') colNum = 4;
		if (getShipCol() == 'F') colNum = 5;
		if (getShipCol() == 'G') colNum = 6;
		if (getShipCol() == 'H') colNum = 7;
		if (getShipCol() == 'I') colNum = 8;
		if (getShipCol() == 'J') colNum = 9;
		if (rowNum == 0) 
			rowNum = 110;
		if (rowNum > 0 && rowNum < 10)
			rowNum *= 100;
		this.shipCoord = rowNum + colNum;
	}

}
