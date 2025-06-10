kth Closest Points from Origin. 
Kth Closes Points from Origin. 

Distance Calculation. 
// Sorting based on the distance and Getting only K points. 
Distance Caclution. 

private void kClosestPoints() {
	Arrays.sort(array, (a, b) -> distance(a) - distance(b)); // What is main things we are doing? 
	return Arrays.copyOf(array, k); What are we retuning? 
}
private int distance(int[] points){
	return points[0] * points[0] + points[1] * points[1];
}
