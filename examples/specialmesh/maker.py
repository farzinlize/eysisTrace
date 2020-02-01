def main():
    st = ""
    #define 12 * 14 mesh
    for j in range(14):
        for i in range(12):
            line = "router " + str(j*12+i) + " node " + str(j*12+i)
            if(i != 11):
                line += " router " + str(j*12+i+1)
            if(i != 0):
                line += " router " + str(j*12+i-1)
            if(j != 0):
                line += " router " + str((j-1)*12+i)
            if(j != 14):
                line += " router " + str((j+1)*12+i)
            st = st + line + "\n"
    extraline = "router " + str(12*14) + " node " + str(12*14)
    for each in range(12*14):
        extraline += " router " + str(each)
    st = st + extraline + "\n"
    result = open("mesh_anynet", "w")
    result.write(st)
    result.close()
    


main()