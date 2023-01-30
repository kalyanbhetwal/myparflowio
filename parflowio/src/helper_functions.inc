

// int calcOffset(int extent, int block_count, int block_idx) {
//     int lx = extent % block_count;
//     int bx = extent / block_count;
//     int offset =  block_idx * bx;
//     if (block_idx < lx) {
//         offset += block_idx;
//     }else{
//         offset += lx;
//     }
//     return offset;
// }