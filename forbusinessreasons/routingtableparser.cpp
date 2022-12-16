/*  reads and parses /proc/net/route
 *
 *  $ g++ routingtableparser.cpp -std=c++11
 *  should not require root priviledges
 *  
 */

#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <arpa/inet.h>
#include <net/route.h>

enum class Flag : unsigned short {
  UNKNWOWN,
  UP = RTF_UP,
  GATEWAY = RTF_GATEWAY,
  HOST = RTF_HOST,
  REINSTATE = RTF_REINSTATE,
  DYNAMIC = RTF_DYNAMIC,
  MODIFIED = RTF_MODIFIED,
  MTU = RTF_MTU,
  MSS = RTF_MSS,
  WINDOW = RTF_WINDOW,
  IRTT = RTF_IRTT,
  REJECT = RTF_REJECT,
  STATIC = RTF_STATIC,
  XRESOLVE = RTF_XRESOLVE,
  NOFORWARD = RTF_NOFORWARD,
  THROW = RTF_THROW,
  NOPMTUDISC = RTF_NOPMTUDISC,
};

struct route {
  std::string iface;
  std::string destination;
  std::string gateway;
  std::vector<Flag> flags;
  std::string refcnt;
  std::string use;
  std::string metric;
  std::string mask;
  std::string mtu;
  std::string window;
  std::string irtt;

  friend std::ostream& operator<<(std::ostream& os, const struct route& rt){

    std::cout << "iface:\t\t" << rt.iface << "\n" <<
                 "destination:\t" << rt.destination << "\n" <<
                 "gateway:\t" << rt.gateway << "\n" <<
                 "mask:\t\t" << rt.mask << "\n" <<
                 "metric:\t\t" << rt.metric << "\n";
    std::for_each(rt.flags.begin(), rt.flags.end(),[](const Flag& f){
        std::cout << (unsigned short) f << " ";
        } );
    std::cout << std::endl;
  }
};

void convertToHumanReadableIp(std::string& reversed){
  std::string result;
  int iparr[4], j = 0;
  for(unsigned int i = reversed.length(); i > 0 ; i -= 2, j++){
    std::stringstream iss;
    auto tmp = reversed.substr(i-2, 2);
    iss << tmp;
    iss >> std::hex >> iparr[j];
  }

  for(int i = 0; i < 4 ; i ++){
    result += (i == 3) ? std::to_string(iparr[i]) : std::to_string(iparr[i]) + ".";
  }
  reversed = result; 
}

void parseFlags(std::string flagstr, std::vector<Flag>& flag){
  auto i = std::stoi(flagstr);

  if( i & (unsigned short) Flag::UP ) { flag.push_back(Flag::UP); }
  if( i & (unsigned short) Flag::GATEWAY ) { flag.push_back(Flag::GATEWAY); }
  if( i & (unsigned short) Flag::HOST ) { flag.push_back(Flag::HOST); }
  if( i & (unsigned short) Flag::REINSTATE ) { flag.push_back(Flag::REINSTATE); }
  if( i & (unsigned short) Flag::DYNAMIC ) { flag.push_back(Flag::DYNAMIC); }
  if( i & (unsigned short) Flag::MODIFIED ) { flag.push_back(Flag::MODIFIED); }
  if( i & (unsigned short) Flag::MTU ) { flag.push_back(Flag::MTU); }
  if( i & (unsigned short) Flag::MSS ) { flag.push_back(Flag::MSS); }
  if( i & (unsigned short) Flag::WINDOW ) { flag.push_back(Flag::WINDOW); }
  if( i & (unsigned short) Flag::IRTT ) { flag.push_back(Flag::IRTT); }
  if( i & (unsigned short) Flag::REJECT ) { flag.push_back(Flag::REJECT); }
  if( i & (unsigned short) Flag::STATIC ) { flag.push_back(Flag::STATIC); }
  if( i & (unsigned short) Flag::XRESOLVE ) { flag.push_back(Flag::XRESOLVE); }
  if( i & (unsigned short) Flag::NOFORWARD ) { flag.push_back(Flag::NOFORWARD); }
  if( i & (unsigned short) Flag::THROW ) { flag.push_back(Flag::THROW); }
  if( i & (unsigned short) Flag::NOPMTUDISC ) { flag.push_back(Flag::NOPMTUDISC); }



}

std::vector<struct route> listRoutes(){
  std::ifstream file;
  file.open("/proc/net/route");
  std::vector<struct route> result;
  for(std::string line, temp; getline(file, line); ){
    std::stringstream iss(line);
    getline(iss, temp, '\t');
    if(temp == "Iface"){
      continue;
    }
    char ip_tmp[INET_ADDRSTRLEN];
    struct route rt;
    rt.iface = temp;
    getline(iss, rt.destination, '\t');
    getline(iss, rt.gateway, '\t');
    getline(iss, temp, '\t');

    parseFlags(temp, rt.flags);

    getline(iss, rt.refcnt, '\t');
    getline(iss, rt.use, '\t');
    getline(iss, rt.metric, '\t');
    getline(iss, rt.mask, '\t');
    getline(iss, rt.mtu, '\t');
    getline(iss, rt.window, '\t');
    getline(iss, rt.irtt, '\t');


    convertToHumanReadableIp(rt.destination);
    convertToHumanReadableIp(rt.gateway);
    convertToHumanReadableIp(rt.mask);
    

    result.push_back(rt);
  }
  return result;
}


int main(int argc, char ** argv){

  auto list = listRoutes();

  std::for_each(list.begin(), list.end(), [](const struct route& rt){
        std::cout << rt << std::endl;
      });

  return 0;
}