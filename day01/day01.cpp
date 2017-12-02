#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <boost/range/combine.hpp>
using namespace std;

int inverse_captcha(string input, int shift) {
  vector<int> data(input.length());
  transform(input.begin(), input.end(), data.begin(),
            [](char x) { return x - '0'; });
  
  int N = input.length();
  vector<int> shifted (data);
  rotate(shifted.begin(), shifted.end() - shift, shifted.end());

  int total = 0;
  for (auto tup : boost::combine(data, shifted)) {
    int a, b;
    boost::tie(a, b) = tup;
    if (a == b) {
      total += a;
    }
  }
  return total;
}

int main()
{
  string input;
  ifstream input_file ("input.txt");
  getline(input_file, input);
  cout << inverse_captcha(input, 1) << endl;
  cout << inverse_captcha(input, input.length() / 2) << endl;
}
