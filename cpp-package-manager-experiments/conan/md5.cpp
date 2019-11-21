#include <boost/program_options.hpp>
#include "Poco/MD5Engine.h"
#include "Poco/DigestStream.h"

#include <iostream>

namespace po = boost::program_options;
using namespace std;

int main(int argc, char** argv)
{
  // ---- boost program options
  // Declare the supported options.
  po::options_description desc("Allowed options");
  desc.add_options()
    ("help", "produce help message")
    ("compression", po::value<int>(), "set compression level")
  ;

  po::variables_map vm;
  po::store(po::parse_command_line(argc, argv, desc), vm);
  po::notify(vm);    

  if (vm.count("help")) {
    cout << desc << "\n";
    return 1;
  }

  if (vm.count("compression")) {
    cout << "Compression level was set to " 
         << vm["compression"].as<int>() << ".\n";
  } else {
    cout << "Compression level was not set.\n";
  }


  // ---- poco md5
  Poco::MD5Engine md5;
  Poco::DigestOutputStream ds(md5);
  ds << "abcdefghijklmnopqrstuvwxyz";
  ds.close();
  cout << Poco::DigestEngine::digestToHex(md5.digest()) << endl;
  return 0;
}
