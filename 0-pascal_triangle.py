def pascal_triangle(n):
    pas_triangle=[]
    if n<=0:
        return pas_triangle
    else:
        pas_triangle=[[1] for _ in range(n)]
        for i in range(n-1):
            prevous=0
            k=0
            j=0
            while j<len(pas_triangle[i]):
                pas_triangle[i+1][k]=prevous + pas_triangle[i][k]
                pas_triangle[i+1].append(1)
                prevous=pas_triangle[i][k]
                k+=1
                j+=1
        return pas_triangle
    
    