file(REMOVE_RECURSE
  "libparflowio_static.a"
  "libparflowio_static.pdb"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/parflowio_static.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
