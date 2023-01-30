#include <iostream>
#include "parflow/pfdata.hpp"
#include <fstream>
#include <string>
#include <cstdlib>

#include <ctime>
#include <chrono>
#include <algorithm>
#include "helper_functions.inc"
int main(void){
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
    std::string m_filename = "tests/inputs/press.init.pfb";
    std::string filename = "tests/inputs/output.init.pfb";
    #include "read_file.inc"


}  