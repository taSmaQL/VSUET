#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

std::vector<double> randomStuff;
std::vector<double> positiveStuff;
std::vector<double> negativeStuff;
std::vector<double> avgStuffPos;
std::vector<double> avgStuffNeg;
double input;
double amountPos;
double amountNeg;
double sumPos;
double sumNeg;
template <typename T> void wrVector(const std::vector<T>& randomStuff) {
	std::cout << "The source vector is: ";
	for (int i = 0; i < randomStuff.size(); i++)
		std::cout << std::fixed << std::setprecision(2)  << randomStuff[i] << " ";
}
template <typename T> void wrVectorPos(const std::vector<T>& positiveStuff) {
	std::cout << "The positive vector is: ";
	for (int i = 0; i < positiveStuff.size(); i++)
		std::cout << std::fixed << std::setprecision(2)  << positiveStuff[i] << " ";
}
template <typename T> void wrVectorNeg(const std::vector<T>& negativeStuff) {
	std::cout << "The negative vector is: ";
	for (int i = 0; i < negativeStuff.size(); i++)
		std::cout << std::fixed << std::setprecision(2) << negativeStuff[i] << " ";
}
template <typename T> void wrVectorAvgPos(const std::vector<T>& avgStuffPos) {
	std::cout << "The average positive vector is: ";
	for (int i = 0; i < avgStuffPos.size(); i++)
		std::cout << std::fixed << std::setprecision(2) << avgStuffPos[i] << " ";
}
template <typename T> void wrVectorAvgNeg(const std::vector<T>& avgStuffNeg) {
	std::cout << "The average negative vector is: ";
	for (int i = 0; i < avgStuffNeg.size(); i++)
		std::cout << std::fixed << std::setprecision(2) << avgStuffNeg[i] << " ";
}
int main() {

	double amountPos = 0;
	double amountNeg = 0;
	double sumPos = 0;
	double sumNeg = 0;

	std::cout << "Input your desire numbers (at least you must input one positive and one negative: " << std::endl;
	while (std::cin >> input) {
		randomStuff.push_back(input);
		if (input >= 0) {
			positiveStuff.push_back(input);
			amountPos += 1;
		}
		else {
			negativeStuff.push_back(input);
			amountNeg += 1;
		}
	}
	for (int i = 0; i < positiveStuff.size(); i++) {
		sumPos += positiveStuff[i];
	}
	for (int i = 0; i < negativeStuff.size(); i++) {
		sumNeg += negativeStuff[i];
	}
	avgStuffPos.push_back(sumPos / amountPos);
	avgStuffNeg.push_back(sumNeg / amountNeg);
	wrVector(randomStuff);
	wrVectorPos(positiveStuff);
	wrVectorNeg(negativeStuff);
	wrVectorAvgPos(avgStuffPos);
	wrVectorAvgNeg(avgStuffNeg);
	return 0;
}
