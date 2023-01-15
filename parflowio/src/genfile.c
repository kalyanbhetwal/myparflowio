#undef s0
#undef s_0
#undef s1
#undef s_1
#undef s2
#undef s_2
#undef s3
#undef s_3
#undef s4
#undef s_4
#undef s5
#undef s_5
#undef s6
#undef s_6
#undef s7
#undef s_7
#undef s8
#undef s_8
#undef s9
#undef s_9
#undef s10
#undef s_10
#undef s11
#undef s_11
#undef s12
#undef s_12
#undef s13
#undef s_13
#undef s14
#undef s_14
#undef s15
#undef s_15
#define s_0(nsg)  int  x_overlap = fminl(clip_x+extent_x, x+nx) - fmaxl(clip_x,x)
#define s0(__x0, nsg, __x2)   s_0(nsg);
#define s_1(nsg)  int y_overlap = fminl(clip_y+extent_y, y+ny) - fmaxl(clip_y,y)
#define s1(__x0, nsg, __x2)   s_1(nsg);
#define s_2(nsg, k, i)   gx = x
#define s2(__x0, nsg, __x2, k, __x4, i, __x6)   s_2(nsg, k, i);
#define s_3(nsg, k, i)   gy = y + i
#define s3(__x0, nsg, __x2, k, __x4, i, __x6)   s_3(nsg, k, i);
#define s_4(nsg, k, i)   gz = z + k
#define s4(__x0, nsg, __x2, k, __x4, i, __x6)   s_4(nsg, k, i);
#define s_5(nsg, k, i)   cx = gx - clip_x
#define s5(__x0, nsg, __x2, k, __x4, i, __x6)   s_5(nsg, k, i);
#define s_6(nsg, k, i)   cy = gy - clip_y;
#define s6(__x0, nsg, __x2, k, __x4, i, __x6)   s_6(nsg, k, i);
#define s_7(nsg, k, i)   cz = gz
#define s7(__x0, nsg, __x2, k, __x4, i, __x6)   s_7(nsg, k, i);
#define s_8(nsg, k, i)   read_count = fread(buf,8,nx,m_fp)
#define s8(__x0, nsg, __x2, k, __x4, i, __x6)   s_8(nsg, k, i);
#define s_9(nsg, k, i, j)   cxi = cx+j
#define s9(__x0, nsg, __x2, k, __x4, i, __x6, j, __x8)   s_9(nsg, k, i, j);
#define s_10(nsg, k, i, j)   index = cz*(extent_y*extent_x) + cy*extent_x + cxi
#define s10(__x0, nsg, __x2, k, __x4, i, __x6, j, __x8)   s_10(nsg, k, i, j);
#define s_11(nsg, k, i, j)   tmp = buf[j]
#define s11(__x0, nsg, __x2, k, __x4, i, __x6, j, __x8)   s_11(nsg, k, i, j);
#define s_12(nsg, k, i, j)   tmp = bswap64(tmp)
#define s12(__x0, nsg, __x2, k, __x4, i, __x6, j, __x8)   s_12(nsg, k, i, j);
#define s_13(nsg, k, i, j)   m_data[index] = *(double*)(&tmp);m_data[index] = 2 * m_data[index]
#define s13(__x0, nsg, __x2, k, __x4, i, __x6, j, __x8)   s_13(nsg, k, i, j);
#define s_14(nsg, k, i)   std::fseek(m_fp, 8*nx, SEEK_CUR)
#define s14(__x0, nsg, __x2, k, __x4, i, __x6)   s_14(nsg, k, i);
#define s_15(nsg)   std::fseek(m_fp, 8*nx*ny*nz, SEEK_CUR)
#define s15(__x0, nsg, __x2)   s_15(nsg);


#define minx(a,b) a < b ? a :b
#define maxm(a,b) a > b ? a : b
#define min1(a,b,c)  (minx(minx((a), (b)), (c)))
//
int cx;
int cxi;
int cy;
int cz;
int gx;
int gy;
int gz;
//int nsg;
//int nx;
//int ny;
//int nz;
int read_count;
//int rx;
//int ry;
//int rz;

unsigned long long tmp;
//int x;
//int x_overlap;
//int y;
//int y_overlap;
//int z;
int index; //added

long long t1 = 0;
long long  t2 = 0;
long long  t3 = 0;
long long  t4 = 0;
long long  t5 = 0;
long long  t6 = 0;
long long  t7 = 0;
long long  t8 = 0;
long long  t9 = 0;


for(t2 = 0; t2 <= m_numSubgrids-1; t2++) {
//read the subgrid header
int errcheck;
READINT(x,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
READINT(y,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
READINT(z,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
READINT(nx,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
READINT(ny,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
READINT(nz,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
READINT(rx,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
READINT(ry,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
READINT(rz,m_fp,errcheck);
if(!errcheck){perror("Error Reading Subgrid Header"); return 1;}
s0(0,t2,0);
s1(0,t2,0);
if (x_overlap >= 1 && ny >= 1 && y_overlap >= 1) {
for(t4 = 0; t4 <= nz-1; t4++) {
for(t6 = 0; t6 <= ny-1; t6++) {
s2(0,t2,0,t4,0,t6,0);
s3(0,t2,0,t4,0,t6,0);
s4(0,t2,0,t4,0,t6,0);
s5(0,t2,0,t4,0,t6,0);
s6(0,t2,0,t4,0,t6,0);
s7(0,t2,0,t4,0,t6,0);
if (clip_y+extent_y >= gy+1 && gy >= clip_y) {
s8(0,t2,0,t4,0,t6,1);
for(t8 = std::max(0,clip_x-gx); t8 <= std::min(extent_x+clip_x-gx-1,nx-1); t8++) {
s9(0,t2,0,t4,0,t6,1,t8,0);
s10(0,t2,0,t4,0,t6,1,t8,0);
s11(0,t2,0,t4,0,t6,1,t8,0);
s12(0,t2,0,t4,0,t6,1,t8,0);
s13(0,t2,0,t4,0,t6,1,t8,0);
}
}
if (gy >= clip_y+extent_y) {
s14(0,t2,0,t4,0,t6,2);
}
else {
if (clip_y >= gy+1) {
s14(0,t2,0,t4,0,t6,2);
}
}
}
}
}
if (x_overlap <= 0) {
s15(0,t2,1);
}
else {
if (y_overlap <= 0) {
s15(0,t2,1);
}
}
}

#undef s0
#undef s_0
#undef s1
#undef s_1
#undef s2
#undef s_2
#undef s3
#undef s_3
#undef s4
#undef s_4
#undef s5
#undef s_5
#undef s6
#undef s_6
#undef s7
#undef s_7
#undef s8
#undef s_8
#undef s9
#undef s_9
#undef s10
#undef s_10
#undef s11
#undef s_11
#undef s12
#undef s_12
#undef s13
#undef s_13
#undef s14
#undef s_14
#undef s15
#undef s_15
#undef min
