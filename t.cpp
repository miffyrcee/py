#defineMAXN1000
#defineINF1<<30
intclosest[MAXN],lowcost[MAXN],m;//m为节点的个数
intG[MAXN][MAXN];//邻接矩阵
intprim()
{
for(inti=0;i<m;i++)
{
lowcost[i]=INF;
}
for(inti=0;i<m;i++)
{
closest[i]=0;
}
closest[0]=-1;//加入第一个点，-1表示该点在集合U中，否则在集合V中
intnum=0,ans=0,e=0;//e为最新加入集合的点
while(num<m-1)//加入m-1条边
{
intmicost=INF,miedge=-1;
for(inti=0;i<m;i++)
if(closest[i]!=-1)
{
inttemp=G[e][i];
if(temp<lowcost[i])
{
lowcost[i]=temp;
closest[i]=e;
}
if(lowcost[i]<micost)
micost=lowcost[miedge=i];
}
ans+=micost;
closest[e=miedge]=-1;
num++;
}
returnans;
}

