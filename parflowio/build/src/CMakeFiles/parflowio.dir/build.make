# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Produce verbose output by default.
VERBOSE = 1

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/apps/cmake/bin/cmake

# The command to remove a file.
RM = /usr/local/apps/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/KALYANBHETWAL/parflowio

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/KALYANBHETWAL/parflowio/build

# Include any dependencies generated for this target.
include src/CMakeFiles/parflowio.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/parflowio.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/parflowio.dir/flags.make

src/CMakeFiles/parflowio.dir/pfdata.cpp.o: src/CMakeFiles/parflowio.dir/flags.make
src/CMakeFiles/parflowio.dir/pfdata.cpp.o: ../src/pfdata.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/KALYANBHETWAL/parflowio/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/parflowio.dir/pfdata.cpp.o"
	cd /home/KALYANBHETWAL/parflowio/build/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/parflowio.dir/pfdata.cpp.o -c /home/KALYANBHETWAL/parflowio/src/pfdata.cpp

src/CMakeFiles/parflowio.dir/pfdata.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/parflowio.dir/pfdata.cpp.i"
	cd /home/KALYANBHETWAL/parflowio/build/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/KALYANBHETWAL/parflowio/src/pfdata.cpp > CMakeFiles/parflowio.dir/pfdata.cpp.i

src/CMakeFiles/parflowio.dir/pfdata.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/parflowio.dir/pfdata.cpp.s"
	cd /home/KALYANBHETWAL/parflowio/build/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/KALYANBHETWAL/parflowio/src/pfdata.cpp -o CMakeFiles/parflowio.dir/pfdata.cpp.s

src/CMakeFiles/parflowio.dir/pfutil.cpp.o: src/CMakeFiles/parflowio.dir/flags.make
src/CMakeFiles/parflowio.dir/pfutil.cpp.o: ../src/pfutil.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/KALYANBHETWAL/parflowio/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object src/CMakeFiles/parflowio.dir/pfutil.cpp.o"
	cd /home/KALYANBHETWAL/parflowio/build/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/parflowio.dir/pfutil.cpp.o -c /home/KALYANBHETWAL/parflowio/src/pfutil.cpp

src/CMakeFiles/parflowio.dir/pfutil.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/parflowio.dir/pfutil.cpp.i"
	cd /home/KALYANBHETWAL/parflowio/build/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/KALYANBHETWAL/parflowio/src/pfutil.cpp > CMakeFiles/parflowio.dir/pfutil.cpp.i

src/CMakeFiles/parflowio.dir/pfutil.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/parflowio.dir/pfutil.cpp.s"
	cd /home/KALYANBHETWAL/parflowio/build/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/KALYANBHETWAL/parflowio/src/pfutil.cpp -o CMakeFiles/parflowio.dir/pfutil.cpp.s

parflowio: src/CMakeFiles/parflowio.dir/pfdata.cpp.o
parflowio: src/CMakeFiles/parflowio.dir/pfutil.cpp.o
parflowio: src/CMakeFiles/parflowio.dir/build.make

.PHONY : parflowio

# Rule to build all files generated by this target.
src/CMakeFiles/parflowio.dir/build: parflowio

.PHONY : src/CMakeFiles/parflowio.dir/build

src/CMakeFiles/parflowio.dir/clean:
	cd /home/KALYANBHETWAL/parflowio/build/src && $(CMAKE_COMMAND) -P CMakeFiles/parflowio.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/parflowio.dir/clean

src/CMakeFiles/parflowio.dir/depend:
	cd /home/KALYANBHETWAL/parflowio/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/KALYANBHETWAL/parflowio /home/KALYANBHETWAL/parflowio/src /home/KALYANBHETWAL/parflowio/build /home/KALYANBHETWAL/parflowio/build/src /home/KALYANBHETWAL/parflowio/build/src/CMakeFiles/parflowio.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/parflowio.dir/depend

