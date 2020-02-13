cmake_minimum_required(VERSION 2.8.3)
project(temizlik_robotu_yayinci_abone_ornek_msgs)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

 add_message_files(
   FILES
   MesafeBilgisiOrnek.msg
 )

 generate_messages(
   DEPENDENCIES
   std_msgs
 )


catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

foreach(dir include msg)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach()
