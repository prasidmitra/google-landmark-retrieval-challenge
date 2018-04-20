#include<stdio.h>
#include<iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/xfeatures2d.hpp>
#include <dirent.h>
#include <chrono>
using namespace cv;
using namespace cv::xfeatures2d;
using namespace std::chrono;
int main(int argc, char** argv) {
  if (argc < 2){
	std::cout << "Please pass the image folder,\n";
	return 0;
  }
  auto start = high_resolution_clock::now();
  std::string image_folder= argv[1];
  DIR *dirp;
  struct dirent *directory;
  dirp = opendir(image_folder.c_str());
  if (dirp) {
	while ((directory = readdir(dirp)) != NULL) {
	  Mat image;
	  std::string image_path = image_folder + directory->d_name;
	  image = imread(image_path, IMREAD_GRAYSCALE);
	  Ptr<SURF> detector = SURF::create(400);
	  std::vector<KeyPoint> kp;
	  detector->detect(image, kp);
	} 	
  }
  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  std::cout << duration.count()<<std::endl;
  
  
  
  waitKey(0);
  return 0;
}
