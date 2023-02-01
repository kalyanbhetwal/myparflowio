#include <iostream>
#include "parflow/pfdata.hpp"
#include <fstream>
#include <string>
#include <cstdlib>

#include <ctime>
#include <chrono>
#include <algorithm>
#include <iostream>
#include<vector>

using namespace std;
using namespace std::chrono;


#include "helper_functions.inc"
int main(int argc, char **argv){
    std::cout <<"hello world"<<'\n';
    // PFData test("tests/inputs/press.init.pfb");
    // test.loadHeader();
    // test.loadData();
    // for(int z = 0; z < test.getNZ(); ++z){
    //     for(int y = 0; y < test.getNY(); ++y){
    //         for(int x = 0; x < test.getNX(); ++x){
    //             std::cout << (z,y,x)<<std::endl;
    //         }
    //         std::cout <<"------------------------"<<std::endl;
    //     }
    // }
    auto start = high_resolution_clock::now();
    std::string m_filename = argv[1];//"tests/inputs/press.init.pfb";
    std::string filename = argv[2];//"tests/inputs/output.init.pfb";
    #include "read_file.inc"
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    cout << "Time taken by function: "
         << duration.count() << " milliseconds" << endl;


}  