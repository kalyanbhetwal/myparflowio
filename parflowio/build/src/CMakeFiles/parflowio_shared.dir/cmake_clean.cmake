file(REMOVE_RECURSE
  "libparflowio_shared.pdb"
  "libparflowio_shared.so"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/parflowio_shared.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
