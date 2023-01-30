#include "pfutil.hpp"

#define minx(a,b) a < b ? a :b
#define maxm(a,b) a > b ? a : b
#define min1(a,b,c)  (minx(minx((a), (b)), (c)))
#define max1(a,b,c)  (maxm(maxm((a), (b)), (c)))
#define max4(a,b,c,d) maxm(maxm(maxm((a), (b)), (c)),d)

#define WRITEINT(V,f) {uint32_t temp = bswap32(V); \
                         fwrite(&temp, 4, 1, f);}
#define READINT(V,f,err) {uint32_t buf; \
                         err = fread(&buf, 4, 1, f);\
                         uint32_t temp =  bswap32(buf);\
                         V = (int)temp;}
#define WRITEDOUBLE(V,f) {uint64_t t1 = *(uint64_t*)&V;\
                         t1 =  bswap64(t1); \
                         fwrite(&t1, 8, 1, f);}
#define READDOUBLE(V,f,err) {uint64_t buf; \
                         err = fread(&buf, 8, 1, f);\
                         uint64_t temp =  bswap64(buf);\
                         V = *(double*)&temp;}

long* _offsets;
uint64_t* buf;
long* byte_offsets;
int clip_x;
int errcheck;
int extent_x;
FILE* fp;
long long index;
long long iy_max;
long long iy_min ;
long long iz_max;
long long iz_min;
double m_X;
double m_Y;
double m_Z;
double m_dX;
double m_dY;
double m_dZ;
double* m_data;
FILE* m_fp;
double m_numSubgrids;
uint64_t m_nx;
uint64_t m_ny;
int m_nz;
int m_p;
int m_q;
int m_r;
int max_x_extent;
double* mean;
int nsg;
int nx;
int ny;
int nz;
int qq;
double read_count;
int rx;
int ry;
int rz;
long long sg_count;
double sum;
uint64_t tmp;
double* writeBuf;

int x;
int x_extent;
int x_overlap;
int y;
int z;

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
#undef s16
#undef s_16
#undef s17
#undef s_17
#undef s18
#undef s_18
#undef s19
#undef s_19
#undef s20
#undef s_20
#undef s21
#undef s_21
#undef s22
#undef s_22
#undef s23
#undef s_23
#define s_0(c_0)   m_fp = fopen( m_filename.c_str(), "rb"); 
#define s0(__x0)   s_0(__x0);
#define s_1(c_0)   READDOUBLE(m_X,m_fp,errcheck);    READDOUBLE(m_Y,m_fp,errcheck);    READDOUBLE(m_Z,m_fp,errcheck);    READINT(m_nx,m_fp,errcheck);    READINT(m_ny,m_fp,errcheck);    READINT(m_nz,m_fp,errcheck);    READDOUBLE(m_dX,m_fp,errcheck);    READDOUBLE(m_dY,m_fp,errcheck);    READDOUBLE(m_dZ,m_fp,errcheck);    READINT(m_numSubgrids,m_fp,errcheck); 
#define s1(__x0)   s_1(__x0);
#define s_2(c_0)   m_data = (double*)malloc(sizeof(double)*m_nx*m_ny*m_nz); 
#define s2(__x0)   s_2(__x0);
#define s_3(nsg)   READINT(x,m_fp,errcheck);READINT(y,m_fp,errcheck);READINT(z,m_fp,errcheck);READINT(nx,m_fp,errcheck);READINT(ny,m_fp,errcheck);READINT(nz,m_fp,errcheck);READINT(rx,m_fp,errcheck);READINT(ry,m_fp,errcheck);READINT(rz,m_fp,errcheck); 
#define s3(__x0, nsg, __x2)   s_3(nsg);
#define s_4(nsg)   qq = z*m_nx*m_ny + y*m_nx + x; 
#define s4(__x0, nsg, __x2)   s_4(nsg);
#define s_5(nsg, k, i)   index = qq+k*m_nx*m_ny+i*m_nx; buf = (uint64_t*)&(m_data[index]);read_count = fread(buf,8,nx,m_fp); 
#define s5(__x0, nsg, __x2, k, __x4, i, __x6)   s_5(nsg, k, i);
#define s_6(nsg, k, i, j)   tmp = buf[j];  tmp = bswap64(tmp);  m_data[index+j] = *(double*)(&tmp); 
#define s6(__x0, nsg, __x2, k, __x4, i, __x6, j, __x8)   s_6(nsg, k, i, j);
#define s_7(c_0)   mean = (double*)malloc(sizeof(double)*m_ny*m_nx); 
#define s7(__x0)   s_7(__x0);
#define s_8(y, x)   sum=0; 
#define s8(__x0, y, __x2, x, __x4)   s_8(y, x);
#define s_9(y, x, z)   sum+=m_data[(long long)(z)*m_ny*m_nx+y*m_nx+x]; 
#define s9(__x0, y, __x2, x, __x4, z, __x6)   s_9(y, x, z);
#define s_10(y, x)   mean[x+y*m_nx] = sum/m_nz; 
#define s10(__x0, y, __x2, x, __x4)   s_10(y, x);
#define s_11(c_0)   m_p=1;m_q=1;m_r=1;_offsets =(long*)malloc(sizeof(long)* ((m_p*m_q*m_r) + 1));m_nz=1; 
#define s11(__x0)   s_11(__x0);
#define s_12(c_0)   fp = std::fopen(filename.c_str(), "wb"); 
#define s12(__x0)   s_12(__x0);
#define s_13(c_0)   m_numSubgrids = m_p * m_q * m_r;    WRITEDOUBLE(m_X,fp);    WRITEDOUBLE(m_Y,fp);    WRITEDOUBLE(m_Z,fp);    WRITEINT(m_nx,fp);    WRITEINT(m_ny,fp);    WRITEINT(m_nz,fp);    WRITEDOUBLE(m_dX,fp);    WRITEDOUBLE(m_dY,fp);    WRITEDOUBLE(m_dZ,fp);    WRITEINT(m_numSubgrids,fp);max_x_extent =calcExtent(m_nx,m_p,0); 
#define s13(__x0)   s_13(__x0);
#define s_14(c_0)   writeBuf = (double*)malloc(sizeof(double)*max_x_extent); 
#define s14(__x0)   s_14(__x0);
#define s_15(c_0)   nsg=0; byte_offsets[0] = 0;sg_count = 1; 
#define s15(__x0)   s_15(__x0);
#define s_16(nsg_z, nsg_y, nsg_x)   x = m_X + calcOffset(m_nx,m_p,nsg_x);y = m_Y + calcOffset(m_ny,m_q,nsg_y);z = m_Z + calcOffset(m_nz,m_r,nsg_z);WRITEINT(x, fp);WRITEINT(y, fp);WRITEINT(z, fp);x_extent =calcExtent(m_nx,m_p,nsg_x);WRITEINT(x_extent, fp);WRITEINT(calcExtent(m_ny,m_q,nsg_y), fp);WRITEINT(calcExtent(m_nz,m_r,nsg_z), fp);WRITEINT(1, fp);WRITEINT(1, fp);WRITEINT(1, fp); 
#define s16(__x0, nsg_z, __x2, nsg_y, __x4, nsg_x, __x6)   s_16(nsg_z, nsg_y, nsg_x);
#define s_17(nsg_z, nsg_y, nsg_x)   iz_min=calcOffset(m_nz,m_r,nsg_z);iz_max=calcOffset(m_nz,m_r,nsg_z+1);iy_min=calcOffset(m_ny,m_q,nsg_y); iy_max= calcOffset(m_ny,m_q,nsg_y+1); 
#define s17(__x0, nsg_z, __x2, nsg_y, __x4, nsg_x, __x6)   s_17(nsg_z, nsg_y, nsg_x);
#define s_18(nsg_z, nsg_y, nsg_x, iz, iy)  buf = (uint64_t*)&(m_data[iz*m_nx*m_ny+iy*m_nx+calcOffset(m_nx,m_p,nsg_x)]); 
#define s18(__x0, nsg_z, __x2, nsg_y, __x4, nsg_x, __x6, iz, __x8, iy, __x10)   s_18(nsg_z, nsg_y, nsg_x, iz, iy);
#define s_19(nsg_z, nsg_y, nsg_x, iz, iy, j) tmp = buf[j]; tmp = bswap64(tmp); writeBuf[j] = *(double*)(&tmp); 
#define s19(__x0, nsg_z, __x2, nsg_y, __x4, nsg_x, __x6, iz, __x8, iy, __x10, j, __x12)   s_19(nsg_z, nsg_y, nsg_x, iz, iy, j);
#define s_20(nsg_z, nsg_y, nsg_x, iz, iy)   fwrite(writeBuf.data(),sizeof(double),x_extent,fp); 
#define s20(__x0, nsg_z, __x2, nsg_y, __x4, nsg_x, __x6, iz, __x8, iy, __x10)   s_20(nsg_z, nsg_y, nsg_x, iz, iy);
#define s_21(nsg_z, nsg_y, nsg_x)   byte_offsets[sg_count] = ftell(fp); sg_count++; 
#define s21(__x0, nsg_z, __x2, nsg_y, __x4, nsg_x, __x6)   s_21(nsg_z, nsg_y, nsg_x);
#define s_22(nsg_z)   nsg= nsg+1; 
#define s22(__x0, nsg_z, __x2)   s_22(nsg_z);
#define s_23(c_0)   fclose(fp); 
#define s23(__x0)   s_23(__x0);


int t1 = 11; 
int t2 = 0; 
int t3 = 1; 
int t4 = 0; 
int t5 = 0; 
int t6 = 0; 
int t7 = 3; 
int t8 = 0; 
int t9 = 0; 
int t10 = 0; 
int t11 = 2; 
int t12 = 0; 
int t13 = 0; 

s0(0);
s1(1);
s2(2);
for(t2 = 0; t2 <= m_numSubgrids-1; t2++) {
  s3(3,t2,0);
  s4(3,t2,1);
  if (ny >= 1) {
    for(t4 = 0; t4 <= nz-1; t4++) {
      for(t6 = 0; t6 <= ny-1; t6++) {
        s5(3,t2,2,t4,0,t6,0);
        for(t8 = 0; t8 <= nx-1; t8++) {
          s6(3,t2,2,t4,0,t6,1,t8,0);
        }
      }
    }
  }
}
// std::fclose(m_fp);
// m_fp = nullptr;
s7(4);
if (m_nx >= 1) {
  for(t2 = 0; t2 <= m_ny-1; t2++) {
    for(t4 = 0; t4 <= m_nx-1; t4++) {
      s8(4,t2,0,t4,0);
      for(t6 = 0; t6 <= m_nz-1; t6++) {
        s9(4,t2,0,t4,1,t6,0);
      }
      s10(4,t2,0,t4,2);
    }
  }
}
m_data = mean;
s11(5);
s12(6);
s13(7);
//std::cout<<"the value of max_x_extent "<< max_x_extent <<std::endl;
//writeBuf = (double*)malloc(sizeof(double)*max_x_extent); 
//s14(8);
s15(9);
for(t2 = 0; t2 <= m_r-1; t2++) {
  if (m_p >= 1) {
    for(t4 = 0; t4 <= m_q-1; t4++) {
      for(t6 = 0; t6 <= m_p-1; t6++) {
        s16(10,t2,0,t4,0,t6,0);
        s17(10,t2,0,t4,0,t6,1);
        if (iy_max >= iy_min+1) {
          for(t8 = iz_min; t8 <= iz_max-1; t8++) {
            for(t10 = iy_min; t10 <= iy_max-1; t10++) {
              std::vector<double> writeBuf(max_x_extent);
              s18(10,t2,0,t4,0,t6,2,t8,0,t10,0);
              //uint64_t* buf = (uint64_t*)&(m_data[t8*m_nx*m_ny+t9*m_nx+calcOffset(m_nx,m_p,t6)]);
              for(t12 = 0; t12 <= x_extent-1; t12++) {
                //std::cout<< "the value of buf " << buf[t12]<<std::endl;
                //  tmp = buf[t12]; 
                //  tmp = bswap64(tmp);
                //  writeBuf[t12] = *(double*)(&tmp); 
                s19(10,t2,0,t4,0,t6,2,t8,0,t10,1,t12,0);
              }
              
             // s20(10,t2,0,t4,0,t6,2,t8,0,t10,2);
              fwrite(writeBuf.data(),sizeof(double),x_extent,fp); 
              std::cout<< "the written data "<<writeBuf.data()<<std::endl;
            }
          }
        }
        s21(10,t2,0,t4,0,t6,3);
      }
    }
  }
  s22(10,t2,1);
}
s23(11);

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
#undef s16
#undef s_16
#undef s17
#undef s_17
#undef s18
#undef s_18
#undef s19
#undef s_19
#undef s20
#undef s_20
#undef s21
#undef s_21
#undef s22
#undef s_22
#undef s23
#undef s_23
