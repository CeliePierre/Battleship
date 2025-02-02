import java.util.Map;
import java.util.TreeMap;

/*
    NAME: Célie Pierre
    COS 161, Spring 2022, Prof. Andrew Amorelli
    Project 04
    File Name: Ship.java
*/

public class Player {
	
	public Map<String, Character> board;
	public Ship[] ships;
	private int player;
	
	// Constructor
	public Player(int p) {
		setPlayer(p);
		board = new TreeMap<String, Character>();
		ships = new Ship[5];
		ships[0] = new Ship("Carrier");
		ships[1] = new Ship("Battleship");
		ships[2] = new Ship("Destroyer");
		ships[3] = new Ship("Submarine");
		ships[4] = new Ship("Patrol Boat");
	}

	public int getPlayer() {
		return player;
	}

	private void setPlayer(int player) {
		this.player = player;
	}

	public Map<String, Character> getBoard() {
		return board;
	}

	public Ship[] getShips() {
		return ships;
	}

}
