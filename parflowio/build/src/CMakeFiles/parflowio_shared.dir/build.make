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
include src/CMakeFiles/parflowio_shared.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/parflowio_shared.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/parflowio_shared.dir/flags.make

# Object files for target parflowio_shared
parflowio_shared_OBJECTS =

# External object files for target parflowio_shared
parflowio_shared_EXTERNAL_OBJECTS = \
"/home/KALYANBHETWAL/parflowio/build/src/CMakeFiles/parflowio.dir/pfdata.cpp.o" \
"/home/KALYANBHETWAL/parflowio/build/src/CMakeFiles/parflowio.dir/pfutil.cpp.o"

src/libparflowio_shared.so: src/CMakeFiles/parflowio.dir/pfdata.cpp.o
src/libparflowio_shared.so: src/CMakeFiles/parflowio.dir/pfutil.cpp.o
src/libparflowio_shared.so: src/CMakeFiles/parflowio_shared.dir/build.make
src/libparflowio_shared.so: src/CMakeFiles/parflowio_shared.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/KALYANBHETWAL/parflowio/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Linking CXX shared library libparflowio_shared.so"
	cd /home/KALYANBHETWAL/parflowio/build/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/parflowio_shared.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/parflowio_shared.dir/build: src/libparflowio_shared.so

.PHONY : src/CMakeFiles/parflowio_shared.dir/build

src/CMakeFiles/parflowio_shared.dir/clean:
	cd /home/KALYANBHETWAL/parflowio/build/src && $(CMAKE_COMMAND) -P CMakeFiles/parflowio_shared.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/parflowio_shared.dir/clean

src/CMakeFiles/parflowio_shared.dir/depend:
	cd /home/KALYANBHETWAL/parflowio/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/KALYANBHETWAL/parflowio /home/KALYANBHETWAL/parflowio/src /home/KALYANBHETWAL/parflowio/build /home/KALYANBHETWAL/parflowio/build/src /home/KALYANBHETWAL/parflowio/build/src/CMakeFiles/parflowio_shared.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/parflowio_shared.dir/depend

