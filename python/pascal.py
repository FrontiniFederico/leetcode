class Solution(object):
    def generate(self, numRows):

        #the idea is to use an output 2d array
        output = []

        for i in range(numRows):
          #we manually populate the first two rows
          if i == 0:
            output.append([1])
          elif i == 1:
            output.append([1,1])
          else:
            prev = output[-1] #prev is the last populated row
            curr = [1,1] #placeholder, we are gonna add elements as we go
            for indice in range(len(prev)-1): #we don't want to go out of bounds
                curr.insert(-1, prev[indice] + prev[indice+1])
            output.append(curr) 

        return output
    
    #this one has a much better runtime but still uses a lot of memory...
    def betterGenerate(self, numRows):
        output = [[1]]
        for i in range(2, numRows+1):
          curr = [1]*i #I already know how many elements this row is gonna get
          for j in range(1, i-1):
            curr[j] = output[i-2][j]+output[i-2][j-1]
        output.append(curr)
        return output


