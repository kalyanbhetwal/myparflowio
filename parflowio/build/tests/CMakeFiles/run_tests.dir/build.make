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
include tests/CMakeFiles/run_tests.dir/depend.make

# Include the progress variables for this target.
include tests/CMakeFiles/run_tests.dir/progress.make

# Include the compile flags for this target's objects.
include tests/CMakeFiles/run_tests.dir/flags.make

tests/CMakeFiles/run_tests.dir/PFData_test.cpp.o: tests/CMakeFiles/run_tests.dir/flags.make
tests/CMakeFiles/run_tests.dir/PFData_test.cpp.o: ../tests/PFData_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/KALYANBHETWAL/parflowio/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object tests/CMakeFiles/run_tests.dir/PFData_test.cpp.o"
	cd /home/KALYANBHETWAL/parflowio/build/tests && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/run_tests.dir/PFData_test.cpp.o -c /home/KALYANBHETWAL/parflowio/tests/PFData_test.cpp

tests/CMakeFiles/run_tests.dir/PFData_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/run_tests.dir/PFData_test.cpp.i"
	cd /home/KALYANBHETWAL/parflowio/build/tests && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/KALYANBHETWAL/parflowio/tests/PFData_test.cpp > CMakeFiles/run_tests.dir/PFData_test.cpp.i

tests/CMakeFiles/run_tests.dir/PFData_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/run_tests.dir/PFData_test.cpp.s"
	cd /home/KALYANBHETWAL/parflowio/build/tests && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/KALYANBHETWAL/parflowio/tests/PFData_test.cpp -o CMakeFiles/run_tests.dir/PFData_test.cpp.s

# Object files for target run_tests
run_tests_OBJECTS = \
"CMakeFiles/run_tests.dir/PFData_test.cpp.o"

# External object files for target run_tests
run_tests_EXTERNAL_OBJECTS = \
"/home/KALYANBHETWAL/parflowio/build/src/CMakeFiles/parflowio.dir/pfdata.cpp.o" \
"/home/KALYANBHETWAL/parflowio/build/src/CMakeFiles/parflowio.dir/pfutil.cpp.o"

tests/run_tests: tests/CMakeFiles/run_tests.dir/PFData_test.cpp.o
tests/run_tests: src/CMakeFiles/parflowio.dir/pfdata.cpp.o
tests/run_tests: src/CMakeFiles/parflowio.dir/pfutil.cpp.o
tests/run_tests: tests/CMakeFiles/run_tests.dir/build.make
tests/run_tests: lib/libgtest.a
tests/run_tests: lib/libgtest_main.a
tests/run_tests: lib/libgtest.a
tests/run_tests: tests/CMakeFiles/run_tests.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/KALYANBHETWAL/parflowio/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable run_tests"
	cd /home/KALYANBHETWAL/parflowio/build/tests && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/run_tests.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/CMakeFiles/run_tests.dir/build: tests/run_tests

.PHONY : tests/CMakeFiles/run_tests.dir/build

tests/CMakeFiles/run_tests.dir/clean:
	cd /home/KALYANBHETWAL/parflowio/build/tests && $(CMAKE_COMMAND) -P CMakeFiles/run_tests.dir/cmake_clean.cmake
.PHONY : tests/CMakeFiles/run_tests.dir/clean

tests/CMakeFiles/run_tests.dir/depend:
	cd /home/KALYANBHETWAL/parflowio/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/KALYANBHETWAL/parflowio /home/KALYANBHETWAL/parflowio/tests /home/KALYANBHETWAL/parflowio/build /home/KALYANBHETWAL/parflowio/build/tests /home/KALYANBHETWAL/parflowio/build/tests/CMakeFiles/run_tests.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/CMakeFiles/run_tests.dir/depend

